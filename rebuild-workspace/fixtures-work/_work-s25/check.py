#!/usr/bin/env python3
"""Read-only verifier for fixture s25-client-documents.

Checks that each generated file opens with the standard library (zipfile for
the Word file, a byte scan and an xref walk for the PDF, PIL for the PNG),
that every quote in answer-key.json appears verbatim at its cited location in
its own file, that the key carries the 25 fields in the reviewed order plus an
intake block under 400 lines, and prints the counts the README records.

Usage: python3 check.py            (from anywhere)
Nothing is written."""
import collections
import json
import os
import re
import sys
import zipfile
import xml.etree.ElementTree as ET

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import content as ct  # noqa: E402  (only for the figure's labels; the image has no text layer)

FIX = os.path.normpath(os.path.join(HERE, "..", "..", "fixtures", "s25-client-documents"))
DOCX = os.path.join(FIX, "QP-07-sample-receipt-testing-certification-v3.2.docx")
PNG = os.path.join(FIX, "QP-07-F1-sample-flow.png")
PDF = os.path.join(FIX, "sample-tracking-what-we-need.pdf")
TXT = os.path.join(FIX, "transcript.txt")
KEY = os.path.join(FIX, "answer-key.json")

FIELDS = ["scenario_id", "call_type", "purpose_of_this_fixture", "transcript_format", "company", "attendees",
          "expected_monday_products", "rubric", "pains", "numbers", "vocabulary", "entities_and_workflows",
          "integrations_mentioned", "compliance_or_security_signals", "objections", "commitments_and_next_steps",
          "traps", "requested_changes", "should_plugin_propose_a_build", "expected_questions_before_building",
          "expected_verdict", "account_context", "expected_structures", "accepted_behaviours",
          "expected_leak_blocklist"]

W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
failures = []


def fail(msg):
    failures.append(msg)
    print("FAIL", msg)


# ------------------------------------------------------------------ docx
def read_docx():
    """Returns (paragraphs as [(section, style, text)], core metadata dict)."""
    with zipfile.ZipFile(DOCX) as z:
        bad = z.testzip()
        if bad:
            fail("docx: corrupt member %s" % bad)
        names = z.namelist()
        for must in ("[Content_Types].xml", "_rels/.rels", "word/document.xml", "docProps/core.xml"):
            if must not in names:
                fail("docx: missing part %s" % must)
        doc = ET.fromstring(z.read("word/document.xml"))
        core = ET.fromstring(z.read("docProps/core.xml"))
    paras, section = [], "front page"
    for p in doc.iter(W + "p"):
        style_el = p.find(W + "pPr/" + W + "pStyle")
        style = style_el.get(W + "val") if style_el is not None else "Normal"
        text = "".join(t.text or "" for t in p.iter(W + "t"))
        if style == "Heading1":
            m = re.match(r"(\d+)\.", text)
            section = m.group(1) if m else text.lower()
        elif style == "Heading2":
            section = text.split()[0]
        elif style in ("Title", "Meta"):
            section = "front page"
        paras.append((section, style, text))
    meta = {}
    for child in core:
        meta[child.tag.split("}")[1]] = child.text
    return paras, meta


# ------------------------------------------------------------------- pdf
def pdf_unescape(s):
    out, i = [], 0
    while i < len(s):
        c = s[i]
        if c == "\\" and i + 1 < len(s):
            out.append(s[i + 1])
            i += 2
        else:
            out.append(c)
            i += 1
    return "".join(out)


def read_pdf():
    """Byte scan plus an xref walk. Returns (pages as [[line, ...]], info dict)."""
    data = open(PDF, "rb").read()
    info = {"bytes": len(data), "header": data[:8].decode("latin-1")}
    if not data.startswith(b"%PDF-1."):
        fail("pdf: no PDF header")
    # xref walk
    m = re.search(rb"startxref\s+(\d+)\s+%%EOF\s*$", data)
    if not m:
        fail("pdf: no startxref")
        return [], info
    xref_at = int(m.group(1))
    if data[xref_at:xref_at + 4] != b"xref":
        fail("pdf: startxref %d does not point at the xref table" % xref_at)
    xm = re.match(rb"xref\s+0 (\d+)\s+", data[xref_at:])
    count = int(xm.group(1))
    entries = re.findall(rb"(\d{10}) (\d{5}) ([nf])", data[xref_at + xm.end():xref_at + xm.end() + 20 * count])
    if len(entries) != count:
        fail("pdf: xref has %d entries, expected %d" % (len(entries), count))
    objects = {}
    for n, (off, gen, kind) in enumerate(entries):
        if kind != b"n":
            continue
        off = int(off)
        head = data[off:off + 16]
        if not head.startswith(("%d 0 obj" % n).encode()):
            fail("pdf: xref offset %d for object %d points at %r" % (off, n, head))
        end = data.index(b"endobj", off)
        objects[n] = data[off:end]
    info["objects"] = len(objects)
    trailer = data[data.index(b"trailer"):]
    if b"/Info" in trailer:
        fail("pdf: trailer carries an /Info dictionary")
    if b"/Author" in data or b"/Creator" in data or b"/CreationDate" in data:
        fail("pdf: author or creation metadata present")
    info["info_dict"] = "absent"
    # page order from the catalog
    root = int(re.search(rb"/Root (\d+) 0 R", trailer).group(1))
    pages_ref = int(re.search(rb"/Pages (\d+) 0 R", objects[root]).group(1))
    kids = [int(k) for k in re.findall(rb"(\d+) 0 R", re.search(rb"/Kids \[([^\]]*)\]", objects[pages_ref]).group(1))]
    pages = []
    for k in kids:
        contents = int(re.search(rb"/Contents (\d+) 0 R", objects[k]).group(1))
        body = objects[contents]
        stream = body[body.index(b"stream\n") + 7:body.index(b"endstream")]
        length = int(re.search(rb"/Length (\d+)", body).group(1))
        if len(stream) != length:
            fail("pdf: object %d /Length %d, stream is %d bytes" % (contents, length, len(stream)))
        lines = [pdf_unescape(s.decode("latin-1")) for s in re.findall(rb"\(((?:\\.|[^\\)])*)\) Tj", stream)]
        pages.append(lines)
    info["pages"] = len(pages)
    info["text_lines"] = sum(len(p) for p in pages)
    info["fonts"] = sorted(set(re.findall(rb"/BaseFont /([A-Za-z-]+)", data)))
    return pages, info


# ------------------------------------------------------------------- png
def read_png():
    from PIL import Image
    im = Image.open(PNG)
    im.verify()
    im = Image.open(PNG)
    info = {"format": im.format, "size": im.size, "mode": im.mode, "text_chunks": sorted(im.text.keys())}
    px = im.convert("L")
    dark = sum(1 for v in px.getdata() if v < 128)
    info["dark_pixels"] = dark
    if im.format != "PNG":
        fail("png: not a PNG")
    if dark < 5000:
        fail("png: nearly blank (%d dark pixels)" % dark)
    return info


# ------------------------------------------------------------ transcript
def read_transcript():
    turns = {}
    lines = open(TXT, encoding="ascii").read().split("\n")
    if lines[-1] == "":
        lines = lines[:-1]
    for ln in lines:
        m = re.match(r"^\[(\d\d:\d\d:\d\d)\] ([^:]+): (.*)$", ln)
        if not m:
            fail("transcript: malformed line %r" % ln[:60])
            continue
        stamp, spk, text = m.groups()
        if stamp in turns:
            fail("transcript: duplicate timestamp %s" % stamp)
        turns[stamp] = (spk, text)
    return turns, len(lines)


# ---------------------------------------------------------------- quotes
def walk(obj, path="key"):
    """Yields (path, dict) for every dict carrying a quote key."""
    if isinstance(obj, dict):
        if "quote" in obj:
            yield path, obj
        for k, v in obj.items():
            for item in walk(v, path + "." + k):
                yield item
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            for item in walk(v, "%s[%d]" % (path, i)):
                yield item


def norm(s):
    return re.sub(r"\s+", " ", s).strip()


def check_quote(path, quote, location, docx_paras, pdf_pages, turns):
    if quote is None:
        return "null"
    if location is None:
        # quote-only field (requested_changes, evidence_quote_or_null): anywhere in any input
        alltext = [t for _, _, t in docx_paras] + [" ".join(p) for p in pdf_pages] + [t for _, t in turns.values()]
        if not any(quote in t or norm(quote) in norm(t) for t in alltext):
            fail("%s: quote-only string not found in any input: %r" % (path, quote[:70]))
        return "quote-only"
    m = re.match(r"^QP-07 (?:section (\S+)|(front page)|(revision history))$", location)
    if m:
        sec = m.group(1) or m.group(2) or m.group(3)
        hits = [t for s, _, t in docx_paras if s == sec and quote in t]
        if not hits:
            fail("%s: not in QP-07 %s: %r" % (path, sec, quote[:70]))
        return "doc"
    m = re.match(r"^write-up p\.(\d) section (\d)(?:, (W-\d+))?$", location)
    if m:
        page, sec = int(m.group(1)), m.group(2)
        lines = pdf_pages[page - 1] if page - 1 < len(pdf_pages) else []
        cur, in_sec = None, []
        for ln in lines:
            h = re.match(r"^(\d)\. ", ln)
            if h:
                cur = h.group(1)
            elif cur == sec:
                in_sec.append(ln)
        joined = norm(" ".join(in_sec))
        if norm(quote) not in joined:
            fail("%s: not in write-up p.%d section %s: %r" % (path, page, sec, quote[:70]))
        return "doc"
    if location == "figure 1 p.1":
        labels = [n[2] for n in ct.NODES] + [e[2] for e in ct.EDGES if e[2]]
        if quote not in labels:
            fail("%s: not a figure label: %r" % (path, quote))
        return "doc"
    m = re.match(r"^(\d\d:\d\d:\d\d) ([^()]+?)(?: \((.+)\))?$", location)
    if m:
        stamp, spk = m.group(1), m.group(2)
        if stamp not in turns:
            fail("%s: no turn at %s" % (path, stamp))
            return "call"
        tspk, text = turns[stamp]
        if tspk != spk:
            fail("%s: turn %s is %s, cited as %s" % (path, stamp, tspk, spk))
        if quote not in text:
            fail("%s: not in turn %s: %r" % (path, stamp, quote[:70]))
        return "call"
    fail("%s: unrecognised location %r" % (path, location))
    return "?"


def main():
    print("== files")
    docx_paras, core = read_docx()
    print("docx: %d paragraphs; core: creator=%r created=%r modified=%r status=%r" % (
        len(docx_paras), core.get("creator"), core.get("created"), core.get("modified"), core.get("contentStatus")))
    for want in ("creator", "created", "modified"):
        if not core.get(want):
            fail("docx: core.xml lacks %s" % want)
    pdf_pages, pinfo = read_pdf()
    print("pdf: %s" % pinfo)
    png_info = read_png()
    print("png: %s" % png_info)
    turns, nlines = read_transcript()
    print("transcript: %d lines, %d turns, %s to %s" % (nlines, len(turns), min(turns), max(turns)))

    print("== key")
    raw = open(KEY, encoding="ascii").read()
    key = json.loads(raw)
    lines = raw.count("\n")
    print("key: %d lines, %d bytes, %d top-level fields" % (lines, len(raw), len(key)))
    if lines >= 400:
        fail("key: %d lines, budget is under 400" % lines)
    if list(key.keys()) != FIELDS + ["intake"]:
        fail("key: field order differs from s1 to s10 plus intake")

    counts = collections.Counter()
    for path, d in walk(key):
        kind = check_quote(path, d.get("quote"), d.get("location"), docx_paras, pdf_pages, turns)
        counts[kind] += 1
    # asked quotes sit inside rubric rows under their own key
    for r in key["rubric"]:
        aq = r.get("asked_quote")
        if r.get("asked") and not aq:
            fail("rubric %s: asked true with no asked_quote" % r["criterion"])
        if not r.get("asked") and aq:
            fail("rubric %s: asked false with an asked_quote" % r["criterion"])
    ev = key["account_context"]["evidence_quote_or_null"]
    counts[check_quote("account_context", ev, None, docx_paras, pdf_pages, turns)] += 1
    print("quotes checked: %s" % dict(counts))

    print("== counts for the README")
    rub = key["rubric"]
    st = collections.Counter(r["status"] for r in rub)
    asked = collections.Counter(bool(r.get("asked")) for r in rub)
    print("rubric rows %d: %s; asked true %d false %d" % (len(rub), dict(st), asked[True], asked[False]))
    for status in sorted(st):
        print("  %s: %s" % (status, ", ".join(r["criterion"] for r in rub if r["status"] == status)))
    pains = set(r["criterion"].split()[0] for r in rub if r["criterion"].startswith("P"))
    exc = [p for p in sorted(pains) if all(
        next(r["status"] for r in rub if r["criterion"] == "%s %s" % (p, c)) in ("met", "met-with-residual")
        for c in ("Stated", "Concrete", "Workaround"))]
    print("graded pains %d (%s), excavated %d (%s); pains array %d" % (
        len(pains), ", ".join(sorted(pains)), len(exc), ", ".join(exc), len(key["pains"])))
    obj = collections.Counter(re.split(r" \(|: ", o["type"])[0] for o in key["objections"])
    print("objections %d: %s" % (len(key["objections"]), dict(obj)))
    rc = collections.Counter(c["type"] for c in key["requested_changes"])
    print("traps %d; blocklist %d; requested changes %s; commitments %d; questions %d; vocabulary %d; "
          "accepted behaviours %d; attendees %d; lookalike traps %d; native boards %d; portfolio_expected %r" % (
              len(key["traps"]), len(key["expected_leak_blocklist"]), dict(rc), len(key["commitments_and_next_steps"]),
              len(key["expected_questions_before_building"]), len(key["vocabulary"]), len(key["accepted_behaviours"]),
              len(key["attendees"]), len(key["expected_structures"]["lookalike_traps"]),
              len(key["expected_structures"]["native_boards_required"]), key["expected_structures"]["portfolio_expected"]))
    v = key["expected_verdict"]
    print("verdict %r; gates met %d, not met %d; propose build %r" % (
        v["verdict"], len(v["gates_met"]), len(v["gates_not_met"]), key["should_plugin_propose_a_build"]))
    ik = key["intake"]
    print("intake: files %d; section map %d; documented rows %d (%d decisions); read-back rows %d; conflicts %d; "
          "not-conflicts %d; second-hand %d; alias map %d; rejoined %d; claims %d; delivery notes %d; "
          "document-only criteria %d; moved with the call %d" % (
              len(ik["files"]), len(ik["section_map"]), len(ik["documented_rows"]),
              sum(1 for r in ik["documented_rows"] if r["kind"] == "decision"), len(ik["read_back"]["rows"]),
              len(ik["conflicts"]), len(ik["not_conflicts"]), len(ik["second_hand"]), len(ik["alias_map"]),
              len(ik["rejoined_sentences"]), len(ik["claims_by_our_side"]), len(ik["delivery_notes"]),
              len(ik["grading_passes"]["document_only"]["criteria"]), len(ik["grading_passes"]["with_call"]["moved"])))

    # A12 and hygiene scans over every file the fixture ships
    print("== hygiene")
    texts = {"key": raw, "transcript": open(TXT, encoding="ascii").read(),
             "docx": " ".join(t for _, _, t in docx_paras), "pdf": " ".join(" ".join(p) for p in pdf_pages)}
    for name, text in texts.items():
        try:
            text.encode("ascii")
        except UnicodeEncodeError:
            fail("%s: non-ASCII content" % name)
        for bad in ("DelOps", "Master Builder", "The user", "the user's name"):
            if bad in text:
                fail("%s: carries %r" % (name, bad))
    print("ascii and naming scans done")
    print("== result: %s" % ("OK, %d checks passed" % sum(counts.values()) if not failures else "%d FAILURES" % len(failures)))
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
