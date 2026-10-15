#!/usr/bin/env python3
"""Authoring build for s23-symmetric-shred. Reads source.txt, applies the seeded shred
plan, writes the fixture's transcript.txt and this folder's truth.tsv, shreds.json,
plan.json and stats.json.

Do not re-run this after the fixture has been reviewed: it writes over the transcript
from the pre-review source (the same caution COVERAGE.md gives for every build script).
check.py is the read-only verifier."""
import json
import os
import random
import re

HERE = os.path.dirname(os.path.abspath(__file__))
FIX = os.path.join(HERE, '..', '..', 'fixtures', 's23-symmetric-shred')
NAMES = {'C': 'Consultant', 'M': 'Maren Solberg', 'P': 'Perpetua Thackeray',
         'L': 'Liesl Vandermeulen', 'T': 'Tariq Paulsen'}
SIDE = {'C': 'own', 'M': 'own', 'P': 'client', 'L': 'client', 'T': 'client'}
PACE = 2.8      # words per second
GAP = 0.7       # seconds between turns
SEED = 2311
EXTRA_EVENTS = 26       # generic shreds on top of the Tariq-adjacent ones
ORPHANS = 10            # head fragments emitted as short turns of their own
SAME_LABEL_SPLITS = 22
T_TARGET = 0.033        # Tariq's raw share overstates the true one by at least this share of all words
SPAN = re.compile(r'\{([A-Z])(!?):([^}]*)\}')


def words(text):
    return [w for w in text.split() if not (w.startswith('[') and w.endswith(']')) and w != '--']


def parse(path):
    turns = []
    pause = 0.0
    duet = None
    for raw in open(path, encoding='utf-8'):
        line = raw.rstrip('\n')
        if not line or line.startswith('#'):
            continue
        if line.startswith('@pause'):
            pause += float(line.split()[1])
            continue
        if line == '@duet-start':
            duet = ['open', len(turns)]
            continue
        if line == '@duet-end':
            duet = ['closed', duet[1], len(turns)]
            continue
        label, text = line.split('|', 1)
        keep = label.endswith('=')
        soft = label.endswith('~')
        label = label.rstrip('=~')
        segs = []
        pos = 0
        for m in SPAN.finditer(text):
            if m.start() > pos:
                segs.append([label, text[pos:m.start()], False])
            segs.append([m.group(1), m.group(3), m.group(2) == '!'])
            pos = m.end()
        if pos < len(text):
            segs.append([label, text[pos:], False])
        turns.append({'label': label, 'segs': segs, 'pause': pause, 'hand': bool(SPAN.search(text)),
                      'flags': {'keep'} if keep else ({'soft'} if soft else set())})
        pause = 0.0
    return turns, duet


def text_of(tu):
    return ''.join(s[1] for s in tu['segs'])


def plain(tu):
    return len(tu['segs']) == 1 and not tu['hand']


def movable(toks):
    return all(not (w.startswith('[') and w.endswith(']')) and w != '--' for w in toks)


def take_head(tu, k):
    """Remove the first k words of the turn's own leading segment; return them."""
    t = tu['segs'][0][1]
    toks = t.split()
    frag, rest = toks[:k], toks[k:]
    tu['segs'][0][1] = ' '.join(rest) + (' ' if len(tu['segs']) > 1 else '')
    return ' '.join(frag)


def take_tail(tu, k):
    t = tu['segs'][-1][1]
    toks = t.split()
    frag, rest = toks[-k:], toks[:-k]
    tu['segs'][-1][1] = (' ' if len(tu['segs']) > 1 else '') + ' '.join(rest)
    return ' '.join(frag)


def eligible(tu, i, protected):
    if i in protected or not plain(tu) or 'assent' in tu['flags']:
        return False
    n = len(words(text_of(tu)))
    return 3 <= n <= 100


def flows(turns, extra=()):
    x = y = 0
    for tu in list(turns) + [o[1] for o in extra]:
        for owner, seg, assent in tu['segs']:
            if owner == tu['label'] or SIDE[owner] == SIDE[tu['label']]:
                continue
            n = len(words(seg))
            if SIDE[owner] == 'client':
                x += n
            else:
                y += n
    return x, y


def auto_shred(turns, duet, rng):
    protected = set()
    if duet:
        protected.update(range(duet[1] - 1, duet[2] + 1))
    for i, tu in enumerate(turns):
        if any(s[2] for s in tu['segs']):
            tu['flags'].add('assent')
    plan = []
    used_boundary = set()
    orphans = []   # (insert after index, turn)

    def donor_ok(i, end):
        tu = turns[i]
        if i in protected or 'assent' in tu['flags'] or ('donor-' + end) in tu['flags'] or 'orphan' in tu['flags'] or 'keep' in tu['flags']:
            return False
        seg = tu['segs'][0] if end == 'head' else tu['segs'][-1]
        if seg[0] != tu['label'] or seg[2]:
            return False
        return 4 <= len(words(seg[1])) and len(words(text_of(tu))) <= 100

    def receiver_ok(i):
        tu = turns[i]
        return i not in protected and 'assent' not in tu['flags'] and len(words(text_of(tu))) <= 100

    def head_shred(i, k, orphan=False):
        # boundary (i, i+1): the first k words of turn i+1 land at the end of turn i
        # (or, as an orphan, become a short turn of their own under turn i's label)
        a, b = turns[i], turns[i + 1]
        if 'soft' in b['flags']:
            k = min(k, 3)
        toks = b['segs'][0][1].split()
        if len(toks) < k + 3 or not movable(toks[:k]):
            return False
        frag = take_head(b, k)
        if orphan:
            orphans.append((i, {'label': a['label'], 'segs': [[b['label'], frag, False]], 'pause': 0.0,
                               'hand': True, 'flags': {'orphan'}}))
        else:
            a['segs'].append([b['label'], ' ' + frag, False])
        b['flags'].add('donor-head')
        used_boundary.add(i)
        plan.append({'boundary': i, 'kind': 'orphan-head' if orphan else 'head', 'k': k,
                     'owner': b['label'], 'under': a['label'], 'frag': frag})
        return True

    def tail_shred(i, k):
        # boundary (i, i+1): the last k words of turn i land at the start of turn i+1
        a, b = turns[i], turns[i + 1]
        if 'soft' in a['flags']:
            k = min(k, 3)
        toks = a['segs'][-1][1].split()
        if len(toks) < k + 3 or not movable(toks[-k:]):
            return False
        frag = take_tail(a, k)
        b['segs'].insert(0, [a['label'], frag + ' ', False])
        a['flags'].add('donor-tail')
        used_boundary.add(i)
        plan.append({'boundary': i, 'kind': 'tail', 'k': k, 'owner': a['label'], 'under': b['label'], 'frag': frag})
        return True

    def boundary_ok(i, donor, receiver):
        end = 'head' if donor == i + 1 else 'tail'
        return (i not in used_boundary and 0 <= i < len(turns) - 1
                and donor_ok(donor, end) and receiver_ok(receiver)
                and turns[i]['label'] != turns[i + 1]['label'])

    # 1. Tariq-adjacent: the neighbours shed words into Tariq's label on both sides
    for i, tu in enumerate(turns):
        if tu['label'] != 'T' or i in protected:
            continue
        if boundary_ok(i - 1, i - 1, i):
            tail_shred(i - 1, rng.choice([4, 5, 6, 7, 8, 9]))
        if boundary_ok(i, i + 1, i):
            head_shred(i, rng.choice([3, 4, 5, 6, 7, 8]))
    # 1b. top up Tariq's label until the raw figure overstates the true one by T_TARGET of all words
    def t_gap():
        raw = sum(len(words(seg)) for tu in turns if tu['label'] == 'T' for o, seg, a in tu['segs'])
        true = sum(len(words(seg)) for tu in turns for o, seg, a in tu['segs'] if o == 'T')
        total = sum(len(words(seg)) for tu in turns for o, seg, a in tu['segs'])
        return raw - true, total
    for _ in range(60):
        gap, total = t_gap()
        if gap >= T_TARGET * total:
            break
        entries = [e for e in plan if e['under'] == 'T' and e['kind'] in ('head', 'tail')]
        rng.shuffle(entries)
        grown = False
        for e in entries:
            i = e['boundary']
            if e['kind'] == 'tail':
                donor, rec = turns[i], turns[i + 1]
                seg = donor['segs'][-1]
                toks = seg[1].split()
                if seg[0] != donor['label'] or len(toks) < 6 or not movable(toks[-2:]) or 'keep' in donor['flags'] or 'soft' in donor['flags']:
                    continue
                more = ' '.join(toks[-2:])
                seg[1] = (' ' if len(donor['segs']) > 1 else '') + ' '.join(toks[:-2])
                rec['segs'][0][1] = more + ' ' + rec['segs'][0][1]
                e['frag'] = more + ' ' + e['frag']
            else:
                rec, donor = turns[i], turns[i + 1]
                seg = donor['segs'][0]
                toks = seg[1].split()
                if seg[0] != donor['label'] or len(toks) < 6 or not movable(toks[:2]) or 'keep' in donor['flags'] or 'soft' in donor['flags']:
                    continue
                more = ' '.join(toks[:2])
                seg[1] = ' '.join(toks[2:]) + (' ' if len(donor['segs']) > 1 else '')
                rec['segs'][-1][1] = rec['segs'][-1][1] + ' ' + more
                e['frag'] = e['frag'] + ' ' + more
            e['k'] += 2
            grown = True
            break
        if not grown:
            break
    # 2. generic shreds; Tariq is never a donor; kinds chosen to keep the cross-side flows balanced
    order = list(range(len(turns) - 1))
    rng.shuffle(order)
    added = 0
    orph = 0
    for i in order:
        x, y = flows(turns, orphans)
        if added >= EXTRA_EVENTS and abs(x - y) <= 1:
            break
        if i in used_boundary or i >= len(turns) - 1:
            continue
        a, b = turns[i], turns[i + 1]
        if a['label'] == b['label']:
            continue
        opts = []
        if b['label'] != 'T' and boundary_ok(i, i + 1, i):
            opts.append('head')
        if a['label'] != 'T' and boundary_ok(i, i, i + 1):
            opts.append('tail')
        if not opts:
            continue
        cross = SIDE[a['label']] != SIDE[b['label']]
        if cross and abs(x - y) > 1:
            # head puts b's words under a's label; tail puts a's words under b's label
            want_x = y > x   # need more client words under own labels
            head_adds_x = SIDE[b['label']] == 'client'
            kind = 'head' if (want_x == head_adds_x) else 'tail'
            if kind not in opts:
                continue
            k = min(abs(x - y), rng.choice([2, 3, 4, 5, 6]))
        else:
            if added >= EXTRA_EVENTS:
                continue
            kind = rng.choice(opts)
            k = rng.choice([1, 1, 2, 2, 3, 4])
        orphan = kind == 'head' and orph < ORPHANS and k <= 3 and rng.random() < 0.5
        done = head_shred(i, k, orphan) if kind == 'head' else tail_shred(i, k)
        if done:
            added += 1
            if orphan:
                orph += 1
    # 3. final balance: bring the cross-side flows within one word of each other
    for _ in range(40):
        x, y = flows(turns, orphans)
        if abs(x - y) <= 1:
            break
        want_x = y > x
        done = False
        rng.shuffle(order)
        for i in order:
            if i in used_boundary or i >= len(turns) - 1:
                continue
            a, b = turns[i], turns[i + 1]
            if a['label'] == b['label'] or SIDE[a['label']] == SIDE[b['label']]:
                continue
            head_adds_x = SIDE[b['label']] == 'client'
            kind = 'head' if (want_x == head_adds_x) else 'tail'
            k = min(abs(x - y), rng.choice([2, 3, 4, 5]))
            if kind == 'head' and b['label'] != 'T' and boundary_ok(i, i + 1, i):
                done = head_shred(i, k)
            elif kind == 'tail' and a['label'] != 'T' and boundary_ok(i, i, i + 1):
                done = tail_shred(i, k)
            if done:
                break
        if not done:
            break
    # 3b. if donors ran out, give words back from the heavier flow's fragments (never Tariq's)
    for _ in range(60):
        x, y = flows(turns, orphans)
        if abs(x - y) <= 1:
            break
        heavy_own = y > x
        entries = [e for e in plan if e['kind'] in ('head', 'tail') and e['under'] != 'T'
                   and SIDE[e['owner']] != SIDE[e['under']]
                   and (SIDE[e['owner']] == 'own') == heavy_own and len(e['frag'].split()) >= 2]
        if not entries:
            break
        e = rng.choice(entries)
        i = e['boundary']
        if e['kind'] == 'head':
            rec, donor = turns[i], turns[i + 1]
            frag_seg = rec['segs'][-1]
            toks = frag_seg[1].split()
            back = toks[-1]
            frag_seg[1] = ' ' + ' '.join(toks[:-1])
            donor['segs'][0][1] = back + ' ' + donor['segs'][0][1].lstrip()
        else:
            donor, rec = turns[i], turns[i + 1]
            frag_seg = rec['segs'][0]
            toks = frag_seg[1].split()
            back = toks[0]
            frag_seg[1] = ' '.join(toks[1:]) + ' '
            donor['segs'][-1][1] = donor['segs'][-1][1].rstrip() + ' ' + back
        e['frag'] = ' '.join(e['frag'].split()[1:]) if e['kind'] == 'tail' else ' '.join(e['frag'].split()[:-1])
        e['k'] -= 1
    for i, new in sorted(orphans, key=lambda o: -o[0]):
        turns.insert(i + 1, new)
    return plan, protected


def same_label_splits(turns, protected, rng):
    cands = [i for i, tu in enumerate(turns)
             if i not in protected and plain(tu) and 'assent' not in tu['flags'] and 'keep' not in tu['flags'] and 'soft' not in tu['flags']
             and 22 <= len(words(text_of(tu))) <= 100]
    rng.shuffle(cands)
    splits = []
    for i in cands[:SAME_LABEL_SPLITS]:
        tu = turns[i]
        toks = tu['segs'][0][1].split()
        mid = len(toks) // 2
        # split after the comma closest to the middle, or after 'and'
        best = None
        for j in range(4, len(toks) - 4):
            if toks[j].endswith(',') or toks[j].endswith('.'):
                if best is None or abs(j - mid) < abs(best - mid):
                    best = j
        if best is None:
            continue
        first = ' '.join(toks[:best + 1])
        second = ' '.join(toks[best + 1:])
        tu['segs'][0][1] = first
        splits.append((i, {'label': tu['label'], 'segs': [[tu['label'], second, False]], 'pause': 0.0,
                           'hand': False, 'flags': {'split'}}))
    for i, new in sorted(splits, key=lambda x: -x[0]):
        turns.insert(i + 1, new)
    return len(splits)


def hms(s):
    s = int(round(s))
    return '%02d:%02d:%02d' % (s // 3600, (s % 3600) // 60, s % 60)


def main():
    rng = random.Random(SEED)
    turns, duet = parse(os.path.join(HERE, 'source.txt'))
    for i in range(duet[1], duet[2]):
        turns[i]['flags'].add('duet')
    for i in (duet[1] - 1, duet[2]):
        turns[i]['flags'].add('duet-edge')
    plan, protected = auto_shred(turns, duet, rng)
    protected = set(i for i, tu in enumerate(turns) if 'duet' in tu['flags'] or 'duet-edge' in tu['flags'] or 'orphan' in tu['flags'])
    nsplit = same_label_splits(turns, protected, rng)
    for tu in turns:
        tu['text'] = text_of(tu)
    duet_idx = [i for i, tu in enumerate(turns) if 'duet' in tu['flags']]
    t = 3.0
    last_start = -1
    for i, tu in enumerate(turns):
        t += tu['pause']
        start = int(round(t))
        if start <= last_start:
            start = last_start + 1
        tu['start'] = start
        tu['line'] = i + 1
        n = len(words(tu['text']))
        tu['words'] = n
        t = start + n / PACE + GAP
        last_start = start
    out = ['%s %s: %s' % (hms(tu['start']), NAMES[tu['label']], tu['text']) for tu in turns]
    with open(os.path.join(FIX, 'transcript.txt'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(out) + '\n')
    raw = {k: 0 for k in NAMES}
    true = {k: 0 for k in NAMES}
    repaired = {k: 0 for k in NAMES}
    unresolved = 0
    shreds = []
    assents = []
    for tu in turns:
        for owner, seg, assent in tu['segs']:
            n = len(words(seg))
            raw[tu['label']] += n
            true[owner] += n
            if assent:
                unresolved += n
                assents.append({'line': tu['line'], 'time': hms(tu['start']), 'label': NAMES[tu['label']],
                                'likely_owner': NAMES[owner], 'text': seg.strip(), 'words': n,
                                'position': 'end' if tu['text'].endswith(seg.strip()) else 'mid',
                                'host_turn_words': tu['words']})
            else:
                repaired[owner] += n
            if owner != tu['label']:
                pos = 'head' if tu['text'].startswith(seg.strip()) else ('tail' if tu['text'].endswith(seg.strip()) else 'interior')
                shreds.append({'line': tu['line'], 'time': hms(tu['start']), 'label': tu['label'], 'owner': owner,
                               'words': n, 'text': seg.strip(), 'position': pos, 'assent': assent,
                               'direction': 'cross-side' if SIDE[owner] != SIDE[tu['label']] else 'within-side'})
    def side(d):
        c = sum(v for k, v in d.items() if SIDE[k] == 'client')
        return c, sum(d.values())
    rc, rt = side(raw)
    tc, tt = side(true)
    pc, pt = side(repaired)
    fmt = lambda d, tot: {NAMES[k]: round(100.0 * d[k] / tot, 2) for k in NAMES}
    stats = {
        'turns': len(turns), 'words': sum(raw.values()), 'same_label_splits_applied': nsplit,
        'auto_shred_events': len(plan),
        'raw_by_label': raw, 'true_by_owner': true, 'repaired_by_owner': repaired,
        'unresolved_words': unresolved,
        'client_share_raw': round(100.0 * rc / rt, 2),
        'client_share_true': round(100.0 * tc / tt, 2),
        'client_share_repaired': round(100.0 * pc / pt, 2),
        'per_speaker_share_raw': fmt(raw, rt),
        'per_speaker_share_true': fmt(true, tt),
        'per_speaker_share_repaired': fmt(repaired, pt),
        'cross_side_client_words_under_own_label': sum(s['words'] for s in shreds if s['direction'] == 'cross-side' and SIDE[s['owner']] == 'client'),
        'cross_side_own_words_under_client_label': sum(s['words'] for s in shreds if s['direction'] == 'cross-side' and SIDE[s['owner']] == 'own'),
        'within_side_words': sum(s['words'] for s in shreds if s['direction'] == 'within-side'),
        'shred_events': len(shreds),
        'turns_carrying_foreign_words': len(set(s['line'] for s in shreds)),
        'one_word_turns': sum(1 for tu in turns if tu['words'] == 1),
        'turns_at_or_under_four_words': sum(1 for tu in turns if tu['words'] <= 4),
        'lowercase_initial_turns': sum(1 for tu in turns if tu['text'][:1].islower()),
        'turns_without_terminal_punctuation': sum(1 for tu in turns if tu['text'].rstrip()[-1:] not in '.?!'),
        'adjacent_same_label_pairs': sum(1 for a, b in zip(turns, turns[1:]) if a['label'] == b['label']),
        'max_unit_words': max(tu['words'] for tu in turns),
        'max_unit_line': max(turns, key=lambda tu: tu['words'])['line'],
        'first_time': hms(turns[0]['start']), 'last_time': hms(turns[-1]['start']),
        'span_seconds': round(turns[-1]['start'] + turns[-1]['words'] / PACE - turns[0]['start'], 1),
        'assents': assents,
        'long_turns_over_100_words': [(tu['line'], hms(tu['start']), NAMES[tu['label']], tu['words']) for tu in turns if tu['words'] > 100],
        'turns_per_speaker': {NAMES[k]: sum(1 for tu in turns if tu['label'] == k) for k in NAMES},
    }
    d = [turns[i] for i in duet_idx]
    labels = [x['label'] for x in d]
    after = turns[duet_idx[-1] + 1]
    before = turns[duet_idx[0] - 1]
    stats['duet'] = {
        'first_line': d[0]['line'], 'last_line': d[-1]['line'],
        'first_time': hms(d[0]['start']), 'last_time': hms(d[-1]['start']),
        'turns': len(d), 'consultant_turns': labels.count('C'), 'maren_turns': labels.count('M'),
        'alternates': all(a != b for a, b in zip(labels, labels[1:])),
        'client_words_inside': sum(len(words(seg)) for x in d for o, seg, a in x['segs'] if SIDE[o] == 'client'),
        'words': sum(x['words'] for x in d),
        'seconds': after['start'] - d[0]['start'],
        'last_client_turn_before': [before['line'], hms(before['start']), NAMES[before['label']]],
        'next_client_turn_after': [after['line'], hms(after['start']), NAMES[after['label']]],
    }
    with open(os.path.join(HERE, 'stats.json'), 'w') as f:
        json.dump(stats, f, indent=1)
    with open(os.path.join(HERE, 'plan.json'), 'w') as f:
        json.dump({'seed': SEED, 'plan': plan}, f, indent=1)
    with open(os.path.join(HERE, 'truth.tsv'), 'w', encoding='utf-8') as f:
        f.write('line\ttime\tlabel\tsegments (owner: text)\n')
        for tu in turns:
            f.write('%d\t%s\t%s\t%s\n' % (tu['line'], hms(tu['start']), NAMES[tu['label']],
                    ' || '.join('%s%s: %s' % (NAMES[o], ' [assent]' if a else '', s.strip()) for o, s, a in tu['segs'])))
    with open(os.path.join(HERE, 'shreds.json'), 'w') as f:
        json.dump(shreds, f, indent=1)
    keep = {k: v for k, v in stats.items() if k != 'assents'}
    print(json.dumps(keep, indent=1))


if __name__ == '__main__':
    main()
