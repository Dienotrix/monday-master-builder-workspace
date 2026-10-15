#!/usr/bin/env python3
"""verify_quotes.py - quote-at-location verifier for the monday Master Builder fixtures.

Usage
    python3 verify_quotes.py <fixture folder> [--json] [--spans]

What it does
    Loads <folder>/answer-key.json and walks the whole JSON tree. A pair is a string value
    under a key whose name carries the word "quote" (quote, quotes, quote_or_null,
    evidence_quote_or_null, asked_quote, type_quote, requote, requotes ...; lists of quotes
    included), together with the nearest location in the same object: a sibling named
    location, locations, at, cue, cues, line, lines, where or source, or a location embedded
    at the end of the quote's own string.

    The location is read in the fixture's own grammar (see LOCATION GRAMMARS below), the
    cited unit (or merged run) is found in the fixture's own files, and the quote must appear
    in it verbatim after normalising whitespace, straight and curly quotes, and the
    three-dot and single-character ellipsis.

Statuses
    verified        the quote is in the cited unit or merged run
    near-miss       the quote differs from the cited text only by punctuation or case
    miss            the quote is not at the cited location (the report says where it is found
                    instead, if anywhere, and the nearest text if not); also a location that
                    does not exist
    skipped         the value is null or empty, or is a pointer (a location with no quote)
    unparsed prose  a string that holds several quotes with their own locations, or that
                    describes a quote instead of being one; reported, not failed
    unsupported     a form this script cannot read here (an image, a PDF it cannot decode)

    A quote with no location at all (for example numbers.bleed.quote, account_context
    .evidence_quote_or_null) cannot be checked at a location. It is checked for presence in
    the fixture's files and counted as verified ("presence only") or as a miss ("not in any
    file"). The report keeps the two apart.

Location grammars (read from the fixtures' own files and READMEs)
    WebVTT / SRT cues     cue 78 | cue 78, 00:05:45.889, Name | cues 82-85 (merged run)
    timestamp-first       @00:21:14 | 00:21:14 Name | 31:16 | 13:58 Name | [03:02] Name
    line numbers          L142 | L142-144 | line 112 | lines 112-114 (physical lines of the file)
    turns                 turn 31, 03:43, Name (the Nth header line)
    paragraphs            paragraph 75 (the Nth blank-line separated block)
    several files         call 2, 00:08:40 Name | rec-4402 07:26 | rec-4418, line 112 | chat 14:26:40 Name
    documents (s25)       QP-07 section 3.2 | QP-07 front page | write-up p.1 section 2, W-2
                          (.docx read through zipfile and word/document.xml; the write-up PDF
                          read from its text-showing operators when they are plain or Flate);
                          figure 1 p.1 (an image) is reported as unsupported.
    Roles in parentheses and the words "inferred", "labelled", "segment N" and "(side-only)"
    are ignored; the timestamp and the speaker label are matched, the role is not.
    Where a location names an index (cue, turn, paragraph, L-number) the index picks the unit
    and a disagreeing stamp or label is a "location note", not a miss. Where it names only a
    stamp and a label, those pick the unit (any unit sharing both counts). A location that
    names a composite-block segment ("segment 3") is also checked against the segment's start
    and end text in intake.composite_blocks, where the key gives them.
    Other forms accepted: a quote offered with a list of locations (verified when any holds);
    a quote list beside a locations list (paired by position); a location at the end of the
    quote's own string ("... (L142)", "... [00:21:14 Name]", "... @00:21:14", "... -- L142, Name").
    The key's own refusals (refused_quotes) document spans the key will not cite and are not
    checked. Keys that describe a quote instead of holding one (figure_as_requoted,
    contrast_with_the_wrong_requote) are reported as unparsed prose.

Options
    --json    emit the full report as JSON instead of the readable report
    --spans   print, per transcript unit, the quoted spans the key protects (the text an
              editor must not change)

Exit status
    0  every pair is verified (unparsed prose, unsupported forms and skipped values do not fail)
    1  at least one miss or near-miss remains
    3  the folder or the key cannot be read

Standard library only, Python 3.9 and later.
"""

import argparse
import difflib
import json
import os
import re
import sys
import zipfile
import zlib
from collections import OrderedDict

# --------------------------------------------------------------------------------------
# Normalisation
# --------------------------------------------------------------------------------------

_QUOTE_MAP = {
    "‘": "'", "’": "'", "‚": "'", "‛": "'", "′": "'", "ʼ": "'",
    "“": '"', "”": '"', "„": '"', "‟": '"', "″": '"',
}


def norm_map(s):
    """Normalise s; return (normalised string, list mapping each output char to an index of s)."""
    out = []
    mp = []
    prev_space = True  # swallow leading whitespace
    for i, ch in enumerate(s):
        ch = _QUOTE_MAP.get(ch, ch)
        if ch == "…":
            out.extend("...")
            mp.extend([i, i, i])
            prev_space = False
            continue
        if ch.isspace() or ch == " ":
            if not prev_space:
                out.append(" ")
                mp.append(i)
            prev_space = True
            continue
        out.append(ch)
        mp.append(i)
        prev_space = False
    if out and out[-1] == " ":
        out.pop()
        mp.pop()
    return "".join(out), mp


def norm(s):
    return norm_map(s)[0]


def loose(s):
    """Punctuation- and case-insensitive form, used only to detect near-misses."""
    s = norm(s).lower()
    s = s.replace("'", "")
    s = re.sub(r"[^\w\s]|_", " ", s)
    return re.sub(r"\s+", " ", s).strip()


# --------------------------------------------------------------------------------------
# Sources and units
# --------------------------------------------------------------------------------------

TS = r"\d{1,2}:\d{2}(?::\d{2})?(?:[.,]\d{1,3})?"


def to_secs(ts):
    ts = re.split(r"[.,]", ts)[0]
    p = [int(x) for x in ts.split(":")]
    if len(p) == 3:
        return p[0] * 3600 + p[1] * 60 + p[2]
    return p[0] * 60 + p[1]


class Unit(object):
    def __init__(self, src, n, line, end_line, time, speaker, text, cue=None, parts=None, label=None):
        self.src = src
        self.n = n                  # ordinal in the file, 1-based (turn / paragraph number)
        self.line = line            # first physical line, 1-based
        self.end_line = end_line
        self.time = time
        self.secs = to_secs(time) if time else None
        self.speaker = speaker
        self.text = text
        self.cue = cue
        self.parts = parts          # for documents: the paragraphs a quote must sit inside
        self.label = label          # for documents: section id, page, W id ...

    def describe(self):
        bits = [self.src.short]
        if self.cue is not None:
            bits.append("cue %s" % self.cue)
        if self.src.kind in ("transcript", "chat", "context") and self.line:
            bits.append("L%s" % self.line)
        if self.src.fmt in ("header-time-last", "header-time-first", "header-bracket", "header-dot", "paragraph"):
            bits.append("%s %s" % ("paragraph" if self.src.fmt == "paragraph" else "turn", self.n))
        if self.time:
            bits.append(self.time)
        if self.speaker:
            bits.append(self.speaker)
        if self.label:
            bits.append(self.label)
        return ", ".join(str(b) for b in bits)


class Source(object):
    def __init__(self, path, kind, fmt=None):
        self.path = path
        self.name = os.path.basename(path)
        self.kind = kind            # transcript, chat, docx, pdf, image, context, other
        self.fmt = fmt
        self.units = []
        self.unsupported = None     # reason, when the form cannot be read here
        self.call_no = None
        self.rec_id = None
        m = re.search(r"transcript-(\d+)", self.name)
        if m:
            self.call_no = int(m.group(1))
        m = re.search(r"rec-(\d+)", self.name)
        if m:
            self.rec_id = m.group(1)
        self.short = self.name

    def __repr__(self):
        return "<Source %s %s %s units=%d>" % (self.name, self.kind, self.fmt, len(self.units))


# line-oriented formats: (name, regex, groups order)
_LINE_FORMATS = [
    ("line-bracket", re.compile(r"^\[(" + TS + r")\]\s+([^:\[\]]{1,60}?):\s*(.*)$"), ("time", "speaker", "text")),
    ("line-time-first", re.compile(r"^(" + TS + r")\s+([^:\[\]]{1,60}?):\s+(.*)$"), ("time", "speaker", "text")),
    ("line-time-last", re.compile(r"^([^:\[\]()]{1,60}?)\s+\((" + TS + r")\):\s*(.*)$"), ("speaker", "time", "text")),
    ("line-plain", re.compile(r"^([A-Z][A-Za-z.'\-]*(?: [A-Za-z.'\-]+){0,3}):\s+(.*)$"), ("speaker", "text")),
]
_HEADER_FORMATS = [
    ("header-bracket", re.compile(r"^\[(" + TS + r")\]\s+(\S.{0,60}?)\s*$"), ("time", "speaker")),
    ("header-time-last", re.compile(r"^([A-Za-z][^:\[\]·]{0,60}?)\s{1,}(" + TS + r")\s*$"), ("speaker", "time")),
    ("header-dot", re.compile(r"^(\S.{0,60}?)\s+·\s+(" + TS + r")\s*$"), ("speaker", "time")),
    ("header-time-first", re.compile(r"^(" + TS + r")\s{2,}(\S.{0,60}?)\s*$"), ("time", "speaker")),
]


def read_text(path):
    with open(path, "rb") as fh:
        raw = fh.read()
    for enc in ("utf-8-sig", "latin-1"):
        try:
            return raw.decode(enc)
        except UnicodeDecodeError:
            continue
    return raw.decode("utf-8", "replace")


def parse_cues(lines, src):
    """WebVTT or SRT. Cue number = the numeric id line when present, else the running count."""
    units = []
    i = 0
    n = len(lines)
    running = 0
    while i < n:
        if not lines[i].strip():
            i += 1
            continue
        block_start = i
        block = []
        while i < n and lines[i].strip():
            block.append((i + 1, lines[i]))
            i += 1
        # find the timing line
        ti = None
        for k, (ln, txt) in enumerate(block):
            if "-->" in txt:
                ti = k
                break
        if ti is None:
            continue
        cue_id = None
        if ti >= 1 and re.match(r"^\s*\d+\s*$", block[ti - 1][1]):
            cue_id = int(block[ti - 1][1])
        running += 1
        if cue_id is None:
            cue_id = running
        m = re.match(r"\s*(\d{1,2}:\d{2}:\d{2}[.,]\d{1,3}|\d{1,2}:\d{2}[.,]\d{1,3})\s*-->", block[ti][1])
        start = m.group(1) if m else None
        payload = " ".join(t.strip() for _, t in block[ti + 1:])
        speaker = None
        mv = re.match(r"^<v\s+([^>]+)>(.*)$", payload)
        if mv:
            speaker = mv.group(1).strip()
            payload = re.sub(r"</v>", "", mv.group(2)).strip()
        else:
            ms = re.match(r"^([A-Za-z][^:]{0,40}?):\s+(.*)$", payload)
            if ms:
                speaker = ms.group(1).strip()
                payload = ms.group(2)
        first_line = block[ti + 1][0] if len(block) > ti + 1 else block[ti][0]
        units.append(Unit(src, len(units) + 1, block[ti][0] if cue_id is not None else first_line,
                          block[-1][0], start, speaker, payload, cue=cue_id))
        # for L-citations a cue's lines run from its id line to its last payload line
        units[-1].line = block[0][0]
    return units


def parse_transcript(path, src):
    text = read_text(path)
    lines = text.split("\n")
    lines = [l.rstrip("\r") for l in lines]
    nonblank = [l for l in lines if l.strip()]
    first = next((l.strip() for l in lines if l.strip()), "")
    if first.startswith("WEBVTT"):
        src.fmt = "vtt"
        return parse_cues(lines, src)
    if re.match(r"^\d+$", first):
        idx = next(i for i, l in enumerate(lines) if l.strip())
        if idx + 1 < len(lines) and "-->" in lines[idx + 1]:
            src.fmt = "srt"
            return parse_cues(lines, src)

    # score the line formats and the header formats
    scores = OrderedDict()
    for name, rx, _ in _LINE_FORMATS:
        scores[name] = sum(1 for l in lines if rx.match(l))
    for name, rx, _ in _HEADER_FORMATS:
        c = 0
        for i, l in enumerate(lines[:-1]):
            if rx.match(l) and lines[i + 1].strip() and not rx.match(lines[i + 1]):
                c += 1
        scores[name] = c
    best = max(scores, key=lambda k: scores[k])
    if scores[best] >= max(5, len(nonblank) // 40):
        # prefer header-time-first for chat-like files named for chat
        src.fmt = best
        if best.startswith("line-"):
            return parse_lines(lines, src, best)
        return parse_headers(lines, src, best)
    src.fmt = "paragraph"
    return parse_paragraphs(lines, src)


def _groups(order, m):
    d = {}
    for k, g in zip(order, m.groups()):
        d[k] = g
    return d


def parse_lines(lines, src, fmt):
    rx, order = next((rx, o) for nm, rx, o in _LINE_FORMATS if nm == fmt)
    units = []
    for i, l in enumerate(lines):
        m = rx.match(l)
        if m:
            g = _groups(order, m)
            units.append(Unit(src, len(units) + 1, i + 1, i + 1, g.get("time"), g["speaker"].strip(), g["text"]))
        elif units and l.strip() and not re.match(r"^[─-╿=\-_\s]+$", l):
            u = units[-1]
            # a continuation line directly under a unit (no blank line between)
            if u.end_line == i:
                u.text += " " + l.strip()
                u.end_line = i + 1
    return units


def parse_headers(lines, src, fmt):
    rx, order = next((rx, o) for nm, rx, o in _HEADER_FORMATS if nm == fmt)
    units = []
    i = 0
    n = len(lines)
    while i < n:
        m = rx.match(lines[i])
        if m and i + 1 < n and lines[i + 1].strip() and not rx.match(lines[i + 1]):
            g = _groups(order, m)
            j = i + 1
            body = []
            while j < n and lines[j].strip() and not (rx.match(lines[j]) and j + 1 < n and lines[j + 1].strip()):
                if re.match(r"^[─-╿=]{3,}", lines[j]):
                    break
                body.append(lines[j].strip())
                j += 1
            units.append(Unit(src, len(units) + 1, i + 1, j, g.get("time"), g["speaker"].strip(), " ".join(body)))
            i = j
        else:
            i += 1
    return units


def parse_paragraphs(lines, src):
    units = []
    i = 0
    n = len(lines)
    while i < n:
        if not lines[i].strip():
            i += 1
            continue
        start = i
        block = []
        while i < n and lines[i].strip():
            block.append(lines[i].strip())
            i += 1
        text = " ".join(block)
        time = None
        m = re.match(r"^\[(" + TS + r")\]\s*(.*)$", text)
        if m:
            time = m.group(1)
            text = m.group(2)
        units.append(Unit(src, len(units) + 1, start + 1, i, time, None, text))
    return units


# ---- documents --------------------------------------------------------------------

def parse_docx(path, src):
    try:
        z = zipfile.ZipFile(path)
        xml = z.read("word/document.xml").decode("utf-8")
    except Exception as e:  # noqa
        src.unsupported = "cannot read word/document.xml (%s)" % e
        return []
    paras = []
    for p in re.findall(r"<w:p[ >].*?</w:p>", xml, flags=re.S):
        t = "".join(re.findall(r"<w:t[^>]*>(.*?)</w:t>", p, flags=re.S))
        t = (t.replace("&amp;", "&").replace("&lt;", "<").replace("&gt;", ">")
             .replace("&quot;", '"').replace("&apos;", "'"))
        style = re.findall(r'<w:pStyle w:val="([^"]+)"', p)
        paras.append((style[0] if style else "", t))
    units = []
    cur = None
    front = Unit(src, 0, 0, 0, None, None, "", parts=[], label="front page")
    front.label = "front page"
    units.append(front)
    cur = front
    for style, t in paras:
        if style in ("Heading1", "Heading2"):
            m = re.match(r"^(\d+(?:\.\d+)*)\.?\s", t)
            if m:
                label = "section " + m.group(1)
            elif t.strip().lower().startswith("revision history"):
                label = "revision history"
            else:
                label = "heading " + t.strip()
            cur = Unit(src, len(units), 0, 0, None, None, "", parts=[], label=label)
            cur.parts.append(t)   # the heading itself is part of the unit
            units.append(cur)
            continue
        cur.parts.append(t)
    for u in units:
        u.text = " ".join(u.parts)
    # a Heading1 section also owns its Heading2 children: "section 3" covers 3.1 .. 3.5
    return units


def _pdf_unescape(b):
    out = bytearray()
    i = 0
    while i < len(b):
        c = b[i]
        if c == 0x5C and i + 1 < len(b):
            d = b[i + 1]
            mp = {ord("n"): 10, ord("r"): 13, ord("t"): 9, ord("b"): 8, ord("f"): 12,
                  ord("("): 40, ord(")"): 41, 0x5C: 0x5C}
            if d in mp:
                out.append(mp[d])
                i += 2
                continue
            m = re.match(rb"[0-7]{1,3}", b[i + 1:i + 4])
            if m:
                out.append(int(m.group(0), 8) & 0xFF)
                i += 1 + len(m.group(0))
                continue
            i += 1
            continue
        out.append(c)
        i += 1
    return bytes(out).decode("cp1252", "replace")


def parse_pdf(path, src):
    with open(path, "rb") as fh:
        raw = fh.read()
    # page order from the /Kids array when readable, else stream order
    streams = []
    for m in re.finditer(rb"(\d+) 0 obj(.*?)endobj", raw, re.S):
        body = m.group(2)
        sm = re.search(rb"stream\r?\n(.*?)\r?\nendstream", body, re.S)
        if not sm:
            continue
        data = sm.group(1)
        if b"/FlateDecode" in body[:sm.start()]:
            try:
                data = zlib.decompress(data)
            except Exception:  # noqa
                src.unsupported = "a Flate stream could not be decoded here"
                return []
        streams.append((int(m.group(1)), data))
    pages = []
    for num, data in streams:
        if b"Tj" not in data and b"TJ" not in data:
            continue
        lines = []
        cur = None
        for tm in re.finditer(rb"/(F\d+)\s+(\d+(?:\.\d+)?)\s+Tf|\((?:\\.|[^\\)])*\)\s*Tj|\[(.*?)\]\s*TJ|ET", data, re.S):
            tok = tm.group(0)
            if tok.endswith(b"Tj"):
                s = _pdf_unescape(re.match(rb"\((.*)\)\s*Tj$", tok, re.S).group(1))
                lines.append((cur, s))
            elif tok.endswith(b"TJ"):
                parts = re.findall(rb"\(((?:\\.|[^\\)])*)\)", tm.group(3))
                lines.append((cur, "".join(_pdf_unescape(p) for p in parts)))
            elif tm.group(1):
                cur = (tm.group(1).decode(), float(tm.group(2)))
        if lines:
            pages.append(lines)
    if not pages:
        src.unsupported = "no text-showing operators found (scanned or encoded PDF)"
        return []
    units = []
    for pno, lines in enumerate(pages, 1):
        sec = 0
        cur = Unit(src, len(units) + 1, 0, 0, None, None, "", parts=[], label="p.%d section 0" % pno)
        cur.page = pno
        cur.section = 0
        units.append(cur)
        for style, s in lines:
            m = re.match(r"^(\d+)\.\s", s)
            if style and style[0] == "F2" and m and style[1] <= 14:
                sec = int(m.group(1))
                cur = Unit(src, len(units) + 1, 0, 0, None, None, "", parts=[s], label="p.%d section %d" % (pno, sec))
                cur.page = pno
                cur.section = sec
                units.append(cur)
                continue
            cur.parts.append(s)
    # the PDF's text lines are joined with a space, as a text extractor yields them
    for u in units:
        u.text = " ".join(u.parts)
        u.parts = [u.text]
        # W-items: a unit of their own, kept as additional index
        u.w_items = {}
        cur_w = None
        for p in re.split(r"(?=\bW-\d+\s)", u.text):
            m = re.match(r"^(W-\d+)\s+(.*)$", p)
            if m:
                u.w_items[m.group(1)] = p
    return units


def load_sources(folder):
    sources = []
    for name in sorted(os.listdir(folder)):
        path = os.path.join(folder, name)
        if not os.path.isfile(path) or name in ("answer-key.json", "README.md") or name.startswith("."):
            continue
        low = name.lower()
        if low.endswith(".txt"):
            if "chat" in low:
                src = Source(path, "chat")
            else:
                src = Source(path, "transcript")
            src.units = parse_transcript(path, src)
            if "chat" in low and src.fmt == "header-time-first":
                pass
            sources.append(src)
        elif low.endswith(".docx"):
            src = Source(path, "docx", "docx")
            src.units = parse_docx(path, src)
            sources.append(src)
        elif low.endswith(".pdf"):
            src = Source(path, "pdf", "pdf")
            src.units = parse_pdf(path, src)
            sources.append(src)
        elif low.endswith((".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg")):
            src = Source(path, "image", "image")
            src.unsupported = "image: not checkable here, skipped"
            sources.append(src)
        elif low.endswith((".md", ".vtt", ".srt")):
            src = Source(path, "context", "context")
            t = read_text(path).split("\n")
            for i, l in enumerate(t):
                if l.strip():
                    src.units.append(Unit(src, len(src.units) + 1, i + 1, i + 1, None, None, l.strip()))
            sources.append(src)
        else:
            src = Source(path, "other", "other")
            src.unsupported = "unknown file type"
            sources.append(src)
    return sources


# --------------------------------------------------------------------------------------
# Location grammar
# --------------------------------------------------------------------------------------

class Loc(object):
    def __init__(self, raw):
        self.raw = raw
        self.call = None
        self.rec = None
        self.chat = False
        self.cue = None             # (a, b)
        self.turn = None
        self.para = None
        self.lines = None           # (a, b)
        self.times = []             # list of seconds
        self.time_strs = []
        self.doc = None             # ('docx', label) | ('pdf', page, sec, w) | ('image',)
        self.merged = False
        self.recognised = False
        self.has_name = False

    def describe(self):
        return self.raw


_DASH = r"\s*[-–—]\s*"


def parse_loc(s):
    loc = Loc(s)
    t = s
    m = re.search(r"\bQP-07\s+(front page|revision history|section\s+([\d.]+))", t, re.I)
    if m:
        loc.doc = ("docx", ("section " + m.group(2)) if m.group(2) else m.group(1).lower())
        loc.recognised = True
        return loc
    m = re.search(r"\bwrite-up\s+p\.(\d+)\s+section\s+(\d+)(?:\s*,\s*(W-\d+))?", t, re.I)
    if m:
        loc.doc = ("pdf", int(m.group(1)), int(m.group(2)), m.group(3))
        loc.recognised = True
        return loc
    m = re.search(r"\bfigure\s+\d+\s+p\.\d+", t, re.I)
    if m:
        loc.doc = ("image",)
        loc.recognised = True
        return loc
    m = re.search(r"\bcall\s+(\d+)", t, re.I)
    if m:
        loc.call = int(m.group(1))
        loc.recognised = True
    m = re.search(r"\brec-(\d+)", t, re.I)
    if m:
        loc.rec = m.group(1)
        loc.recognised = True
    if re.match(r"^\s*chat\b", t, re.I):
        loc.chat = True
        loc.recognised = True
    m = re.search(r"\bcues?\s+(\d+)(?:" + _DASH + r"(\d+))?", t, re.I)
    if m:
        a = int(m.group(1))
        b = int(m.group(2)) if m.group(2) else a
        loc.cue = (a, b)
        loc.recognised = True
    m = re.search(r"\bturn\s+(\d+)", t, re.I)
    if m:
        loc.turn = int(m.group(1))
        loc.recognised = True
    m = re.search(r"\bparagraph\s+(\d+)", t, re.I)
    if m:
        loc.para = int(m.group(1))
        loc.recognised = True
    m = re.search(r"(?<![\w])L(\d+)(?:" + _DASH + r"(\d+))?(?!\d)", t) or \
        re.search(r"\blines?\s+(\d+)(?:" + _DASH + r"(\d+))?", t, re.I)
    if m:
        a = int(m.group(1))
        b = int(m.group(2)) if m.group(2) else a
        loc.lines = (a, b)
        loc.recognised = True
    # times: strip the 'rec-4402' style tokens first so ids do not read as times
    tt = re.sub(r"rec-\d+", "", t)
    for tm in re.finditer(r"(?<![\d:.])(" + TS + r")(?![\d:])", tt):
        loc.time_strs.append(tm.group(1))
        loc.times.append(to_secs(tm.group(1)))
        loc.recognised = True
    if re.search(r"merged run", t, re.I):
        loc.merged = True
    rest = re.sub(r"\([^)]*\)|\bcalls?\b|\bcues?\b|\bturns?\b|\bparagraph\b|\blines?\b|\bchat\b|rec-\d+|\bL\d+|\d|"
                  r"[:.,\[\]@\-]|\bsegment\b|\blabelled\b|\binferred\b|\bblock\b|\bside-only\b|\band\b", "", t, flags=re.I)
    loc.has_name = re.search(r"[A-Za-z]{2,}", rest) is not None
    return loc


def speaker_in(loc_text, label):
    if not label:
        return True
    if len(label) == 1:
        return re.search(r"(?<![\w])" + re.escape(label) + r"(?![\w])", loc_text) is not None
    return re.search(r"(?<![\w])" + re.escape(label) + r"(?![\w])", loc_text, re.I) is not None


# --------------------------------------------------------------------------------------
# Resolving a location to units
# --------------------------------------------------------------------------------------

class Resolution(object):
    def __init__(self):
        self.candidates = []     # list of lists of units (a run), each a candidate cited text
        self.warnings = []
        self.error = None        # why nothing could be resolved
        self.unsupported = None  # reason, when the location points into a form not readable here


def candidate_sources(loc, sources):
    if loc.doc:
        kind = loc.doc[0]
        return [s for s in sources if s.kind == kind]
    if loc.chat:
        return [s for s in sources if s.kind == "chat"]
    pool = [s for s in sources if s.kind == "transcript"]
    if loc.rec:
        sel = [s for s in pool if s.rec_id == loc.rec]
        return sel
    if loc.call is not None:
        sel = [s for s in pool if s.call_no == loc.call]
        return sel
    return pool


def resolve(loc, sources):
    res = Resolution()
    pool = candidate_sources(loc, sources)
    if loc.doc:
        kind = loc.doc[0]
        if not pool:
            res.unsupported = "no %s source in the folder" % kind
            return res
        if kind == "image":
            res.unsupported = pool[0].unsupported or "image: not checkable here"
            return res
        for s in pool:
            if s.unsupported:
                res.unsupported = s.unsupported
                return res
            if kind == "docx":
                want = loc.doc[1]
                for u in s.units:
                    if u.label == want:
                        res.candidates.append([u])
                    elif want.startswith("section ") and u.label.startswith("section ") and \
                            u.label[8:].startswith(want[8:] + "."):
                        # a chapter number cites everything beneath it
                        res.candidates.append([u])
            else:
                _, page, sec, w = loc.doc
                for u in s.units:
                    if getattr(u, "page", None) == page and getattr(u, "section", None) == sec:
                        if w and w in u.w_items:
                            v = Unit(s, u.n, 0, 0, None, None, u.w_items[w], parts=[u.w_items[w]], label=u.label + ", " + w)
                            res.candidates.append([v])
                        elif w:
                            res.warnings.append("%s not found on %s; checking the whole section" % (w, u.label))
                            res.candidates.append([u])
                        else:
                            res.candidates.append([u])
        if not res.candidates:
            res.error = "no such unit in the document"
        return res
    if not pool:
        res.error = "no transcript for this location (call/recording/file not found)"
        return res

    for s in pool:
        units = s.units
        sel = None
        if loc.cue:
            if s.fmt not in ("vtt", "srt"):
                continue
            a, b = loc.cue
            sel = [u for u in units if u.cue is not None and a <= u.cue <= b]
        elif loc.turn is not None:
            sel = [u for u in units if u.n == loc.turn]
        elif loc.para is not None:
            sel = [u for u in units if u.n == loc.para]
        elif loc.lines:
            a, b = loc.lines
            if a == b:
                sel = [u for u in units if u.line <= a <= u.end_line]
            else:
                sel = [u for u in units if a <= u.line <= b]
                if not sel:
                    sel = [u for u in units if u.line <= a <= u.end_line]
        else:
            sel = None
        if sel is not None:
            if not sel:
                continue
            # location metadata agrees with the unit?
            if loc.times and any(u.secs is not None for u in sel):
                if loc.times[0] != sel[0].secs and not (len(sel) > 1 and loc.times[0] in [u.secs for u in sel]):
                    res.warnings.append("cited time %s but the unit at that index is %s (%s)" % (
                        loc.time_strs[0], sel[0].time, sel[0].describe()))
            if sel[0].speaker and loc.has_name and not loc.merged and not speaker_in(loc.raw, sel[0].speaker):
                if not re.search(r"speaker (not resolvable|unclear)", loc.raw) and "labelled" not in loc.raw:
                    res.warnings.append("cited speaker differs from the unit's label %r (%s)" % (
                        sel[0].speaker, sel[0].describe()))
            res.candidates.append(sel)
            continue
        # time-based
        if loc.times:
            hits = [u for u in units if u.secs is not None and u.secs in loc.times]
            named = [u for u in hits if speaker_in(loc.raw, u.speaker)] if any(u.speaker for u in hits) else hits
            if named:
                for u in named:
                    res.candidates.append([u])
            elif hits:
                if not re.search(r"speaker (not resolvable|unclear)|\bblock\b|\bsegment\b", loc.raw):
                    res.warnings.append("a unit at that time exists but under another label: %s" %
                                        "; ".join(u.describe() for u in hits[:3]))
                for u in hits:
                    res.candidates.append([u])
    if not res.candidates:
        if loc.cue and not any(s.fmt in ("vtt", "srt") for s in pool):
            res.error = "cue citation but the file has no cues"
        elif loc.cue or loc.turn is not None or loc.para is not None or loc.lines:
            res.error = "no unit at that index"
        elif loc.times:
            res.error = "no unit at that time"
        else:
            res.error = "location not understood"
    return res


# --------------------------------------------------------------------------------------
# Matching a quote against text
# --------------------------------------------------------------------------------------

def texts_of(run):
    """The cited texts of a candidate: one joined string for a run of transcript units, the
    separate paragraphs for a document unit."""
    if run[0].parts is not None:
        out = []
        for u in run:
            out.extend(u.parts if u.parts else [u.text])
        return out
    return [" ".join(u.text for u in run)]


def find_all(hay, needle):
    out = []
    start = 0
    while True:
        i = hay.find(needle, start)
        if i < 0:
            return out
        out.append(i)
        start = i + 1


def fragments(qn):
    """Split a quote at an elision ('...' with spaces or at an end) into its fragments."""
    parts = [p.strip() for p in re.split(r"\s*(?:\[\.\.\.\]|\.\.\.)\s*", qn)]
    return [p for p in parts if p]


def match_exact(texts, qn):
    """Return (kind, text_index, [(start, end)], norm_text, mp) for the first text holding qn."""
    for ti, t in enumerate(texts):
        tn, mp = norm_map(t)
        pos = find_all(tn, qn)
        if pos:
            return ("exact", ti, [(p, p + len(qn)) for p in pos], tn, mp)
    return None


def match_elided(texts, qn):
    frs = fragments(qn)
    if len(frs) < 2 and not (qn.startswith("...") or qn.endswith("...")):
        return None
    if not frs:
        return None
    for ti, t in enumerate(texts):
        tn, mp = norm_map(t)
        at = 0
        spans = []
        ok = True
        for f in frs:
            i = tn.find(f, at)
            if i < 0:
                ok = False
                break
            spans.append((i, i + len(f)))
            at = i + len(f)
        if ok:
            return ("elided", ti, spans, tn, mp)
    return None


def match_loose(texts, qn):
    lq = loose(qn)
    if not lq:
        return None
    for t in texts:
        if lq in loose(t):
            return ("near", t)
    return None


def diff_hint(qn, tn):
    sm = difflib.SequenceMatcher(None, qn, tn, autojunk=False)
    blocks = [b for b in sm.get_matching_blocks() if b.size >= 6]
    if not blocks:
        return None, None
    start = max(0, blocks[0].b - blocks[0].a)
    end = min(len(tn), blocks[-1].b + blocks[-1].size + (len(qn) - blocks[-1].a - blocks[-1].size) + 20)
    snippet = tn[start:end]
    ops = []
    sm2 = difflib.SequenceMatcher(None, qn, snippet, autojunk=False)
    for tag, i1, i2, j1, j2 in sm2.get_opcodes():
        if tag != "equal":
            ops.append("quote[%s] vs text[%s]" % (qn[i1:i2], snippet[j1:j2]))
    return snippet, ops[:4]


def _label_tokens(label):
    return set(t for t in re.findall(r"[a-z]+", (label or "").lower()))


def label_crossing(run):
    """Two units of a merged run under labels that share no name token (and are not an
    initial of one another) are two speakers; a quote must not cross that."""
    if len(run) < 2:
        return None
    base = run[0]
    for u in run[1:]:
        a, b = _label_tokens(base.speaker), _label_tokens(u.speaker)
        if not a or not b:
            continue
        if a & b:
            continue
        ia = set(t[0] for t in a)
        ib = set(t[0] for t in b)
        if (len(a) == 1 and list(a)[0] in ib and len(list(a)[0]) == 1) or \
                (len(b) == 1 and list(b)[0] in ia and len(list(b)[0]) == 1):
            continue
        return "%r then %r" % (base.speaker, u.speaker)
    return None


def _segment_defs(key, unit):
    """Segments of the composite block that sits on this unit, as {n: (starts, ends)}."""
    intake = key.get("intake") if isinstance(key, dict) else None
    cb = intake.get("composite_blocks") if isinstance(intake, dict) else None
    if not cb:
        return {}
    blocks = []
    if isinstance(cb, dict):
        for k, v in cb.items():
            if isinstance(v, dict):
                blocks.append((k, v))
    elif isinstance(cb, list):
        for v in cb:
            if isinstance(v, dict):
                blocks.append((None, v))
    for k, b in blocks:
        match = False
        if k and unit.time and k.lstrip("0:") == unit.time.lstrip("0:"):
            match = True
        if b.get("turn") == unit.n and unit.src.fmt.startswith("header"):
            match = True
        u = b.get("unit")
        if isinstance(u, str) and unit.time and unit.time in u and ("L%d" % unit.line) in u:
            match = True
        if not match:
            continue
        segs = None
        for name in ("candidate_segments", "segments"):
            if isinstance(b.get(name), list):
                segs = b[name]
        out = {}
        for sg in segs or []:
            n = sg.get("segment", sg.get("k", sg.get("n")))
            a = sg.get("starts", sg.get("from", sg.get("text_starts")))
            z = sg.get("ends", sg.get("to", sg.get("text_ends")))
            if isinstance(n, int) and isinstance(a, str) and isinstance(z, str):
                out[n] = (a, z)
        return out
    return {}


def segment_check(key, unit, n, qn):
    defs = _segment_defs(key, unit)
    if n not in defs:
        return None
    a, z = defs[n]
    tn = norm(unit.text)
    an = norm(a).rstrip(".\u2026 ")
    zn = norm(z).rstrip(".\u2026 ")
    sa = tn.find(an)
    if sa < 0:
        return "segment %d start text not found in the block, so the segment could not be checked" % n
    ze = tn.find(zn, sa)
    if ze < 0:
        return "segment %d end text not found in the block, so the segment could not be checked" % n
    ze += len(zn)
    for q in find_all(tn, qn):
        if q >= sa and q + len(qn) <= ze + 2:
            return "ok"
    return "outside:segment %d runs from %r to %r" % (n, a[:40], z[:40])


class QuoteIndex(object):
    """All units of all transcripts, for 'found elsewhere' searches and for presence-only checks."""

    def __init__(self, sources):
        self.sources = sources
        self.units = []
        for s in sources:
            if s.kind in ("transcript", "chat", "docx", "pdf"):
                for u in s.units:
                    self.units.append(u)
        self._norm = {}

    def nt(self, u):
        k = id(u)
        if k not in self._norm:
            if u.parts is not None:
                self._norm[k] = [norm(p) for p in (u.parts or [u.text])]
            else:
                self._norm[k] = [norm(u.text)]
        return self._norm[k]

    def find_exact(self, qn, limit=6):
        hits = []
        for u in self.units:
            for t in self.nt(u):
                if qn in t:
                    hits.append(u)
                    break
            if len(hits) >= limit:
                break
        if hits:
            return hits, "unit"
        # across adjacent units of one file (a quote that straddles a unit boundary)
        by_src = {}
        for u in self.units:
            if u.src.kind in ("transcript", "chat"):
                by_src.setdefault(id(u.src), []).append(u)
        for lst in by_src.values():
            for k in range(len(lst) - 1):
                for w in (2, 3):
                    run = lst[k:k + w]
                    if len(run) < w:
                        continue
                    joined = " ".join(self.nt(u)[0] for u in run)
                    if qn in joined and not any(qn in self.nt(u)[0] for u in run):
                        hits.append(run)
                        break
                if len(hits) >= limit:
                    break
        return hits, "run"

    def find_loose(self, qn, limit=4):
        lq = loose(qn)
        hits = []
        if len(lq) < 6:
            return hits
        for u in self.units:
            for t in self.nt(u):
                pass
            if lq in loose(" ".join(self.nt(u))):
                hits.append(u)
                if len(hits) >= limit:
                    break
        return hits

    def nearest(self, qn, prefer=None):
        """Best-aligned unit text for a quote that is nowhere: (unit, snippet, ratio, ops)."""
        qw = set(re.findall(r"\w+", qn.lower()))
        best = None
        cand = list(self.units)
        scored = []
        for u in cand:
            uw = set(re.findall(r"\w+", " ".join(self.nt(u)).lower()))
            if not uw:
                continue
            ov = len(qw & uw)
            scored.append((ov / float(len(qw) or 1), u))
        scored.sort(key=lambda x: -x[0])
        for _, u in scored[:6]:
            tn = " ".join(self.nt(u))
            sm = difflib.SequenceMatcher(None, qn.lower(), tn.lower(), autojunk=False)
            r = sm.find_longest_match(0, len(qn), 0, len(tn)).size / float(len(qn) or 1)
            if best is None or r > best[0]:
                best = (r, u, tn)
        if best is None:
            return None
        r, u, tn = best
        snippet, ops = diff_hint(qn, tn)
        return {"unit": u, "ratio": round(r, 2), "snippet": snippet or tn[:200], "ops": ops or []}


# --------------------------------------------------------------------------------------
# Walking the key
# --------------------------------------------------------------------------------------

LOC_KEYS = ("location", "locations", "at", "cue", "cues", "line", "lines", "where", "source")
_QUOTE_KEY = re.compile(r"(^|_)(re)?quotes?(_|$)", re.I)
PROSE_KEYS = ("figure_as_requoted", "contrast_with_the_wrong_requote")
# keys that document spans the key refuses; their strings are deliberately not locatable
REFUSED_KEYS = ("refused_quotes",)

_LOC_START = re.compile(r"^\s*(?:@|\[)?(?:call\s+\d+\s*,\s*|rec-\d+\s*,?\s*|chat\s+|cues?\s+\d|L\d|lines?\s+\d|turn\s+\d|paragraph\s+\d|" + TS + r")", re.I)
_LOC_TAIL = re.compile(r"\s*[\(\[]\s*((?:call\s+\d+\s*,\s*|rec-\d+\s*,?\s*)?(?:cues?|L|lines?|turn|paragraph|@)?\s*\d[^()\[\]]*)[\)\]]\s*$", re.I)


class Pair(object):
    def __init__(self, path, key, quote, loc_str, loc_key):
        self.path = path
        self.key = key
        self.quote = quote
        self.loc_str = loc_str
        self.loc_key = loc_key
        self.status = None
        self.reason = None
        self.where_found = []
        self.nearest = None
        self.warnings = []
        self.spans = []          # [(unit, start, end)] in original unit text
        self.elided = False
        self.presence_only = False
        self.cited = None
        self.loc_list = None

    def to_dict(self):
        d = OrderedDict()
        d["path"] = self.path
        d["status"] = self.status
        d["quote"] = self.quote
        d["location"] = self.loc_str
        if self.reason:
            d["reason"] = self.reason
        if self.presence_only:
            d["presence_only"] = True
        if self.elided:
            d["elided"] = True
        if self.cited:
            d["cited"] = self.cited
        if self.where_found:
            d["found_at"] = self.where_found
        if self.nearest:
            d["nearest"] = self.nearest
        if self.warnings:
            d["warnings"] = self.warnings
        return d


def collect(obj, path="", out=None, skipped=None, refused=None):
    if out is None:
        out, skipped, refused = [], [], []
    if isinstance(obj, dict):
        for k, v in obj.items():
            p = path + "/" + k
            if k in REFUSED_KEYS:
                if isinstance(v, list):
                    refused.append((p, len(v)))
                continue
            if _QUOTE_KEY.search(k) or k in PROSE_KEYS:
                if v is None or (isinstance(v, str) and not v.strip()):
                    skipped.append((p, "null or empty"))
                    continue
                if isinstance(v, str):
                    loc, lk = sibling_loc(obj, k)
                    out.append(Pair(p, k, v, loc if isinstance(loc, str) else None, lk))
                    if isinstance(loc, list) and loc:
                        out[-1].loc_list = [str(x) for x in loc]
                        out[-1].loc_str = " | ".join(out[-1].loc_list)
                        if len(loc) == 1:
                            out[-1].loc_str = out[-1].loc_list[0]
                    continue
                if isinstance(v, list) and v and all(isinstance(x, str) or x is None for x in v):
                    loc, lk = sibling_loc(obj, k)
                    for i, q in enumerate(v):
                        if q is None or not q.strip():
                            skipped.append((p + "[%d]" % i, "null or empty"))
                            continue
                        if isinstance(loc, list):
                            li = loc[i] if i < len(loc) else (loc[-1] if loc else None)
                        else:
                            li = loc
                        out.append(Pair(p + "[%d]" % i, k, q, li if isinstance(li, str) else None, lk))
                    continue
            collect(v, p, out, skipped, refused)
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            collect(v, "%s[%d]" % (path, i), out, skipped, refused)
    return out, skipped, refused


def sibling_loc(obj, qkey):
    # a location named for the key itself first (asked_quote / location), else the plain names
    for k in LOC_KEYS:
        if k in obj and k != qkey:
            v = obj[k]
            if isinstance(v, (str, list)) and v:
                return v, k
    return None, None


_LOC_TAIL2 = re.compile(r"\s+(?:@|[\u2014\u2013]|--)\s*((?:call\s+\d+\s*,\s*|rec-\d+\s*,?\s*|chat\s+)?(?:cues?\s+\d|L\d|lines?\s+\d|turn\s+\d|paragraph\s+\d|\[?" + TS + r")[^\n]{0,80})$", re.I)


def split_embedded(quote):
    """A location embedded at the end of a quote's own string: 'text (L142)', 'text [00:21:14 Name]',
    'text @00:21:14', 'text -- L142, Name'."""
    m = _LOC_TAIL.search(quote)
    if m and parse_loc(m.group(1)).recognised:
        return quote[:m.start()].rstrip(), m.group(1)
    m = _LOC_TAIL2.search(quote)
    if m and parse_loc(m.group(1)).recognised:
        return quote[:m.start()].rstrip(), m.group(1)
    return quote, None


# --------------------------------------------------------------------------------------
# Checking one pair
# --------------------------------------------------------------------------------------

def looks_like_pointer(s):
    """A string that is only a location (the from_quotes lists in s21)."""
    st = s.strip()
    if not _LOC_START.match(st):
        return False
    loc = parse_loc(st)
    if not loc.recognised:
        return False
    # remove the recognised tokens; what is left must be a name, role or nothing: no sentence
    rest = re.sub(r"\([^)]*\)", "", st)
    return not re.search(r"[.?!]\s*\S", rest) and len(rest.split()) <= 14


def multi_location_prose(quote):
    """A string that holds several quotes with their own locations in prose."""
    hits = re.findall(r"(?:\bL\d+\b|\bcues?\s+\d+|\b\d{1,2}:\d{2}(?::\d{2})?(?:[.,]\d+)?\b)", quote)
    return len(hits) >= 2 and re.search(r"[\"'‘“]", quote) is not None


def check_pair(p, sources, qi, key=None):
    """Check one pair; a quote offered with a list of locations is verified when any one holds."""
    locs = getattr(p, "loc_list", None)
    if not locs or len(locs) < 2:
        return check_pair_one(p, sources, qi, key)
    best = None
    rank = {"verified": 0, "near-miss": 1, "unsupported": 2, "unparsed": 3, "skipped": 4, "miss": 5}
    for ls in locs:
        q = Pair(p.path, p.key, p.quote, ls, p.loc_key)
        check_pair_one(q, sources, qi, key)
        if best is None or rank.get(q.status, 9) < rank.get(best.status, 9):
            best = q
    for attr in ("status", "reason", "where_found", "nearest", "warnings", "spans", "elided", "presence_only", "cited"):
        setattr(p, attr, getattr(best, attr))
    p.loc_str = " | ".join(locs) + "  (checked: " + best.loc_str + ")"


def check_pair_one(p, sources, qi, key=None):
    quote = p.quote
    if p.key in PROSE_KEYS:
        p.status = "unparsed"
        p.reason = "a description about a quote, not a quotation"
        return
    loc_str = p.loc_str
    if loc_str is None and multi_location_prose(quote) and not qi.find_exact(norm(quote))[0]:
        p.status = "unparsed"
        p.reason = "several quotes with their own locations in prose"
        return
    emb_quote, emb_loc = split_embedded(quote) if loc_str is None else (quote, None)
    if loc_str is None and emb_loc:
        loc_str = emb_loc
        quote = emb_quote
        p.loc_str = emb_loc + " (embedded)"
    qn = norm(quote)
    if loc_str is None:
        if looks_like_pointer(quote):
            loc = parse_loc(quote)
            r = resolve(loc, sources)
            if r.candidates:
                p.status = "skipped"
                p.reason = "location pointer (no quote text); it resolves to a real unit"
            elif r.unsupported:
                p.status = "unsupported"
                p.reason = r.unsupported
            else:
                p.status = "miss"
                p.reason = "pointer does not resolve: " + (r.error or "")
            return
        if multi_location_prose(quote) and not qi.find_exact(qn)[0]:
            p.status = "unparsed"
            p.reason = "several quotes with their own locations in prose"
            return
        # presence only
        p.presence_only = True
        hits, how = qi.find_exact(qn)
        if hits:
            p.status = "verified"
            p.reason = "presence only: no location cited; found in the file"
            p.where_found = [describe_hit(h) for h in hits[:3]]
            record_spans(p, qn, hits)
            return
        fr = match_elided([" ".join(qi.nt(u)) for u in qi.units], qn)
        lh = qi.find_loose(qn)
        if lh:
            p.status = "near-miss"
            p.reason = "no location cited; differs from the text only by punctuation or case"
            p.where_found = [describe_hit(h) for h in lh[:3]]
            return
        p.status = "miss"
        p.reason = "no location cited and the quote is not in any file"
        nr = qi.nearest(qn)
        if nr:
            p.nearest = {"at": nr["unit"].describe(), "text": nr["snippet"], "ratio": nr["ratio"], "differences": nr["ops"]}
        return
    loc = parse_loc(loc_str)
    if not loc.recognised:
        if multi_location_prose(loc_str):
            p.status = "unparsed"
            p.reason = "location holds several locations in prose"
        else:
            p.status = "miss"
            p.reason = "location form not understood: %r" % loc_str
        return
    if multi_location_prose(quote) and loc_str and len(re.findall(r"\bL\d+\b|\bcue", loc_str)) == 0 and False:
        pass
    res = resolve(loc, sources)
    p.warnings = list(res.warnings)
    if res.unsupported:
        p.status = "unsupported"
        p.reason = res.unsupported
        return
    if not res.candidates:
        p.status = "miss"
        p.reason = "location does not resolve: " + (res.error or "")
        hits, how = qi.find_exact(qn)
        if hits:
            p.where_found = [describe_hit(h) for h in hits[:4]]
        return
    # the quote against each candidate
    best_near = None
    for run in res.candidates:
        texts = texts_of(run)
        m = match_exact(texts, qn)
        if m:
            p.status = "verified"
            p.cited = ", ".join(u.describe() for u in run[:3]) + (" ..." if len(run) > 3 else "")
            record_spans(p, qn, [run], exact_in=run)
            crossing = label_crossing(run)
            if crossing:
                p.warnings.append("the cited run crosses a label change: " + crossing)
            seg = re.search(r"\bsegment\s+(\d+)", loc.raw, re.I)
            if seg and key is not None and len(run) == 1:
                msg = segment_check(key, run[0], int(seg.group(1)), qn)
                if msg == "ok" or msg is None:
                    pass
                elif msg.startswith("outside:"):
                    p.status = "miss"
                    p.reason = "in the cited block but not in the cited segment: " + msg[8:]
                    p.nearest = {"at": p.cited, "text": run[0].text[:240], "differences": []}
                else:
                    p.warnings.append(msg)
            return
    for run in res.candidates:
        texts = texts_of(run)
        m = match_elided(texts, qn)
        if m:
            p.status = "verified"
            p.elided = True
            p.reason = "verified as ordered fragments around an elision"
            p.cited = ", ".join(u.describe() for u in run[:3])
            return
    for run in res.candidates:
        texts = texts_of(run)
        m = match_loose(texts, qn)
        if m:
            best_near = (run, m)
            break
    if best_near:
        run, m = best_near
        p.status = "near-miss"
        p.cited = ", ".join(u.describe() for u in run[:3])
        p.reason = "differs from the cited text only by punctuation or case"
        snippet, ops = diff_hint(qn, " ".join(norm(t) for t in texts_of(run)))
        p.nearest = {"at": p.cited, "text": snippet, "differences": ops or []}
        return
    # several quotes with their own locations in one string: reported, not failed
    if multi_location_prose(quote):
        p.status = "unparsed"
        p.reason = "several quotes with their own locations in prose"
        return
    # a miss
    p.status = "miss"
    run = res.candidates[0]
    p.cited = ", ".join(u.describe() for u in run[:3])
    hits, how = qi.find_exact(qn)
    if hits:
        p.where_found = [describe_hit(h) for h in hits[:4]]
        if how == "run":
            p.reason = "not in the cited unit; found only across adjacent units"
        else:
            p.reason = "not at the cited location; found elsewhere"
    else:
        lh = qi.find_loose(qn)
        if lh:
            p.reason = "not at the cited location; found elsewhere differing by punctuation or case"
            p.where_found = [describe_hit(h) for h in lh[:4]]
        else:
            p.reason = "not in the cited unit and not found in any file"
    ctext = " ".join(norm(t) for t in texts_of(run))
    sm = difflib.SequenceMatcher(None, qn.lower(), ctext.lower(), autojunk=False)
    ratio = round(sm.find_longest_match(0, len(qn), 0, len(ctext)).size / float(len(qn) or 1), 2)
    snippet, ops = diff_hint(qn, ctext)
    p.nearest = {"at": p.cited, "text": snippet or ctext[:240], "ratio": ratio,
                 "differences": (ops or []) if ratio >= 0.6 else []}
    if ratio < 0.6:
        nr = qi.nearest(qn)
        if nr and nr["ratio"] > ratio:
            p.nearest["closest_elsewhere"] = {"at": nr["unit"].describe(), "text": nr["snippet"], "ratio": nr["ratio"]}


def describe_hit(h):
    if isinstance(h, list):
        return " + ".join(u.describe() for u in h)
    return h.describe()


def record_spans(p, qn, hits, exact_in=None):
    """Spans of the quote, as offsets into each unit's original text."""
    runs = [exact_in] if exact_in else [h if isinstance(h, list) else [h] for h in hits]
    for run in runs:
        if run[0].parts is not None:
            continue    # documents: spans are not tracked
        pieces = []
        off = 0
        joined = []
        for u in run:
            tn, mp = norm_map(u.text)
            pieces.append((u, tn, mp, off))
            joined.append(tn)
            off += len(tn) + 1
        jn = " ".join(joined)
        for s in find_all(jn, qn):
            e = s + len(qn)
            for (u, tn, mp, o) in pieces:
                a = max(s, o)
                b = min(e, o + len(tn))
                if a < b and tn:
                    p.spans.append((u, mp[a - o], mp[b - o - 1] + 1))


# --------------------------------------------------------------------------------------
# Reporting
# --------------------------------------------------------------------------------------

def run_folder(folder):
    keypath = os.path.join(folder, "answer-key.json")
    with open(keypath, "rb") as fh:
        key = json.loads(fh.read().decode("utf-8"), object_pairs_hook=OrderedDict)
    sources = load_sources(folder)
    qi = QuoteIndex(sources)
    pairs, skipped, refused = collect(key)
    for p in pairs:
        check_pair(p, sources, qi, key)
    return key, sources, pairs, skipped, refused


def counts(pairs, skipped):
    c = OrderedDict()
    c["pairs"] = len(pairs)
    c["verified"] = sum(1 for p in pairs if p.status == "verified")
    c["verified_presence_only"] = sum(1 for p in pairs if p.status == "verified" and p.presence_only)
    c["skipped"] = len(skipped) + sum(1 for p in pairs if p.status == "skipped")
    c["unparsed_prose"] = sum(1 for p in pairs if p.status == "unparsed")
    c["near_misses"] = sum(1 for p in pairs if p.status == "near-miss")
    c["misses"] = sum(1 for p in pairs if p.status == "miss")
    c["unsupported"] = sum(1 for p in pairs if p.status == "unsupported")
    c["warnings"] = sum(1 for p in pairs if p.warnings)
    return c


def short(s, n=160):
    s = s.replace("\n", " ")
    return s if len(s) <= n else s[:n - 1] + "…"


def readable(folder, sources, pairs, skipped, refused, spans):
    c = counts(pairs, skipped)
    out = []
    out.append("Fixture: %s" % os.path.basename(os.path.abspath(folder)))
    out.append("Sources: " + "; ".join("%s (%s%s, %d units)" % (
        s.name, s.kind, "/" + s.fmt if s.fmt and s.fmt != s.kind else "", len(s.units)) for s in sources))
    out.append("")
    out.append("pairs found      %d" % c["pairs"])
    out.append("verified         %d  (of which presence only, no location cited: %d)" % (c["verified"], c["verified_presence_only"]))
    out.append("skipped          %d  (null, empty or a bare location pointer)" % c["skipped"])
    out.append("unparsed prose   %d" % c["unparsed_prose"])
    out.append("near-misses      %d" % c["near_misses"])
    out.append("misses           %d" % c["misses"])
    out.append("unsupported      %d" % c["unsupported"])
    if refused:
        out.append("refused_quotes   %d entries in %d list(s) are the key's own refusals and are not checked" % (
            sum(n for _, n in refused), len(refused)))
    if c["warnings"]:
        out.append("location notes   %d pairs whose cited stamp or label disagrees with the unit at the cited index" % c["warnings"])
    for title, st in (("MISSES", "miss"), ("NEAR-MISSES", "near-miss")):
        sel = [p for p in pairs if p.status == st]
        if sel:
            out.append("")
            out.append(title)
            for p in sel:
                out.append("- %s" % p.path)
                out.append("    quote:   %s" % short(p.quote, 240))
                out.append("    cited:   %s" % (p.loc_str if p.loc_str else "(none)"))
                out.append("    why:     %s" % p.reason)
                if p.where_found:
                    out.append("    found:   %s" % "; ".join(p.where_found))
                if p.nearest:
                    out.append("    nearest: %s" % short(p.nearest.get("text") or "", 240))
                    if p.nearest.get("at"):
                        out.append("             (at %s)" % p.nearest["at"])
                    if p.nearest.get("differences"):
                        out.append("    diff:    %s" % "; ".join(short(x, 100) for x in p.nearest["differences"]))
                    ce = p.nearest.get("closest_elsewhere")
                    if ce:
                        out.append("    closest elsewhere: %s (at %s)" % (short(ce["text"], 160), ce["at"]))
    un = [p for p in pairs if p.status in ("unparsed", "unsupported")]
    if un:
        out.append("")
        out.append("UNPARSED PROSE AND UNSUPPORTED FORMS")
        for p in un:
            out.append("- %s [%s] %s | %s" % (p.path, p.status, p.reason, short(p.quote, 100)))
    wn = [p for p in pairs if p.warnings]
    if wn:
        out.append("")
        out.append("LOCATION NOTES")
        for p in wn:
            out.append("- %s: %s" % (p.path, "; ".join(p.warnings)))
    if spans:
        out.append("")
        out.append("QUOTED SPANS PER UNIT (text between ⟦ ⟧ must not change)")
        out.extend(spans_text(sources, pairs))
    return "\n".join(out)


def spans_by_unit(pairs):
    by = OrderedDict()
    for p in pairs:
        for (u, a, b) in p.spans:
            by.setdefault(id(u), (u, []))[1].append((a, b, p.path, p.presence_only))
    return by


def merge_spans(lst):
    lst = sorted(lst, key=lambda x: (x[0], x[1]))
    out = []
    for a, b, path, po in lst:
        if out and a <= out[-1][1]:
            out[-1][1] = max(out[-1][1], b)
            out[-1][2].append(path)
        else:
            out.append([a, b, [path], po])
    return out


def spans_text(sources, pairs):
    by = spans_by_unit(pairs)
    lines = []
    ordered = sorted(by.values(), key=lambda x: (x[0].src.name, x[0].n))
    for u, lst in ordered:
        merged = merge_spans(lst)
        txt = u.text
        marked = []
        pos = 0
        for a, b, paths, po in merged:
            marked.append(txt[pos:a])
            marked.append("⟦" + txt[a:b] + "⟧")
            pos = b
        marked.append(txt[pos:])
        lines.append("%s" % u.describe())
        lines.append("    %d span(s), %d citation(s)%s" % (
            len(merged), len(lst), "; includes presence-only quotes (every occurrence protected)" if any(m[3] for m in merged) else ""))
        for a, b, paths, po in merged:
            lines.append("    ⟦%s⟧" % short(txt[a:b], 200))
        if len(txt) <= 400:
            lines.append("    in context: " + "".join(marked))
    if not ordered:
        lines.append("(no verified quote with a transcript unit)")
    return lines


def json_report(folder, sources, pairs, skipped, refused, spans):
    rep = OrderedDict()
    rep["fixture"] = os.path.basename(os.path.abspath(folder))
    rep["sources"] = [OrderedDict([("name", s.name), ("kind", s.kind), ("format", s.fmt), ("units", len(s.units)),
                                   ("unsupported", s.unsupported)]) for s in sources]
    rep["counts"] = counts(pairs, skipped)
    rep["refused_quotes_not_checked"] = [OrderedDict([("path", p), ("entries", n)]) for p, n in refused]
    rep["skipped"] = [OrderedDict([("path", p), ("reason", r)]) for p, r in skipped]
    rep["pairs"] = [p.to_dict() for p in pairs]
    if spans:
        by = spans_by_unit(pairs)
        sp = []
        for u, lst in sorted(by.values(), key=lambda x: (x[0].src.name, x[0].n)):
            merged = merge_spans(lst)
            sp.append(OrderedDict([
                ("unit", u.describe()),
                ("source", u.src.name),
                ("line", u.line),
                ("spans", [OrderedDict([("start", a), ("end", b), ("text", u.text[a:b]), ("cited_by", paths)])
                           for a, b, paths, po in merged])]))
        rep["spans"] = sp
    return rep


def main(argv=None):
    ap = argparse.ArgumentParser(description="Verify every structured quote of a fixture key at its cited location.")
    ap.add_argument("folder")
    ap.add_argument("--json", action="store_true", help="emit the full report as JSON")
    ap.add_argument("--spans", action="store_true", help="print the quoted spans per transcript unit")
    a = ap.parse_args(argv)
    try:
        if not os.path.isdir(a.folder):
            raise IOError("not a folder: %s" % a.folder)
        key, sources, pairs, skipped, refused = run_folder(a.folder)
    except Exception as e:  # noqa
        sys.stderr.write("cannot read the fixture: %s\n" % e)
        return 3
    if a.json:
        print(json.dumps(json_report(a.folder, sources, pairs, skipped, refused, a.spans), indent=2, ensure_ascii=False))
    else:
        print(readable(a.folder, sources, pairs, skipped, refused, a.spans))
    c = counts(pairs, skipped)
    return 1 if (c["misses"] or c["near_misses"]) else 0


if __name__ == "__main__":
    sys.exit(main())
