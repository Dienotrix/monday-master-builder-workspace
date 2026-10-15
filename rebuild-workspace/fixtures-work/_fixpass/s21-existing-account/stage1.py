import json, sys
sys.path.insert(0, '.')
from render import dump
P = '/Users/caramelm4/DelOps/rebuild-workspace/fixtures/s21-existing-account/answer-key.json'
k = json.load(open(P, encoding='utf-8'))

def rep(s, old, new):
    assert s.count(old) == 1, (s.count(old), old[:80])
    return s.replace(old, new)

APPROVAL = "archive proposed; Idris accepts; Henrietta's approval still required before anything changes"

# ---- FEEDBACK item 1: the costing delta joins requested_changes, first, as the main build
k['requested_changes'].insert(0, {
    "type": "change",
    "description": "The costing delta, the main build: keep Bethan's form and her cells as subitems; get the cell total onto the parent so the Studies board can read it through a connection (the drift at 00:18:20, where the summary moves and the parent does not, is the failure it fixes); unverified until tried on a copy (00:19:46); access to her workspace pending the client's IT (00:20:26). Plus the monthly per-agency costed-versus-actual view (00:17:34, 00:21:47), once the finance source for 'actual' is resolved. Chosen by Bethan from the two approaches offered at 00:19:16 and approved by Henrietta ('The costing piece, yes, today.', 00:35:53).",
    "quote": "Either of those would do it, honestly. The first one. I don't want to lose the form."
})

# ---- FEEDBACK item 2: the rota archive has no approval from Henrietta
rc = k['requested_changes']
rm = [e for e in rc if e['type'] == 'remove'][0]
rm['description'] = rep(rm['description'], ", with Henrietta's yes since it is a live object of ours.",
    ". Approval state: " + APPROVAL + ", since it is a live object of ours in the client's account.")
r12 = [r for r in k['rubric'] if r['criterion'].startswith('R12')][0]
r12['note'] = rep(r12['note'], "The label self-service ask and the rota archive were agreed as changes to live objects with Henrietta's yes.",
    "The label self-service ask was agreed as a change to a live object with Henrietta's yes; the rota archive was proposed by the Consultant and accepted by Idris, and Henrietta's approval is still required before anything changes.")
arc = [c for c in k['commitments_and_next_steps'] if c['what'].startswith('Archive the dead rota board')][0]
arc['what'] = "Archive the dead rota board (never delete). Approval state: " + APPROVAL
arc['owner'] = "Consultant, at the approval stop, after Henrietta's yes"
pa = k['intake']['prior_attempts'][0]
pa['disposition'] = rep(pa['disposition'], "archive with Henrietta's yes;", APPROVAL + ";")
lt = k['expected_structures']['lookalike_traps']
lt[2] = rep(lt[2], "the dead board is archived with Henrietta's yes, and",
    "the dead board is archived only once Henrietta approves (" + APPROVAL + "), and")
tr = k['traps']
i = [n for n, t in enumerate(tr) if t.startswith('The dead rota board is archived, never deleted')][0]
tr[i] = tr[i] + " The archive itself was proposed by the Consultant and accepted by Idris; Henrietta's approval is still required before anything changes."
emp = k['expected_monday_products'][0]
emp['why'] = rep(emp['why'], "and the dead rota board is archived.",
    "and the dead rota board is archived once Henrietta approves (proposed on the call; Idris accepts; her approval still required).")
k['purpose_of_this_fixture'] = rep(k['purpose_of_this_fixture'], "the dead rota board archived and never deleted.",
    "the dead rota board archived once Henrietta approves (proposed on the call; Idris accepts) and never deleted.")

# ---- FEEDBACK item 3: the booking link is committed, not delivered
k['purpose_of_this_fixture'] = rep(k['purpose_of_this_fixture'],
    "grades R10 Met on a booking mechanism delivered on the call with a named owner, a stated purpose and the client's assent",
    "grades R10 Met on a booking mechanism committed on the call (evidence state: the booking link is committed to send today, owner the Consultant, purpose a 45-minute working session walking the costing board cell by cell on a copy; it is not sent, and becomes done only on evidence) with a named owner, a stated purpose and the client's assent")
r10 = [r for r in k['rubric'] if r['criterion'].startswith('R10')][0]
r10['note'] = rep(r10['note'], "the Consultant delivers the mechanism on the call (a booking link sent today), names the owners",
    "the Consultant commits to the mechanism on the call (evidence state: a booking link committed to send today; owner the Consultant; purpose the 45-minute working session on a copy of the costing board; done only on evidence it was sent), names the owners")
bl = k['commitments_and_next_steps'][0]
assert bl['what'].startswith('Booking link')
bl['what'] = rep(bl['what'], "(the next step, R10)", "(the next step, R10); state: committed to send today, owner the Consultant, purpose the working session; done only on evidence it was sent")
bl['date'] = rep(bl['date'], "Link sent on the day of the call (date not stated)", "Committed: the link is to be sent on the day of the call (date not stated), not yet sent")
ns = k['intake']['next_step']
ns['state'] = "booking mechanism committed on the call: the link is committed to send today, owner the Consultant, purpose the working session; not sent, done only on evidence"
ns['mechanism'] = "a booking link, committed to send today, for a 45-minute working session"

# ---- direction rename (direction_of_show -> direction; its note follows)
th = k['intake']['type_header']
new = {}
for key, val in th.items():
    nk = {'direction_of_show': 'direction', 'direction_of_show_note': 'direction_note'}.get(key, key)
    if key == 'segments':
        val = [{('direction' if a == 'direction_of_show' else a): b for a, b in seg.items()} for seg in val]
    new[nk] = val
k['intake']['type_header'] = new
assert 'direction_of_show' not in json.dumps(k)

dump(k, P)
print('stage 1 written; requested_changes', len(k['requested_changes']), '| header keys:', list(new)[:12])
