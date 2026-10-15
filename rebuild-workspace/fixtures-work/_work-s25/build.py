#!/usr/bin/env python3
"""Builds fixture s25-client-documents: the four input files and answer-key.json.

Standard library for the Word file, the PDF and the transcript; PIL (present on
this Mac) for the PNG. Run from anywhere: python3 build.py. It overwrites the
fixture files, so it is not re-run after review; check.py is the read-only
verifier. Every call quote in the key is asserted against its turn here and
re-verified against the files on disk by check.py."""
import json
import os
import re
import sys
import zipfile
from xml.sax.saxutils import escape

from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import content as ct  # noqa: E402

OUT = os.path.normpath(os.path.join(HERE, "..", "..", "fixtures", "s25-client-documents"))
SOP_FILE = "QP-07-sample-receipt-testing-certification-v3.2.docx"
FIG_FILE = "QP-07-F1-sample-flow.png"
WU_FILE = "sample-tracking-what-we-need.pdf"
TX_FILE = "transcript.txt"
HELVETICA = "/System/Library/Fonts/Helvetica.ttc"


# ---------------------------------------------------------------- docx
CONTENT_TYPES = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
<Default Extension="xml" ContentType="application/xml"/>
<Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>
<Override PartName="/word/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/>
<Override PartName="/docProps/core.xml" ContentType="application/vnd.openxmlformats-package.core-properties+xml"/>
<Override PartName="/docProps/app.xml" ContentType="application/vnd.openxmlformats-officedocument.extended-properties+xml"/>
</Types>"""

RELS = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>
<Relationship Id="rId2" Type="http://schemas.openxmlformats.org/package/2006/relationships/metadata/core-properties" Target="docProps/core.xml"/>
<Relationship Id="rId3" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/extended-properties" Target="docProps/app.xml"/>
</Relationships>"""

DOC_RELS = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/>
</Relationships>"""

STYLES = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:styles xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
<w:docDefaults><w:rPrDefault><w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial"/><w:sz w:val="22"/></w:rPr></w:rPrDefault>
<w:pPrDefault><w:pPr><w:spacing w:after="120"/></w:pPr></w:pPrDefault></w:docDefaults>
<w:style w:type="paragraph" w:default="1" w:styleId="Normal"><w:name w:val="Normal"/></w:style>
<w:style w:type="paragraph" w:styleId="Title"><w:name w:val="Title"/><w:basedOn w:val="Normal"/><w:pPr><w:spacing w:after="240"/></w:pPr><w:rPr><w:b/><w:sz w:val="36"/></w:rPr></w:style>
<w:style w:type="paragraph" w:styleId="Meta"><w:name w:val="Meta"/><w:basedOn w:val="Normal"/><w:pPr><w:spacing w:after="40"/></w:pPr><w:rPr><w:sz w:val="20"/></w:rPr></w:style>
<w:style w:type="paragraph" w:styleId="Heading1"><w:name w:val="heading 1"/><w:basedOn w:val="Normal"/><w:pPr><w:keepNext/><w:spacing w:before="360" w:after="120"/><w:outlineLvl w:val="0"/></w:pPr><w:rPr><w:b/><w:sz w:val="28"/></w:rPr></w:style>
<w:style w:type="paragraph" w:styleId="Heading2"><w:name w:val="heading 2"/><w:basedOn w:val="Normal"/><w:pPr><w:keepNext/><w:spacing w:before="240" w:after="80"/><w:outlineLvl w:val="1"/></w:pPr><w:rPr><w:b/><w:sz w:val="24"/></w:rPr></w:style>
</w:styles>"""

CORE = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:dcmitype="http://purl.org/dc/dcmitype/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
<dc:title>QP-07 Sample Receipt, Testing and Certification Procedure</dc:title>
<dc:subject>Quality procedure</dc:subject>
<dc:creator>Annelise Valdemarsson</dc:creator>
<cp:keywords>QP-07; sample receipt; certification</cp:keywords>
<cp:lastModifiedBy>Annelise Valdemarsson</cp:lastModifiedBy>
<cp:revision>14</cp:revision>
<dcterms:created xsi:type="dcterms:W3CDTF">2026-02-24T10:05:00Z</dcterms:created>
<dcterms:modified xsi:type="dcterms:W3CDTF">2026-03-11T09:14:00Z</dcterms:modified>
<cp:contentStatus>Approved</cp:contentStatus>
</cp:coreProperties>"""

APP = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Properties xmlns="http://schemas.openxmlformats.org/officeDocument/2006/extended-properties" xmlns:vt="http://schemas.openxmlformats.org/officeDocument/2006/docPropsVTypes">
<Pages>5</Pages><Words>{words}</Words><Company>Wexcombe Seed Testing Laboratory</Company>
</Properties>"""


def build_docx():
    paras = []
    for style, text in ct.SOP:
        ppr = "" if style == "Normal" else '<w:pPr><w:pStyle w:val="%s"/></w:pPr>' % style
        paras.append('<w:p>%s<w:r><w:t xml:space="preserve">%s</w:t></w:r></w:p>' % (ppr, escape(text)))
    document = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
        '<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">'
        "<w:body>" + "\n".join(paras) +
        '<w:sectPr><w:pgSz w:w="11906" w:h="16838"/><w:pgMar w:top="1440" w:right="1440" w:bottom="1440" w:left="1440"/></w:sectPr>'
        "</w:body></w:document>"
    )
    words = sum(len(t.split()) for _, t in ct.SOP)
    with zipfile.ZipFile(os.path.join(OUT, SOP_FILE), "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("[Content_Types].xml", CONTENT_TYPES)
        z.writestr("_rels/.rels", RELS)
        z.writestr("word/document.xml", document)
        z.writestr("word/_rels/document.xml.rels", DOC_RELS)
        z.writestr("word/styles.xml", STYLES)
        z.writestr("docProps/core.xml", CORE)
        z.writestr("docProps/app.xml", APP.format(words=words))
    return {"paragraphs": len(ct.SOP), "words": words}


# ----------------------------------------------------------------- pdf
PAGE_W, MARGIN = 595, 72


def pdf_escape(s):
    return s.replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)")


def page_stream(entries):
    """One content stream: every text line is its own BT ... Tj ET block."""
    ops, y = [], 760
    for style, text in entries:
        if style == "Title":
            font, size, gap = "/F2", 16, 26
        elif style == "Sub":
            font, size, gap = "/F1", 11, 16
        elif style == "Heading":
            font, size, gap = "/F2", 12, 20
            y -= 6
        elif style == "Blank":
            y -= 8
            continue
        else:
            font, size, gap = "/F1", 10, 14
        if text:
            face = ImageFont.truetype(HELVETICA, size, index=1 if font == "/F2" else 0)
            width = ImageDraw.Draw(Image.new("L", (1, 1))).textlength(text, font=face)
            assert width <= PAGE_W - 2 * MARGIN, "PDF line too wide (%.0f pt): %s" % (width, text)
            ops.append("BT %s %d Tf %d %d Td (%s) Tj ET" % (font, size, MARGIN, y, pdf_escape(text)))
        y -= gap
    assert y > MARGIN, "PDF page overflows"
    return "\n".join(ops) + "\n"


def build_pdf():
    page1 = ct.WRITEUP[:ct.WRITEUP_PAGE1_END]
    page2 = ct.WRITEUP[ct.WRITEUP_PAGE1_END:]
    streams = [page_stream(page1), page_stream(page2)]
    objs = []
    objs.append("<< /Type /Catalog /Pages 2 0 R >>")
    objs.append("<< /Type /Pages /Kids [3 0 R 4 0 R] /Count 2 >>")
    page_tpl = ("<< /Type /Page /Parent 2 0 R /MediaBox [0 0 595 842] "
                "/Resources << /Font << /F1 5 0 R /F2 6 0 R >> >> /Contents %d 0 R >>")
    objs.append(page_tpl % 7)
    objs.append(page_tpl % 8)
    objs.append("<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica /Encoding /WinAnsiEncoding >>")
    objs.append("<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Bold /Encoding /WinAnsiEncoding >>")
    for s in streams:
        objs.append("<< /Length %d >>\nstream\n%sendstream" % (len(s.encode("latin-1")), s))
    out = bytearray(b"%PDF-1.4\n%\xe2\xe3\xcf\xd3\n")
    offsets = []
    for i, body in enumerate(objs, start=1):
        offsets.append(len(out))
        out += ("%d 0 obj\n%s\nendobj\n" % (i, body)).encode("latin-1")
    xref_at = len(out)
    out += ("xref\n0 %d\n" % (len(objs) + 1)).encode("latin-1")
    out += b"0000000000 65535 f \n"
    for off in offsets:
        out += ("%010d 00000 n \n" % off).encode("latin-1")
    out += ("trailer\n<< /Size %d /Root 1 0 R >>\nstartxref\n%d\n%%%%EOF\n"
            % (len(objs) + 1, xref_at)).encode("latin-1")
    with open(os.path.join(OUT, WU_FILE), "wb") as f:
        f.write(bytes(out))
    return {"pages": len(streams), "lines": sum(1 for s, t in ct.WRITEUP if s != "Blank"), "bytes": len(out)}


# ----------------------------------------------------------------- png
W, H = 1000, 1560
COL_X = {"c": 400, "r": 790}
ROW_Y0, ROW_DY = 150, 128
BOX_W, BOX_H = 330, 74
DIA_W, DIA_H = 300, 110


def font(size, bold=False):
    return ImageFont.truetype(HELVETICA, size, index=1 if bold else 0)


def centre(node):
    return COL_X[node[3]], ROW_Y0 + node[4] * ROW_DY


def shape_bounds(node):
    cx, cy = centre(node)
    if node[1] == "decision":
        return cx - DIA_W // 2, cy - DIA_H // 2, cx + DIA_W // 2, cy + DIA_H // 2
    return cx - BOX_W // 2, cy - BOX_H // 2, cx + BOX_W // 2, cy + BOX_H // 2


def arrow(d, p0, p1, width=3):
    d.line([p0, p1], fill="black", width=width)
    x0, y0 = p0
    x1, y1 = p1
    if x0 == x1:
        s = 1 if y1 > y0 else -1
        head = [(x1, y1), (x1 - 9, y1 - s * 16), (x1 + 9, y1 - s * 16)]
    else:
        s = 1 if x1 > x0 else -1
        head = [(x1, y1), (x1 - s * 16, y1 - 9), (x1 - s * 16, y1 + 9)]
    d.polygon(head, fill="black")


def build_png():
    img = Image.new("RGB", (W, H), "white")
    d = ImageDraw.Draw(img)
    f_label, f_small = font(22), font(20, True)
    d.text((60, 40), ct.FIGURE_TITLE, fill="black", font=font(30, True))
    d.text((60, 84), ct.FIGURE_REF, fill="black", font=font(20))
    by_id = {n[0]: n for n in ct.NODES}
    for a, b, label in ct.EDGES:  # edges first so shapes sit on top
        na, nb = by_id[a], by_id[b]
        ax, ay = centre(na)
        bx, by = centre(nb)
        al, at, ar, ab = shape_bounds(na)
        bl, bt, br, bb = shape_bounds(nb)
        if na[4] > nb[4]:  # the return loop: up the right column, then left into the side of the target
            d.line([(ax, at), (ax, by)], fill="black", width=3)
            arrow(d, (ax, by), (br + 2, by))
            d.text((ax + 12, (at + by) // 2 - 12), label, fill="black", font=font(20))
        elif na[3] == nb[3]:  # same column, straight down
            arrow(d, (ax, ab), (bx, bt - 2))
            if label:
                d.text((ax + 14, ab + 8), label, fill="black", font=f_small)
        elif na[3] == "c":  # decision exit to the right
            arrow(d, (ar, ay), (bl - 2, by))
            if label:
                d.text((ar + 14, ay - 30), label, fill="black", font=f_small)
        else:  # right column back to the centre: down, then left
            d.line([(ax, ab), (ax, by)], fill="black", width=3)
            arrow(d, (ax, by), (br + 2, by))
    for n in ct.NODES:
        cx, cy = centre(n)
        l, t, r, b = shape_bounds(n)
        if n[1] == "decision":
            d.polygon([(cx, t), (r, cy), (cx, b), (l, cy)], fill="#fff6d5", outline="black", width=3)
        elif n[1] in ("start", "end"):
            d.rounded_rectangle([l, t, r, b], radius=37, fill="#e4efe6", outline="black", width=3)
        else:
            d.rectangle([l, t, r, b], fill="#eef2f7", outline="black", width=3)
        tw = d.textlength(n[2], font=f_label)
        d.text((cx - tw / 2, cy - 13), n[2], fill="black", font=f_label)
    d.text((60, H - 60), ct.FIGURE_NOTE, fill="black", font=font(18))
    img.save(os.path.join(OUT, FIG_FILE), format="PNG", optimize=True)
    return {"size": img.size, "nodes": len(ct.NODES), "edges": len(ct.EDGES)}


# ------------------------------------------------------------ transcript
def build_transcript():
    t, lines, stamps = 3.0, [], []
    for i, (spk, text) in enumerate(ct.TURNS):
        stamp = "%02d:%02d:%02d" % (int(t // 3600), int(t % 3600 // 60), int(t % 60))
        stamps.append(stamp)
        lines.append("[%s] %s: %s" % (stamp, spk, text))
        dur = len(text.split()) / 2.55 + 0.9 + (i % 3) * 0.35
        if "[pause]" in text:
            dur += 9
        if "[laughs]" in text:
            dur += 1.2
        t += dur
    with open(os.path.join(OUT, TX_FILE), "w", encoding="ascii", newline="\n") as f:
        f.write("\n".join(lines) + "\n")
    total, longest_c = {}, (0, "")
    for (spk, text), st in zip(ct.TURNS, stamps):
        n = len(re.sub(r"\[[a-z]+\]", "", text).split())
        total[spk] = total.get(spk, 0) + n
        if spk == ct.C and n > longest_c[0]:
            longest_c = (n, st)
    allw = sum(total.values())
    alltext = "\n".join(lines)
    stats = {"lines": len(lines), "first": stamps[0], "last": stamps[-1], "words": allw, "by_speaker": total,
             "client_share": 100.0 * (allw - total[ct.C]) / allw, "longest_consultant": longest_c,
             "laughs": alltext.count("[laughs]"), "pause": alltext.count("[pause]"), "dashes": alltext.count(" -- ")}
    return stamps, stats


# ----------------------------------------------------------------- key
def build_key(STAMPS, ts, docx_info, pdf_info, png_info):
    def T(i):
        return STAMPS[i]

    def L(i):
        spk = ct.TURNS[i][0]
        role = ct.ROLES.get(spk)
        return "%s %s" % (STAMPS[i], spk) + (" (%s)" % role if role else "")

    def Q(i, text):
        assert text in ct.TURNS[i][1], "turn %d lacks: %s" % (i, text)
        return {"quote": text, "location": L(i)}

    def D(text, loc):
        return {"quote": text, "location": loc}

    def row(criterion, status, evidence, note, asked, asked_quote=None):
        r = {"criterion": criterion, "status": status, "evidence": evidence, "note": note, "asked": asked}
        if asked_quote is not None:
            r["asked_quote"] = asked_quote
        return r

    MEET = "2026-10-09"
    key = {}
    key["scenario_id"] = "s25-client-documents"
    key["call_type"] = "discovery"
    key["purpose_of_this_fixture"] = (
        "The document fixture (A16, WP18): not a transcript fixture. Three client documents and one short call. The documents: a client SOP as a Word file "
        "(QP-07, version 3.2, with an author, a date and a status on its front page and in its core metadata), a flowchart as a PNG image (Figure 1, QP-07-F1, "
        "twelve nodes with two decision diamonds and labelled exits, no metadata), and a requirements write-up as a PDF with no author, date or status anywhere. "
        "The call: fifteen minutes with the Sample Reception Coordinator, the operator who runs the documented process, in which she says the documented "
        "priority-approval step (QP-07 section 4.2) is not used. Fictional client: an independent seed-testing laboratory. It proves that each document is measured, "
        "saved unchanged into inputs/ and stopped at the same open question as a transcript [A11-3]; that author, date and status are recorded from the SOP and "
        "left unknown on the figure and the write-up, with no author invented; that the SOP's sections feed current state while the write-up feeds the requirement "
        "trace and never the current-state picture; that the flowchart's steps and decision points become documented rows in the structure inventory citing the "
        "page; that every extract is [Q/doc] by document and section or page and never by speaker, at the attributed tier for the SOP and one step below for the "
        "write-up and the figure; that the document-versus-call disagreement on the priority approval is kept as a conflict with both sources and offered as a "
        "callback, never resolved by recency and never discarded; and that the record grades twice: document-only first, with no type header, nothing advisory, "
        "the current-state and requirements criteria Met from the documents (each with a residual) and cost, why-now, decision and next step Missing with every "
        "gap shown, then with the call, where the operator's figure grades as a client figure and the verdict becomes Nearly ready. Taking the call first and the "
        "documents after ends in the same record (intake.grading_passes.arrival_orders)."
    )
    key["transcript_format"] = (
        "Four input files. (1) %s: a Word file built as a zip of [Content_Types].xml, _rels/.rels, word/document.xml (%d paragraphs: a Title, eight Meta lines, "
        "Heading1 and Heading2 headings, Normal paragraphs, one run each), word/styles.xml, docProps/core.xml (dc:creator, dcterms:created, dcterms:modified, "
        "cp:contentStatus) and docProps/app.xml; eight numbered sections plus a revision history; ASCII text. (2) %s: a PNG image, %d by %d pixels, RGB, no text "
        "chunks; a title, a reference, %d nodes and %d arrows with the exit labels Yes and No on each diamond and re-test on the loop; it has no text layer, so its "
        "labels are read from the image. (3) %s: an uncompressed PDF 1.4 with a catalog, a page tree, two pages, Helvetica and Helvetica-Bold font resources, one "
        "content stream per page with every text line in its own Tj operator, a correct xref table and no document information dictionary; ASCII text, %d lines; "
        "page 1 holds sections 1 and 2 (W-1 to W-10), page 2 sections 3 and 4. (4) %s: plain text, %d lines, one speaker turn per line as '[HH:MM:SS] Speaker "
        "Name: text', turn start times from [%s] to [%s], no header and no call date. Speakers: 'Consultant', 'Rosalind Okonjo' (Sample Reception Coordinator) "
        "and one line labelled 'Speaker 2'. About %d spoken words; client share about %.0f%%; the Consultant's longest turn is %d words at [%s], the first-cut "
        "playback. Artefacts: [laughs] x%d, [pause] x%d, ' -- ' x%d, no crosstalk marker. Locations in this key: a call quote is 'HH:MM:SS Speaker Name (role)' "
        "from the line it is on, the Consultant with no role; a document extract is 'QP-07 section N.N' (or 'QP-07 front page', 'QP-07 revision history') for the "
        "SOP, 'write-up p.N section N' with the W id where one applies for the PDF, and 'figure 1 p.1' for the image, never a speaker. A document extract sits "
        "inside one paragraph of the SOP, inside one section of one page of the write-up (lines joined by a space, as a text extractor yields them), or is one "
        "label of the figure. Every document extract is [Q/doc]; every call quote is [Q]."
        % (SOP_FILE, docx_info["paragraphs"], FIG_FILE, png_info["size"][0], png_info["size"][1], png_info["nodes"], png_info["edges"],
           WU_FILE, pdf_info["lines"], TX_FILE, ts["lines"], ts["first"], ts["last"], ts["words"], ts["client_share"],
           ts["longest_consultant"][0], ts["longest_consultant"][1], ts["laughs"], ts["pause"], ts["dashes"])
    )
    key["company"] = {
        "name": "Wexcombe Seed Testing Laboratory (called 'the lab' or 'the building')",
        "industry": "Independent seed-testing laboratory: germination, purity, moisture and vigour tests on seed samples from seed merchants, growers' co-operatives, plant breeders and private growers, with a signed certificate per sample, under an accreditation with annual surveillance visits. Seed health testing is a separate procedure (QP-09) and out of scope.",
        "size": "Not stated as a headcount. One reception desk (the Sample Reception Coordinator), three benches (purity; germination; moisture and vigour) with their analysts, a Laboratory Supervisor (a role in the SOP, never named on the call), a Laboratory Manager, a Quality Manager and a Laboratory Director. About 9,000 samples a year by the procedure, 'ninety-two hundred, something like that' last year by the operator, with about 2,000 a year more from October under a new co-operative contract; peak September to January, over 80 samples a day in the peak.",
        "locations": "One laboratory building, never named beyond 'the building'; samples arrive by courier, post or hand between 08:00 and 16:00. Speech is British ('lorry', 'biro', 'dobbed'); no time zone is stated.",
        "current_tools": [
            "The sample register: a spreadsheet kept by the Sample Reception Coordinator, held on a shared drive. It has been corrupted twice, so a paper day book is written first and typed up after; the day book is not in the procedure.",
            "The results database: the validated system of record for results, from which certificate numbers are issued; the analyst enters results into it from the bench sheet; the accreditation assessor has seen it; it must stay.",
            "The certificate template: a word-processing document the coordinator types each certificate into. The results are re-typed from the results database and checked against it twice before printing.",
            "Paper: the test request (QF-03), the re-test request (QF-12), the bench sheet, the bench allocation sheet (in practice the previous day's register printed with the bench written on in biro) and the day book.",
            "No work management platform and no monday account evidenced; the Quality Manager 'has got a login to something from her last place, I think'.",
        ],
    }
    key["attendees"] = [
        {"name": "Rosalind Okonjo", "role": "Sample Reception Coordinator: receives, registers, labels and stores samples, fields submitter enquiries, prepares certificates for signature. Runs reception day to day and is the only named client speaker on the call. Does not buy ('I don't buy things') and books the next meeting on the Quality Manager's instruction.", "side": "client", "decision_role": "end user (the operator)"},
        {"name": "Speaker 2", "role": "An unlabelled client voice at reception asking for a courier signature, under the export's placeholder label; never named beyond the vocative 'Ros' it uses, not on any roster.", "side": "client", "decision_role": "unknown"},
        {"name": "Consultant", "role": "monday.com consultant who received the three documents from the Quality Manager and asked to hear the process from the person who runs it", "side": "consultant", "decision_role": "not applicable"},
    ]
    key["expected_monday_products"] = [
        {"kind": "core", "why": "monday Work Management for sample tracking: one register that reception, the benches and the Laboratory Manager all see (W-1), a status per sample from receipt to certificate (W-2), a priority flag visible to every bench with its approval mechanism held open until the 9th (W-3 against QP-07 section 4.2 against the call), a daily list per bench (W-8), turnaround measured against QP-07 section 6.5 (W-6), a certificate prepared as a draft for signature from recorded results (W-5, under the signatory rule of section 6.4), re-test requests raised on screen with the authorisation number carried to the bench sheet (W-7), and a monthly view for the Director (W-9, W-10). The results database stays the system of record for results (W-4) and is read, never replaced. Traces to P1 (status and priority invisible) and P2 (results transcribed three times). No CRM: submitters are a name on the sample today and tracking them as accounts is a question. No Service: no request desk. Dev is out of v1 in any case. Tier unknown and no account, so nothing tier-dependent is designed before the account is known."},
    ]

    RUB = []
    RUB.append(row("R1 Current state mapped", "met", [
        D("Each sample is given the next sample number in sequence and is entered in the sample register with the submitter, the crop and variety, the lot reference, the tests requested and the date of receipt.", "QP-07 section 3.2"),
        D("Each morning the Laboratory Supervisor takes the samples received on the previous working day from the receipt store and allocates them to the benches in order of receipt.", "QP-07 section 4.1"),
        D("On completion of the test, the analyst enters the results from the bench sheet into the results database and signs the bench sheet.", "QP-07 section 5.3"),
        D("The results are transcribed onto the certificate from the results database and are checked against the database before the certificate is printed.", "QP-07 section 6.3"),
        D("Log in sample register", "figure 1 p.1"),
        Q(7, "In the register. Which is a spreadsheet."),
        Q(11, "She prints it. Prints the previous day. That's the allocation sheet, basically, she writes the bench on the printout."),
        Q(9, "A book. A paper book. It's not in the procedure, I know it's not in the procedure."),
        Q(19, "It's two hours a day, some days. Most days. Just the walking and the ringing back."),
    ], "Met-with-residual from the documents alone (document-only pass) and Met with the call. The current-state picture is built from QP-07 sections 3 to 7 and the figure's twelve documented rows, all [Q/doc]: the SOP at the attributed tier because its author is known from the front page and the core metadata, the figure one step below. Elements: the process end to end (SOP), the tools and their lack of connections (sections 2.1, 5.3, 6.3), who touches it (roles in the SOP, names on the call), what monday does today (nothing: no platform is named anywhere), and time on their own process, which no document states and which is the document-only residual routed to the operator; the call closes it (two hours a day walking and ringing at %s, ten to fifteen minutes a certificate at %s). The call adds the lived version beside each documented step: the register is a spreadsheet plus a paper day book, the allocation sheet is a printout with biro, the priority approval does not happen (kept as a conflict, not overwritten), the re-test authorisation does. The write-up's sentences appear nowhere in this section." % (T(19), T(53)), True, Q(4, "Let's start at the door, then. A box arrives. What happens?")))
    RUB.append(row("R2 Pain made concrete", "met", [
        Q(33, "But germination's a seven-day test and nobody on germination knew it was urgent, so it went in the normal queue, and it came out the Thursday after."),
        Q(33, "They'd sown it on the Saturday. Untested. And then they rang to tell us."),
        Q(49, "A germination went out as sixty-eight instead of eighty-six. Transposed."),
        D("We cannot see where a sample is without going to the bench or ringing.", "write-up p.1 section 1"),
    ], "Partial document-only: the write-up states the problems in general terms and nothing is concrete, and the SOP by its nature describes the intended process, not its failures. Met with the call: P1 excavated (Stated, Concrete, Workaround all Met) on the September trial lot that was sown untested, P2 excavated on the transposed germination result and the reissue.", True, Q(32, "Priority. Has the priority thing ever actually gone wrong?")))
    RUB.append(row("R3 Why now", "met-with-residual", [
        Q(37, "The co-op, the Harrowfield growers, they've signed with us from October. Next week's the first lorry, actually. It's about two thousand samples a year on top."),
        Q(41, "We had a finding at the surveillance visit in May about the register, because the assessor asked me to show where a sample was and I had to go and find it."),
        Q(41, "So that's a finding, and it has to be closed before the next visit."),
        Q(43, "March, I think. Annelise would know. It's a year, roughly."),
    ], "Missing document-only: no document states a change, a trigger or a clock; the SOP's 'Review due: March 2027' is a document-control date, not a client clock, and the write-up carries no date. With the call: a client-side change (the co-operative contract adding about two thousand samples a year from October, first lorry next week) and a client-side trigger (the audit finding in May) are first-hand from the operator, so the criterion is Met on change plus trigger. The clock is hedged ('March, I think') and belongs to the Quality Manager, so it is the residual and becomes a gap question for the 9th instead of a one-word grade. Nothing our side supplied: the Consultant asked and named no date.", True, Q(40, "And is there anything else that made Annelise write the what-we-need notes now rather than last year?")))
    RUB.append(row("R4 Bleed number", "partial", [
        Q(19, "It's two hours a day, some days. Most days. Just the walking and the ringing back."),
        Q(53, "Ten minutes? Fifteen if it's a multi-test. And it's, what, thirty a day in the season."),
        D("The laboratory receives approximately 9,000 samples a year.", "QP-07 section 3.5"),
        Q(55, "I don't know. That's a Marguerite question. I don't want to guess at their time, they'd be cross with me."),
    ], "Missing document-only, with the scale section filled from QP-07 section 3.5 (about 9,000 samples a year, peak September to January, over 80 a day in the peak) as a client figure with the document as its source, and the missing multiplier named: time per sample handled and a loaded rate. With the call: effort-quantified, rate pending. The operator's own time is a client figure with the call as its source (two hours a day walking and ringing; ten to fifteen minutes a certificate at thirty a day in the season); no rate exists and the bench side is a Laboratory Manager question, so the cost criterion cannot exceed Partial. The September incident carries no figure ('I don't know what it cost') and none is invented; the transposed certificate is an incident count, not a rate.", True, Q(18, "How much of your day is that?")))
    RUB.append(row("R5 Upside number", "not-obtainable", [
        Q(59, "Turn away? I wouldn't know. That's Cormac. He'd know what we've lost, if we've lost anything. I just know who rings."),
    ], "Not obtainable from this room. Asked once; the operator routes it to the Laboratory Director, who attended nothing and appears in the documents only as the approver of the procedure. Missing document-only; no volume or value is stated anywhere and none is invented. Routes to a room with the Laboratory Director, not to the same question again.", True, Q(58, "Is there work you turn away, or lose, because of the turnaround?")))
    RUB.append(row("R6 Desired outcome", "met-with-residual", [
        D("The status of every sample visible at each stage, from receipt to certificate", "write-up p.1 section 2, W-2"),
        D("The certificate prepared from recorded results without re-typing, ready to sign.", "write-up p.1 section 2, W-5"),
        D("Turnaround measured for every sample against the targets in QP-07 section 6.5", "write-up p.1 section 2, W-6"),
        Q(61, "I don't walk. [laughs] I look at a screen and I can tell Marlowe's where their sample is without getting up."),
        Q(63, "Turnaround, probably. He gets the complaints. And the audit finding closed, Annelise would say that."),
    ], "Met-with-residual in both passes. The write-up's ten wants (W-1 to W-10) are the client's own statement of what solved looks like, cited [Q/doc] at the tier 'the client's document' because the author is unknown; they feed the requirement trace and the solution, never the current-state picture. The residual is the second element, what leadership would count as a win: no document states it, and on the call the operator guesses at the Director's and the Quality Manager's win ('Turnaround, probably', 'Annelise would say that'), which is her view of theirs and not their statement. The residual is a gap question routed to the Laboratory Director through the Quality Manager. The call adds the operator's own day-to-day version.", True, Q(60, "All right. If this worked, what's different in a normal week for you?")))
    RUB.append(row("R7 Decision process mapped", "partial", [
        Q(65, "Annelise owns the procedure, so it's her project. But anything that costs money is Cormac. I don't know what the number is where it becomes Cormac."),
        Q(81, "I'll get them in the room. Cormac I can't promise."),
    ], "Missing document-only: 'Approved by: Cormac Delahunty, Laboratory Director' on the SOP's front page is document control, not a decision process for buying anything, and the write-up names nobody. With the call: the operator names the owner (the Quality Manager) and the payer (the Laboratory Director) with no threshold, no process and no timing, from below both of them; the gate-holder's own words are not obtainable from this room, and the approver is invited through the Quality Manager. Partial; the delegation graph has two nodes and no gate condition.", True, Q(64, "Who decides on something like this, if it costs money?")))
    RUB.append(row("R8 Priority and timing", "partial", [
        Q(67, "Before the season's properly going, so, yesterday. [laughs] Realistically Annelise said before the visit. But that's her saying it, not me. Ask her."),
        Q(73, "If it just did the register and the where-is-it, that'd be most of it for me."),
    ], "Missing document-only: the SOP's review-due date is not a timing for this work and the write-up carries none. With the call: a priority (the register and the where-is-it first) from the operator, and a timing relayed from the Quality Manager ('before the visit') with the operator's own hedge, recorded as reported and not as the Quality Manager's statement; Partial until she says it herself on the 9th.", True, Q(66, "That's fine. When would this need to be in by?")))
    RUB.append(row("R9 Blockers surfaced", "met", [
        Q(69, "The analysts have got seed dust on their hands all day, they're not going to touch a screen. Tobiah will, the others won't."),
        Q(69, "Whatever this is, it can't be the place results live."),
        D("The results database cannot be replaced or altered.", "write-up p.2 section 3"),
        D("Nothing may issue a certificate without a signature.", "write-up p.2 section 3"),
    ], "Partial document-only: the write-up's constraints (the results database stays, a signature on every certificate, no double entry at the bench, retention, confidentiality) are design constraints stated in writing, not what could stop the work going ahead, and nobody could be asked. With the call: the bench adoption blocker and the system-of-record constraint in the operator's words make it Met.", True, Q(68, "I will. What could get in the way of it?")))
    RUB.append(row("R10 Next step committed", "met", [
        Q(79, "Annelise said to book it through me. Friday the ninth? Two o'clock? Marguerite does allocation in the morning so afternoons are better."),
        Q(80, "Friday the ninth at two, then. I'll send the invite to you today, and you'll get Annelise and Marguerite in the room?"),
        Q(81, "I'll get them in the room. Cormac I can't promise."),
    ], "Missing document-only: a document commits nobody to a meeting. With the call, a discovery call, the strict form applies and is met: a date (Friday 9 October), a time (two o'clock) and owners (the Consultant sends the invite today; the operator brings the Quality Manager and the Laboratory Manager, on the Quality Manager's own instruction to book through her). The Director's attendance is a to-do through the Quality Manager, not part of the criterion. The Consultant's line is the one admissible piece of our-side next-step evidence.", True, Q(78, "When could we get the three of you together? You, Annelise and Marguerite.")))
    RUB.append(row("R11 Solution confirmed", "missing", [], "No demo has happened; nothing has been shown or described as a mechanism to the owner. Missing in both passes; blocks only the v1.0 sign-off gate.", False))
    RUB.append(row("R12 Scope agreed verbally", "partial", [
        Q(73, "If it just did the register and the where-is-it, that'd be most of it for me. The certificate thing would be lovely. Annelise will want the turnaround numbers, she's asked for them twice."),
    ], "Missing document-only: scope cannot be agreed verbally by a document, and the write-up's list is a wish list of ten, not a short agreement. With the call: the operator accepts the Consultant's six-part playback (%s) in her own words and adds a relayed want; she is neither the owner nor the approver, so Partial until the 9th." % T(72), True, Q(72, "Okay. Let me play back what I think the first version is, and you tell me where I've got it wrong.")))
    # P1: a sample's status and its priority are invisible
    RUB.append(row("P1 Stated", "met", [
        D("We cannot see where a sample is without going to the bench or ringing.", "write-up p.1 section 1"),
        Q(17, "Then I walk. [laughs] Honestly. I walk to purity, I walk to germination, I ask whoever's there, and if it's in the germinator I have to find the bench sheet, and the bench sheet's wherever Tobiah left it."),
        Q(21, "That box on the form? Nobody uses it."),
    ], "P1: nobody can see where a sample is or that it is urgent; reception walks the benches, and a priority agreed on the phone reaches purity by word of mouth and germination not at all. Stated in writing (document-only: Met from the write-up's problem statement, tier 'the client's document') and again on the call.", True, Q(16, "So a submitter rings and asks where their sample is.")))
    RUB.append(row("P1 Concrete", "met", [
        Q(33, "they rang on the Monday and said it was urgent, sowing that weekend, and I did my usual, top of the pile, told purity"),
        Q(33, "The certificate went out on the eleventh day. They'd sown it on the Saturday. Untested."),
    ], "September, the first trial lot from the co-operative: urgent on the Monday, purity done that day, germination in the normal queue, certificate on day eleven, seed sown untested on the Saturday, the Quality Manager writing to them. Missing document-only.", True, Q(32, "Priority. Has the priority thing ever actually gone wrong?")))
    RUB.append(row("P1 Workaround", "met", [
        Q(17, "Or I ring, if I can't leave the desk, and then I'm waiting for someone to ring me back."),
        Q(21, "I put it at the top of the pile and I tell whoever's on purity. Marguerite finds out when she sees it on the list. If she looks."),
        D("Where a submitter enquires about the progress of a sample, the Sample Reception Coordinator establishes its status with the bench and responds to the submitter on the same working day.", "QP-07 section 3.4"),
    ], "Today: walking or ringing the benches, and a priority passed by word of mouth to one bench. Why it will not do: two hours a day, and the September lot. The SOP documents the walk as the procedure (section 3.4), which is why the document-only grade is Partial: the what without the why-not.", True, Q(16, "So a submitter rings and asks where their sample is.")))
    RUB.append(row("P1 Reach", "partial", [
        Q(35, "Annelise had to write to them. I don't know if it cost money. It cost, you know. Them not trusting us in the first month of a contract we'd only just won."),
        Q(63, "Turnaround, probably. He gets the complaints."),
    ], "The submitter, the Quality Manager who writes the apology, the Director who gets the complaints and the germination bench are touched; nobody was asked who else is, and the bench's own view is absent. Missing document-only.", False))
    RUB.append(row("P1 Cost inputs", "met", [
        Q(19, "It's two hours a day, some days. Most days. Just the walking and the ringing back."),
        Q(19, "In the season it's more, but then everything's more in the season."),
    ], "The operator's own time, from the person who does the work: two hours a day most days, more in the season; a client figure with the call as its source. Ask-only, and asked. The rate is an engagement-level gap (R4), not a missing input for this pain. Missing document-only.", True, Q(18, "How much of your day is that?")))
    RUB.append(row("P1 Trajectory", "partial", [
        Q(37, "It's about two thousand samples a year on top."),
        Q(39, "-- ninety-two hundred, something like that, last year."),
        Q(19, "In the season it's more, but then everything's more in the season."),
    ], "Volume rises: about two thousand samples a year more from October on about nine thousand, arriving in the peak, with the first lorry next week, and the walking grows with the season; nobody says what that does to the two hours, so Partial. The two halves of the figure sit either side of the Consultant's interjection and are cited from their own turns (intake.rejoined_sentences). Missing document-only.", True, Q(36, "Tell me about the contract, because that sounds like part of why now.")))
    # P2: results transcribed three times; certificates typed and checked by hand
    RUB.append(row("P2 Stated", "met", [
        D("Every result is written three times: bench sheet, results database, certificate.", "write-up p.1 section 1"),
        Q(45, "Three times. And the certificate is me, typing, from the database into the template. And then checking it against the database again, because I've typed it."),
    ], "P2: every result is written three times and the certificate is typed by hand from the database, then checked twice. Met from the write-up document-only, restated on the call.", True, Q(44, "The procedure has results going onto the bench sheet, then into the results database, then onto the certificate. Three times.")))
    RUB.append(row("P2 Concrete", "met", [
        Q(49, "A germination went out as sixty-eight instead of eighty-six. Transposed. In, um, June? The merchant rang, we reissued."),
        Q(51, "Not often. Twice this year that I know of."),
    ], "A transposed germination result on an issued certificate in June, reissued under the Laboratory Manager's signature; twice this year that the operator knows of. Missing document-only.", True, Q(48, "Has the typing ever gone wrong?")))
    RUB.append(row("P2 Workaround", "met", [
        Q(51, "It's the checking that takes the time, not the mistakes. Every certificate, I check every number twice."),
        D("The Sample Reception Coordinator prepares the certificate from the certificate template.", "QP-07 section 6.3"),
    ], "Today: the double check of every number against the database, which the SOP prescribes (section 6.3). Why it will not do: ten to fifteen minutes a certificate, thirty a day in the season, and errors still get through. Partial document-only: the procedure, not its cost.", True, Q(52, "How long is that, per certificate?")))
    RUB.append(row("P2 Reach", "partial", [
        Q(49, "Marguerite had to sign the reissue and she wasn't happy."),
    ], "The Laboratory Manager signing reissues and the merchant; the bench analysts' share is unknown. Not asked. Missing document-only.", False))
    RUB.append(row("P2 Cost inputs", "met-with-residual", [
        Q(53, "Ten minutes? Fifteen if it's a multi-test. And it's, what, thirty a day in the season."),
        Q(55, "That's a Marguerite question."),
    ], "Two elements. Reception's half is a client figure from the person who does it (ten to fifteen minutes a certificate, thirty a day in the season). The bench's half, the analysts' entry time, is the residual: not obtainable from this room, refused rather than guessed by the operator, and routed to the Laboratory Manager as a gap question. No rate; that is R4's gap. Missing document-only.", True, Q(54, "And the bench side, the time the analysts spend entering --")))
    RUB.append(row("P2 Trajectory", "partial", [
        Q(53, "Less now. Well, not less now, it's the season now."),
    ], "Volume rises in the season and the co-operative adds about two thousand samples a year, but nobody says what the typing looks like with that, and the question was not asked for this pain. Missing document-only.", False))
    key["rubric"] = RUB

    key["pains"] = [
        D("We cannot see where a sample is without going to the bench or ringing.", "write-up p.1 section 1") | {"theme": "P1 A sample's status is invisible without walking or ringing (the client's document)"},
        Q(17, "Then I walk. [laughs] Honestly.") | {"theme": "P1 Reception walks the benches to answer a submitter"},
        Q(21, "That box on the form? Nobody uses it.") | {"theme": "P1 The documented priority approval is not used; priority travels by word of mouth"},
        Q(33, "nobody on germination knew it was urgent, so it went in the normal queue") | {"theme": "P1 A priority reaches one bench and not the next"},
        Q(57, "But by then it's late. We find out it's late when they ring.") | {"theme": "P1 Turnaround is measured after the fact, from the register's dates"},
        D("Every result is written three times: bench sheet, results database, certificate.", "write-up p.1 section 1") | {"theme": "P2 Results transcribed three times (the client's document)"},
        Q(45, "And the certificate is me, typing, from the database into the template.") | {"theme": "P2 The certificate is typed by hand"},
        Q(51, "It's the checking that takes the time, not the mistakes.") | {"theme": "P2 Every number checked twice"},
        Q(9, "The spreadsheet's been corrupted twice, once in the season, and I lost a day and a half of receipts") | {"theme": "P3 The register file is fragile, so a paper day book is kept first (stated, not graded)"},
        Q(41, "the assessor asked me to show where a sample was and I had to go and find it") | {"theme": "P4 The register's retrieval drew an audit finding (stated, not graded; the why-now trigger)"},
    ]
    key["numbers"] = {
        "bleed": {
            "value": "Effort-quantified, rate pending. Reception: about two hours a day most days walking and ringing (the operator's own figure, a client figure with the call as its source), and ten to fifteen minutes a certificate at about thirty a day in the season. Bench time: not obtainable from this room, the Laboratory Manager's. No loaded rate exists and none is invented; nothing is multiplied. The September incident has no figure ('I don't know what it cost') and is not priced. Scale, from QP-07 section 3.5, a client figure with the document as its source: about 9,000 samples a year, peak September to January, over 80 a day in the peak; the operator's 'ninety-two hundred, something like that' agrees within rounding and is not a conflict. Missing multiplier: a loaded rate for reception and the bench's time per sample. Document-only the bleed is Missing and the scale section is filled.",
            "quote": "It's two hours a day, some days. Most days. Just the walking and the ringing back.",
            "status": "partial",
        },
        "upside": {
            "value": "Not obtainable from this room: the operator routes lost or turned-away work to the Laboratory Director, who attended nothing. The write-up states no value and the SOP none. Nothing is invented from 'he gets the complaints' or from the lost trust of the co-operative, which is a why-now trigger and not an upside.",
            "quote": None,
            "status": "missing",
        },
    }
    key["vocabulary"] = [
        {"their_term": "sample", "meaning": "One quantity of seed submitted for testing, identified by a sample number (QP-07 section 2.1); the unit everything hangs off", "likely_monday_object": "item on a Samples board, one line per sample, the sample number as the item name"},
        {"their_term": "submitter", "meaning": "The customer who sends the sample and receives the certificate: a merchant, a co-operative, a breeder or a private grower", "likely_monday_object": "a text or dropdown column on the sample for the first version; an Accounts question if submitters are to be tracked in their own right (native CRM boards if yes)"},
        {"their_term": "test request (QF-03)", "meaning": "The paper form that comes with the sample and states the tests required; stamped with the sample number", "likely_monday_object": "columns on the sample: tests requested, priority requested, lot reference; the paper form stays"},
        {"their_term": "sample register", "meaning": "The spreadsheet in which every sample is logged from receipt to certificate; the day book is written first", "likely_monday_object": "the Samples board itself, with the register's fields as columns"},
        {"their_term": "day book", "meaning": "The paper book reception writes receipts in first because the spreadsheet has been corrupted twice; not in the procedure", "likely_monday_object": "no object; it goes away only when the operator trusts the board, which is a question for her"},
        {"their_term": "bench", "meaning": "The purity bench, the germination bench or the moisture and vigour bench, each a team of analysts; 'purity' and 'germination' in speech are benches, not people", "likely_monday_object": "a status or dropdown column for the allocated bench, and a view per bench; never a People column"},
        {"their_term": "bench sheet", "meaning": "The paper record of observations and results for one sample, signed by the analyst and initialled by the checker", "likely_monday_object": "no object in the first version; a date column for results entered and one for the second-analyst check"},
        {"their_term": "allocation sheet", "meaning": "QP-07's bench allocation sheet, in practice the previous day's register printed with the bench written on in biro", "likely_monday_object": "the daily view per bench (W-8), which replaces the printout"},
        {"their_term": "Laboratory Supervisor / Laboratory Manager", "meaning": "Two titles in QP-07: the Supervisor allocates (4.1) and is told of outages (5.4); the Manager approves priorities (4.2), authorises re-tests (4.3) and signs (6.4). On the call one person, Marguerite, does the allocation and the signing, and no Supervisor is named; whether the two titles are one person or a vacant role is a question", "likely_monday_object": "an owner on the allocation view and an approver on the priority and re-test steps; confirm before naming either"},
        {"their_term": "results database", "meaning": "The validated system of record for results, from which certificate numbers come; must stay", "likely_monday_object": "not modelled; a read from it, in a form to be agreed, feeds the certificate draft"},
        {"their_term": "certificate", "meaning": "The signed report of results sent to the submitter; prepared by reception, signed by the Laboratory Manager or the Quality Manager", "likely_monday_object": "a status stage on the sample plus a document draft for signature; never issued automatically"},
        {"their_term": "priority request", "meaning": "A submitter's request to be tested ahead of the queue; approved by the Laboratory Manager on paper by the procedure, passed to one bench by word of mouth in practice", "likely_monday_object": "a priority column on the sample with a notification; whether an approval step sits behind it is the open conflict"},
        {"their_term": "re-test (QF-12)", "meaning": "A repeat test authorised by the Laboratory Manager on a form; the one approval step the call confirms is used", "likely_monday_object": "a re-test status with the authorisation number as a column (W-7); the paper form stays until the Laboratory Manager says otherwise"},
        {"their_term": "the season", "meaning": "The peak receipt period, September to January, over 80 samples a day", "likely_monday_object": "no object; a fact for the SOP and for the build's volume assumptions"},
        {"their_term": "multi-test", "meaning": "A sample with more than one test requested, which takes longer to certify", "likely_monday_object": "the tests-requested column holding several values; no separate object"},
        {"their_term": "surveillance visit", "meaning": "The accreditation body's annual audit; the May visit produced a finding about the register; the next is 'March, I think'", "likely_monday_object": "no object; the why-now trigger and the clock question"},
    ]
    key["entities_and_workflows"] = [
        "Sample receipt (QP-07 section 3): a consignment arrives by courier, post or hand; the Sample Reception Coordinator checks it against the test request (QF-03), gives it the next sample number, enters it in the register (lived: the day book first, then the spreadsheet), stamps the form into the tray and labels the container into the receipt store (a locked cupboard with a sealed section for moisture samples).",
        "Allocation (section 4.1): each morning the Laboratory Supervisor allocates the previous day's samples to the benches in order of receipt on the bench allocation sheet; lived: the Laboratory Manager prints the previous day's register and writes the bench on it in biro.",
        "Priority requests (section 4.2): documented as approved by the Laboratory Manager before allocation, initials and date on the form and in the register, then allocated at the head of the next allocation; lived: nobody uses the box, reception puts the sample at the top of the pile and tells whoever is on purity, the Laboratory Manager finds out from the list if she looks. Kept as the conflict.",
        "Re-tests (section 4.3): a re-test starts only on a re-test request (QF-12) authorised by the Laboratory Manager, its number recorded on the bench sheet; lived: used, the bench will not start without the form, checked against the forms monthly.",
        "Testing (section 5): the analyst tests by the methods manual, records on the bench sheet, enters results into the results database on completion and signs the sheet; if the database is down, results wait on the sheet.",
        "Review (sections 6.1 and 6.2): a second analyst checks the database against the bench sheet and initials it; a result outside tolerance goes to a re-test under section 4.3.",
        "Certification (sections 6.3 and 6.4): reception prepares the certificate from the template by transcribing results from the database and checking them; the Laboratory Manager or the Quality Manager signs; the issue date goes in the register. Lived: every number checked twice, ten to fifteen minutes each, thirty a day in the season; a transposed result reissued in June.",
        "Turnaround (section 6.5): 21 days for germination and vigour, 10 for purity and moisture, 7 for an approved priority; lived: not measured in progress, the Quality Manager counts monthly from the register's dates, lateness is learned from the submitter's call.",
        "Enquiries (section 3.4): reception establishes a sample's status with the bench and answers the same day; lived: walking the benches or ringing and waiting, about two hours a day.",
        "Records (section 7): bench sheets, requests and certificate copies kept six years; the register backed up weekly.",
        "The figure (QP-07-F1): twelve nodes from Sample received to Certificate sent to submitter, with Priority requested? (Yes to Laboratory Manager approves, No to Allocate to bench) and Within tolerance? (Yes to Second-analyst check, No to Re-test authorised (QF-12), which loops back to the bench).",
        "Customers named on the call: a seed merchant ('Marlowe's', who rings about lorries and who rang about the transposed result) and the Harrowfield growers' co-operative ('the co-op', signed from October, about two thousand samples a year, the September trial lot).",
    ]
    key["integrations_mentioned"] = [
        "The results database: the validated system of record for results; results are entered there by the analysts and must stay there; the certificate draft needs a read from it in a form to be agreed (an export, a report or read access), never a write, and never a copy of the results into the platform as the record.",
        "The sample register spreadsheet: replaced by the board; whether its history is migrated, and from which date, is a question; the paper day book stops only when the operator trusts the board.",
        "The certificate template: a word-processing document; the first version prepares a draft for signature from the recorded results, and the signed certificate still goes to the submitter as it does today.",
        "Paper forms QF-03 and QF-12 and the bench sheet: stay; the board carries their numbers and dates.",
        "Nothing else: no accounts system (out of scope by the write-up), no messaging tool named, no monday account evidenced.",
    ]
    key["compliance_or_security_signals"] = [
        "The laboratory is accredited: annual surveillance visits by the accreditation body; a finding in May about the register's retrieval must be closed before the next visit ('March, I think').",
        "The results database is validated for the accreditation and the assessor has seen it; it cannot be replaced or altered (write-up section 3; call %s)." % T(69),
        "Certificates must be signed by an authorised signatory, the Laboratory Manager or the Quality Manager (QP-07 section 6.4); nothing may issue a certificate without a signature (write-up section 3); reception may not sign.",
        "Records retained six years: bench sheets, test requests, re-test requests and certificate copies (QP-07 section 7.1; write-up section 3).",
        "Submitters' names, samples and results are confidential to the submitter (write-up section 3): no seed data with real submitters, no results in a demo.",
        "The client's own documents are under the same leak-lint, neutral-naming and retention rules as transcripts; the open retention question covers them [A11-3].",
    ]
    key["objections"] = [
        Q(69, "The analysts have got seed dust on their hands all day, they're not going to touch a screen.") | {"type": "Team won't adopt it (embedded: stated as a fact about today by the person who works beside them; client-attributed cause: seed dust and no keyboard at the bench)"},
        Q(69, "Whatever this is, it can't be the place results live.") | {"type": "Outside the map: system-of-record constraint (the validated results database stays; a design constraint, not a deal objection)"},
        Q(81, "Cormac I can't promise.") | {"type": "Must check with someone (the approver was not on the call and is reached through the Quality Manager)"},
        Q(67, "But that's her saying it, not me. Ask her.") | {"type": "Must check with someone (timing belongs to the Quality Manager)"},
        Q(83, "Don't make it sound like I've dobbed anyone in.") | {"type": "Outside the map: fear of exposure (the operator asks that the document-versus-practice gap be raised as a question about the procedure, not as a report about her; handled in the write-up and the callback, kept internal)"},
        Q(77, "[laughs] Good luck.") | {"type": "Outside the map: scepticism that the managers will settle the approval question (kept internal)"},
        Q(25, "I'm not going to say she doesn't know.") | {"type": "Outside the map: loyalty hedge (the operator will not characterise the Quality Manager's knowledge; the conflict is raised with the Quality Manager directly)"},
    ]
    key["commitments_and_next_steps"] = [
        Q(80, "Friday the ninth at two, then. I'll send the invite to you today, and you'll get Annelise and Marguerite in the room?") | {"what": "Meeting with the Quality Manager and the Laboratory Manager, the operator present, to walk the lived process against QP-07 and settle the priority-approval question", "owner": "Consultant (hosts, sends the invite); Rosalind brings Annelise and Marguerite", "date": "%s 14:00 (Friday the ninth; month and year inferred from the contract 'from October', 'next week's the first lorry' and the September incident)" % MEET},
        Q(81, "I'll get them in the room.") | {"what": "Get the Quality Manager and the Laboratory Manager to attend on the 9th", "owner": "Rosalind Okonjo", "date": "before %s" % MEET},
        Q(82, "I'd rather ask Cormac through Annelise anyway.") | {"what": "Invite the Laboratory Director through the Quality Manager rather than through the operator", "owner": "Consultant", "date": "with the invite, day of the call"},
        Q(82, "Before then I'll write up what you've told me, and where it's different from the procedure I'll put it as a question for Annelise, not as a finding.") | {"what": "Write up the lived process beside QP-07 with each difference phrased as a question for the Quality Manager", "owner": "Consultant", "date": "before %s" % MEET},
        Q(26, "That's fair, and I'll ask her, and I'll ask it as a question, not as a finding.") | {"what": "Ask the Quality Manager whether the priority approval in section 4.2 is used, as a question (the callback)", "owner": "Consultant", "date": MEET},
        Q(56, "Fair enough, I'll take that to Marguerite rather than guess.") | {"what": "Get the bench analysts' time on results entry from the Laboratory Manager", "owner": "Consultant, with Marguerite", "date": MEET},
        Q(44, "Okay, I'll ask her that too.") | {"what": "Confirm the date of the next surveillance visit with the Quality Manager (the clock)", "owner": "Consultant", "date": MEET},
        Q(76, "What it should do about the approval is what I want to ask Annelise and Marguerite, because the procedure says one thing and you've told me another, and I don't want to build either without them in the room.") | {"what": "Build neither version of the priority approval until the Quality Manager and the Laboratory Manager have settled it", "owner": "Consultant", "date": "%s, before any build" % MEET},
    ]
    key["traps"] = [
        "The core conflict. QP-07 section 4.2 says 'A priority request is approved by the Laboratory Manager before the sample is allocated.' At %s and %s the operator says 'That box on the form? Nobody uses it.' and 'It doesn't happen.' Keep both, with the document's section and the call's speaker and location, as kind conflict in open-questions.md with a conflict log entry; the current-state picture carries the lived version with the documented version beside it; it is offered as a callback for the 9th, phrased as procedure-versus-reception; it is never resolved by recency, never discarded, never a finding against the operator, and never a reason to distrust the rest of the SOP." % (T(21), T(23)),
        "The write-up's W-3 ('Priority requests approved by the Laboratory Manager on screen, not on the form') presupposes the documented step. It is desired state and joins the conflict block as the requirement that depends on the answer; it is not a third current-state source and does not make the document side 'two against one'.",
        "The write-up feeds the requirement trace only: its section 1 problem statements are the reasons for its wants and are admitted for P1 and P2 Stated, but no sentence of the write-up enters the current-state section, which the SOP and the figure fill.",
        "The write-up has no author, no date and no status: three unknown fields, no author invented from the SOP's, no date inferred from its references to QP-07, and 'Notes for the systems review' is a subtitle, not a status. The call attributes it to the Quality Manager ('the notes she called what we need', 'made Annelise write the what-we-need notes'); that is a spoken attribution recorded beside the field, and the field itself stays unknown because the document does not say. Its extracts sit at the tier 'the client's document', one step below the SOP's.",
        "The figure has no metadata: author, date and status unknown. QP-07 section 1.3 names it as issued with the procedure; that is an inference [I] for its place in the sequence and is never written into the figure's own fields.",
        "The SOP's date is 11 March 2026, from the front page and dcterms:modified, which agree. dcterms:created (24 February 2026) is a drafting date; the revision history's 2024 and 2023 dates belong to versions 3.1 and 3.0; 'Review due: March 2027' is document control and is not a client clock for R3 or R8.",
        "'Approved by: Cormac Delahunty, Laboratory Director' on the front page is document control, not a decision process: R7 stays Missing document-only. The call's 'anything that costs money is Cormac' is the decision-process evidence, and it is Partial.",
        "A document carries no type header: the document-only pass proposes no call type, demotes nothing to advisory, and grades every criterion against its plain definition; the doors read the strand's kind and output class, which the user set.",
        "'approximately 9,000 samples a year' (QP-07 section 3.5) and 'ninety-two hundred, something like that, last year' (%s) agree within rounding and are not a conflict; the SOP's figure is a client figure with the document as its source, the operator's is hedged and attributed by her to the procedure, so it is second-hand and the document is the source." % T(39),
        "The day book (%s) is absent from the SOP and present on the call: an addition to the current-state picture, not a conflict; likewise the allocation sheet being a printout with biro (%s) is lived detail consistent with section 4.1." % (T(9), T(11)),
        "QP-07 names a Laboratory Supervisor (sections 4.1, 5.4) and a Laboratory Manager (4.2, 4.3, 6.4). The call names Marguerite for the allocation and the signing and nobody as Supervisor. Do not merge the two titles into one person and do not invent a second person: record both titles, the observed behaviour, and a question for the 9th.",
        "The re-test authorisation (section 4.3) is used ('So that one's real.', %s): the priority conflict must not be generalised to every approval step, and the re-test form is a current-state fact to preserve, not a second conflict." % T(27),
        "The figure's 'No' exit from 'Within tolerance?' loops to 'Re-test authorised (QF-12)', and section 6.2 says the same; the two documents agree, so no document-versus-document conflict is raised.",
        "The September incident carries no figure: 'I don't know what it cost.' Nothing is priced from it; the reputational cost is recorded in the operator's words and the incident is P1 Concrete, not a bleed input.",
        "'It's two hours a day, some days. Most days.' is the operator's own time and a client figure with the call as its source; there is no rate, so the frame is effort-quantified, rate pending. No loaded rate is invented and nothing is multiplied.",
        "The bench analysts' time is not obtainable from this room ('That's a Marguerite question.'): route it to the Laboratory Manager rather than asking the operator again; the same for the upside, which routes to the Laboratory Director.",
        "Relayed reasons and timings ('Realistically Annelise said before the visit', 'Annelise will want the turnaround numbers') are reported by the operator and are not the Quality Manager's statements; R8 is Partial until she says it herself.",
        "'March, I think. Annelise would know.' is hedged: the clock is the residual on R3 (met-with-residual), not Met, and it is a gap question routed to the Quality Manager.",
        "The transposed certificate ('sixty-eight instead of eighty-six') is an incident, twice this year; it is P2 Concrete and not a defect rate, and the cost of P2 is the checking time, not the mistakes.",
        "'purity' and 'germination' are benches, not people: 'I tell whoever's on purity' and 'told purity' must not coerce an ordinary word into a name; the alias map lists them as benches.",
        "The 'Speaker 2' line (%s) is an export placeholder for an unresolved client voice; the vocative 'Ros' binds to Rosalind as the addressee, never as the speaker; the unit is unattributable, nothing is derived from it, and it is never bound to the Laboratory Manager, the Quality Manager or the analyst named on the call." % T(30),
        "The Consultant's interjection at %s ('On nine thousand, that's a fair chunk.') splits the operator's sentence: each half is cited from its own turn, a merged quote across our label is refused, and the interjection is non-evidence." % T(38),
        "The Consultant's answer at %s ('A flag that notifies someone is a normal thing for it to do.') is a claim about the platform: it goes to the claims store, unhedged, and is evidence of nothing." % T(76),
        "'Marlowe's' is a customer, a seed merchant, in the operator's possessive form; never a person and never an attendee. 'the co-op', 'the Harrowfield growers' and 'the co-operative' are one customer.",
        "No monday account: 'a login to something from her last place, I think' is hearsay about a login, not evidence of an account, a tier or a product. Tier unknown, no account, portfolio_expected false with the reason recorded, and the account question asked before anything tier-dependent is designed.",
        "No CRM is proposed: submitters are a name on the sample today; tracking them as accounts is a question, and if the answer is yes the native CRM boards are used, never a Submitters look-alike.",
        "The results database stays: never rebuild results inside the platform, never write to it, and the certificate is a draft for signature under section 6.4, never issued automatically.",
        "Turnaround targets (21, 10 and 7 days) come from QP-07 section 6.5, a client figure with the document as its source; W-6 measures against them; the plugin does not propose targets of its own.",
        "Dates: no file states the call's date. The call fits the last week of September 2026 (the contract 'from October', 'next week's the first lorry', the incident 'September', 'Friday the ninth' as 9 October 2026); the SOP is dated; the figure and the write-up are not.",
        "'Don't make it sound like I've dobbed anyone in.' governs the write-up and the callback: the gap is phrased as the procedure against reception, never as the operator's report; the remark and 'Good luck' stay internal.",
        "Order independence: taking the call first and the three documents after ends in the same record. Sequence comes from each input's date and internal evidence, never from arrival; the conflict block, the documented rows, the author, date and status fields and every grade are identical in both runs.",
        "The client's SOP is the starting point for ours: QP-07's sections and vocabulary are reused and the draft shows what changed; the client's own text is exempt from the copied-run lint rule, every other rule runs.",
        "The write-up's W-7 (re-tests on screen) is a want; the lived use of the paper re-test form is the current state; nothing removes the form before the Laboratory Manager says so.",
        "The operator's playback assent (%s) is R12 Partial, not Met: she is neither the owner nor the approver, and she adds a want relayed from the Quality Manager." % T(73),
        "Two hours a day and thirty certificates a day are the operator's; the per-pain cost checks (P1 Cost inputs Met, P2 Cost inputs met-with-residual) are reported apart from the engagement-level bleed (Partial, rate pending), and the scale section is filled in both passes.",
        "The documented rows keep the marker documented in both passes; the call adds a read-back state per row (confirmed, contradicted, not read back) and never changes the marker to spoken.",
    ]
    key["requested_changes"] = [
        {"type": "change", "description": "Pre-build requirement from the write-up (no build exists yet): the results database stays the system of record for results and is read, never replaced or written to.", "quote": "The results database stays the system of record for results."},
        {"type": "add", "description": "Pre-build requirement from the write-up: no certificate is issued without a signature, so the first version prepares a draft for signature and stops there.", "quote": "Nothing may issue a certificate without a signature."},
        {"type": "change", "description": "Pre-build requirement from the call: the bench analysts will not use a keyboard or a screen with seed in hand, so whatever marks a sample started, done or re-tested at the bench needs another mechanism, to be agreed with the Laboratory Manager.", "quote": "they're not going to touch a screen. Tobiah will, the others won't."},
        {"type": "add", "description": "Pre-build requirement from the call: the priority flag must reach every bench the same day, with the approval behind it left open until the 9th.", "quote": "And the priority thing is visible, so when I say it's urgent, germination knows it's urgent, not just purity."},
        {"type": "add", "description": "Pre-build requirement relayed from the Quality Manager: turnaround numbers against QP-07 section 6.5, to be confirmed with her.", "quote": "Annelise will want the turnaround numbers, she's asked for them twice."},
    ]
    key["should_plugin_propose_a_build"] = True
    key["expected_questions_before_building"] = [
        "The priority approval: QP-07 section 4.2 says the Laboratory Manager approves before allocation, W-3 wants that approval on screen, and reception says the step is not used. Which should the first version do, who owns the flag, and does an approval step exist at all? (Annelise and Marguerite on the 9th; the callback)",
        "The results database: what can be read from it and how (an export, a report, read access), so a certificate draft can be prepared from recorded results without anyone re-typing and without touching the validated system? Who grants it? (Annelise)",
        "Signature: is a draft certificate prepared for the Laboratory Manager's or the Quality Manager's signature acceptable under section 6.4 and to the accreditation body? (Annelise, Marguerite)",
        "The bench: how does an analyst mark a sample started, done or re-tested without a keyboard in hand: a scan, a shared screen at the bench, the supervisor's morning sheet, or the Laboratory Manager alone? And how much of the analysts' time does results entry take? (Marguerite)",
        "Roles: is the Laboratory Supervisor of sections 4.1 and 5.4 the same person as the Laboratory Manager, who does the allocation in practice, or a role that is vacant? Who should own the allocation view and the approvals? (Annelise, Marguerite)",
        "Decision process: at what threshold does spend go to the Laboratory Director, what does he need to see, what would he count as a win, and does he want to be on the 9th or after? (Annelise, then Cormac)",
        "Why now and the clock: the wording of the audit finding, the date of the next surveillance visit, and whether closing the finding is the deadline. (Annelise)",
        "The account: is there a monday account (the Quality Manager's login from her last place is not one), who would administer it, which tier and how many seats? (Annelise)",
        "Submitters: are merchants, co-operatives and breeders to be tracked as accounts with contacts (a CRM question, native boards if yes), or only as a name on the sample? (Annelise)",
        "The register: is the spreadsheet's history migrated, from which date, and does the paper day book stop once the operator trusts the board? (Rosalind, Annelise)",
    ]
    key["expected_verdict"] = {
        "verdict": "Nearly ready",
        "gates_met": [
            "Solution blueprint (R1 Met, R2 Met; the structure inventory's read-back is graded Partial and recorded in front of the gate: seven of the twelve documented rows were read back to the operator: five confirmed with lived detail, the priority decision acknowledged, and its approval exit contradicted into the conflict; the rest not read back)",
            "Build (no extra method gate; still needs the Consultant's approval at the approval stop, after the 9th has settled the approval question or it is carried as a listed open decision)",
            "First demo (v0.1): nothing extra needed",
        ],
        "gates_not_met": [
            "Pricing or proposal prep (R4 Partial: effort-quantified, rate pending; R7 Partial: owner and payer named, no threshold, the approver absent; R12 Partial: the operator's assent, not the owner's)",
            "v1.0 sign-off (R11 Missing: no demo has happened; R6 success criteria from the write-up are proposed, not agreed, and the leadership win is a residual)",
        ],
        "note": "This is the end state, reached after the documents and the call in either order. R2 Met, R3 met-with-residual (counts as Met for the verdict, the clock as a gap question), R4 Partial and R7 Partial give Nearly ready, with the reason line reading scale established from the client's document, cost effort-quantified, missing multiplier the loaded rate and the bench's time. The document-only pass before the call is a different state, asserted in intake.grading_passes.document_only: Not ready, no gate met, no build. Gap questions for the 9th (at most five, per audience): the priority approval (Annelise and Marguerite), the clock and the finding (Annelise), the bench's time and input mechanism (Marguerite), the decision threshold, the win and the upside (Cormac through Annelise), the results-database read (Annelise). Propose the blueprint and a v0.1 once the pre-build questions are answered or listed as assumptions, with the priority approval carried as an open decision if the 9th does not settle it. No figure, no proposal; pricing is not part of this plugin. The automations are put forward as one approval list, the priority notification among them.",
    }
    key["account_context"] = {
        "tier": "unknown",
        "products_enabled": [
            "unknown: no document and no line of the call says which monday products or seats exist",
            "No account evidenced. 'Annelise has got a login to something from her last place, I think' (%s) is hearsay about a login and is not evidence of an account, a tier or a product; treat Work Management as a product to be provisioned, not found" % T(71),
            "No CRM and no Service discussed",
        ],
        "existing_monday_setup": "None evidenced. The register is a spreadsheet plus a paper day book, results live in the validated results database, and certificates are typed into a template; nothing is inherited, audited or migrated. The plugin should ask which account the build goes into, who administers it, and which products and seats are being bought, before designing anything that depends on the answer, and should not take the Quality Manager's possible old login as an account.",
        "evidence_quote_or_null": "No. Annelise has got a login to something from her last place, I think. I don't know what.",
    }
    key["expected_structures"] = {
        "native_boards_required": [],
        "portfolio_expected": False,
        "portfolio_reason": "No account and no tier: nothing in the documents or the call names a monday account, a plan or a seat count, so the A6 default cannot fire and is not assumed. Work Management is the only product and the work is one register with a status per sample, a bench view and a certificate draft, none of it portfolio-shaped. The tier is read live at preflight once an account exists; if it turns out to be Enterprise the portfolio question is asked then, with the reason recorded, not assumed now.",
        "lookalike_traps": [
            "Building a Submitters, Merchants or Customers board as a CRM look-alike in a build with no CRM in scope; if submitters are to be tracked in their own right, the native CRM Accounts and Contacts boards are used.",
            "Rebuilding the results database inside the platform, or copying results into a Results board as the record; results are read from the validated database and never held on the platform as the record (W-4, write-up section 3).",
            "A Certificates board or automation that issues a certificate on a status change; the certificate is a draft for signature and the signatory rule of section 6.4 stands.",
            "Building the on-screen priority approval (W-3) as if it were today's process, or dropping the approval because the operator says it is not used; the step is an open conflict until the 9th and is built neither way before then.",
            "Modelling the benches as a People column or as people: purity, germination and moisture and vigour are teams, and the bench is a status or dropdown with a view each.",
            "Treating the write-up's ten wants as current state and skipping the SOP, or the reverse: the SOP feeds current state, the write-up the requirement trace, and the figure the documented rows.",
        ],
        "notes": "One product, one board of samples with the register's fields as columns, a status from receipt to certificate, a bench column with a view per bench in priority order, a priority flag with a notification (on the approval list), a re-test status with the authorisation number, dates for results entered, checked, prepared and signed, and turnaround measured against section 6.5. The figure's twelve documented rows are the shape of the status column and the two decision points are the priority flag and the re-test loop. The results database is read, not modelled; the certificate is a draft; the paper forms stay. No CRM, no Service, no portfolio, no time tracking. Submitter names and results never enter seed data. Every automation, including the priority notification, goes on one approval list with recipients shown.",
    }
    key["accepted_behaviours"] = [
        "Taking the three documents as one intake or as three, in any order, as long as each gets its own snapshot with its own author, date and status fields and the SOP's fields are never copied onto the figure or the write-up.",
        "Recording the write-up's author as unknown with the call's attribution to the Quality Manager noted beside it, or as unknown alone; writing the Quality Manager into the field as the document's author is not accepted.",
        "Citing the SOP by section number with or without the section title, and the write-up by page with or without the section number or the W id, as long as no extract is cited by speaker and every extract carries the document.",
        "Labelling the documented rows in the figure's own words or lightly normalised, as long as there are twelve rows, two of them decisions with two labelled exits each, every row marked documented and cited to the figure's page, and none marked spoken or observed.",
        "Grading R1 and R6 in the document-only pass as met-with-residual, or as met with the residual (time on their own process; the leadership win) shown as a gap question with its role; both count as Met for the gates.",
        "Grading R3 met-with-residual, or met with the clock shown as a gap question routed to the Quality Manager; the verdict is Nearly ready either way because R4 is Partial.",
        "Grading R6 met-with-residual in the end state, or met with the leadership win carried as a gap question to the Director; grading it Met on the operator's guess at his win is not accepted.",
        "In the document-only pass, admitting the write-up's problem statements as P1 and P2 Stated, or recording them in the requirement trace only with Stated unmet; both give R2 Partial, the same verdict and the same shut gates. R9 document-only may be partial or missing and R12 document-only missing or partial, as long as the constraints reach the requirement trace and no gate opens.",
        "Naming the write-up's and the figure's stems from the arrival date because they carry none, and flagging their sequence as a tie; either order between the two undated documents.",
        "Recording the conflict as one block with both statements and W-3 noted as the dependent requirement, or as one block with three sources; never as two conflicts and never resolved.",
        "Adding a submitters question (CRM, native boards if yes) without proposing CRM, or leaving CRM unmentioned; proposing CRM or Service is not accepted.",
        "Recording the relayed reasons and timings ('Annelise said before the visit') as reported, or as the operator's own hedged statement with the Quality Manager named; never as the Quality Manager's statement.",
        "Placing the scale section beside the bleed frame or inside it, as long as it is filled in both passes with the multiplier named.",
        "Naming the product 'Work Management' or 'core', as long as it is the only product proposed.",
        "Labelling the 'Speaker 2' line as an unresolved client voice with the side inferred from the vocative and the context, or leaving it unattributable with no side; never binding it to a named person.",
        "Treating 'the co-op', 'the Harrowfield growers' and 'the co-operative' as one alias and 'Marlowe's' as a merchant customer, without a full name for either.",
        "In the call-first run, grading the call alone as an intermediate state is not asserted by this key; only the end state after both kinds of input is.",
    ]
    key["expected_leak_blocklist"] = [
        "The conflict text in every form: 'Nobody uses it', 'It doesn't happen', 'That box on the form', 'the priority box', 'nobody at that desk at half past eight', 'If she looks', and any sentence saying the priority approval is not done; the callback is phrased as a question about the procedure and never quotes the operator to the client.",
        "The operator's remarks about colleagues: 'she's not on reception', 'I'm not going to say she doesn't know', 'Marguerite is quite hot on that one', 'she checks the numbers against the forms', 'Marguerite had to sign the reissue and she wasn't happy', 'Tobiah will, the others won't', 'they'd be cross with me', 'She doesn't love it'.",
        "'Don't make it sound like I've dobbed anyone in', 'Good luck', 'I don't buy things', 'Ask her', 'You'd have to ask Cormac', and every other line about who knows what or who decides.",
        "The September incident: the trial lot, 'sowing that weekend', 'the eleventh day', 'They'd sown it on the Saturday. Untested.', 'they rang to tell us', 'Annelise had to write to them', 'not trusting us in the first month of a contract we'd only just won'.",
        "The transposed certificate: 68, 86, 'sixty-eight instead of eighty-six', 'Transposed', 'we reissued', 'the reissue', 'Twice this year'.",
        "The audit finding: 'a finding at the surveillance visit in May', 'the assessor asked me to show where a sample was', 'In front of an assessor', 'it has to be closed before the next visit', 'March, I think'; the accreditation itself may be named as a fact, the finding may not.",
        "Cost inputs and time figures: 'two hours a day', '2 h/day', 'Ten minutes? Fifteen', '10-15 minutes', 'thirty a day', 'thirty certificates', and any rate, total or multiplication built from them.",
        "'ninety-two hundred', '9,200', '9200', 'two thousand samples a year on top', '2,000 more', 'eleven thousand' or any total built from the SOP's 9,000 and the co-operative's figure.",
        "The register's failures: 'corrupted twice', 'lost a day and a half of receipts', and the day book as a workaround narrative (the day book may be named as a current-state fact).",
        "'a login to something from her last place', and any statement about the Quality Manager's previous employer or accounts.",
        "The customers by name in any client-facing text other than the client's own SOP draft: 'Marlowe's', 'the Harrowfield growers', 'the co-op'; submitter names and results are confidential to the submitter (write-up section 3).",
        "Our own claim: 'A flag that notifies someone is a normal thing for it to do' is not restated to the client from memory; it is shown or it is in the claims store.",
        "Method vocabulary and markers: P1, P2, R1 to R12, [Q], [Q/doc], [I], [X], 'documented', 'spoken', 'observed', 'conflict', 'met-with-residual', 'not-obtainable', 'advisory', 'effort-quantified', 'bleed', 'upside', 'excavated', 'gate', 'verdict', 'Nearly ready'.",
        "Stakeholder assessments: 'the operator', 'end user', 'approver (absent)', 'decision-shaped absentee', 'fear of exposure', 'loyalty hedge', 'scepticism', 'titled Supervisor, behaves as', and every objection type.",
        "Internal ids, file stems and record paths: inputs/, calls/, open-questions.md, structure-inventory.md, the intake report, the sha256 lines, the strand id.",
        "Flag, do not remove (process facts that belong in an SOP or on a board, but worth a look before they ship): about 9,000 samples a year; the peak September to January; over 80 samples a day in the peak; 21, 10 and 7 day turnaround targets; six-year retention; QF-03, QF-12, QM-01 and the QP references; the three benches; the signatory rule; receipt between 08:00 and 16:00; the weekly backup.",
        "CAUTION: 'priority', 're-test', 'approved' and 'authorised' are the client's own vocabulary (QP-07 sections 4.2 and 4.3) and must survive in the SOP and on the board; only the sentences about the step not being used are blocked.",
        "CAUTION: text that matches QP-07 verbatim is the client's own document and is exempt from the copied-run rule in the SOP draft; the same words inside our recap or blueprint are not exempt from any other rule.",
    ]

    # ------------------------------------------------------------ intake
    HDR = {"label": "discovery", "seat": "partner-led", "relationship": "new logo", "direction_of_show": "nobody shows", "output_class": "configured structure",
           "room_shape": "small: one client operator at a reception desk, one unresolved second client voice", "money_live": "no: no figure our side spoke, no tier, no price; the operator does not buy and the approver was absent",
           "signals": [{"signal": "screen-control deixis", "result": "none; our side states no screen", "quote": "I'm not going to show you anything today."}, {"signal": "same-side screen direction", "result": "none (one person on our side)"}, {"signal": "agenda sentence and the client's answer", "result": "discovery: the agenda sentence at %s and the operator's acceptance at %s" % (T(2), T(3)), "quote": "Yeah, that's fine. She said you'd want the real version. [laughs] Ask away."}, {"signal": "output-class markers", "result": "configured structure: a register, a status, a list per bench, a flag; no code, modules or renderers", "quote": "If it just did the register and the where-is-it, that'd be most of it for me."}, {"signal": "commercial markers", "result": "who approves spend (%s, from the operator, second-hand about the threshold); no currency figure, tier, seat or credit count from either side" % T(65), "quote": "But anything that costs money is Cormac."}],
           "proposal": "one-line dismissible header with the agenda quote; detection proposes, the user decides", "documents": "none: a document carries no type header and none is proposed for the SOP, the figure or the write-up"}
    intake = {}
    intake["files"] = [
        {"file": SOP_FILE, "input_kind": "document", "sequence": 1, "provenance": "first-hand: supplied by the client's Quality Manager to the user", "handed_over_by": "none", "author": "Annelise Valdemarsson, Quality Manager", "document_date": "2026-03-11", "status": "approved, current practice", "format": "docx: %d paragraphs, 8 numbered sections plus a revision history, read by unzipping word/document.xml and docProps/core.xml" % docx_info["paragraphs"], "type_header": "none: a document carries no type header and none is proposed", "strands": "unassigned until the front door routes it; 001 once the strand is opened"},
        {"file": FIG_FILE, "input_kind": "document", "sequence": "tie with the write-up, after the SOP: undated; QP-07 section 1.3 names it as issued with the procedure, recorded as an inference [I]", "provenance": "first-hand: supplied with the SOP", "handed_over_by": "none", "author": "unknown", "document_date": "unknown", "status": "unknown", "format": "PNG image, %d by %d, no text chunks; reported as one page for the model to read; 12 nodes (10 steps, 2 decisions), 13 arrows, exit labels Yes and No on each diamond, re-test on the loop" % png_info["size"], "type_header": "none", "strands": "as the SOP"},
        {"file": WU_FILE, "input_kind": "document", "sequence": "tie with the figure, after the SOP: undated; it cites QP-07 sections 6.4 and 6.5, so it knows version 3.2, an inference [I] for ordering only", "provenance": "first-hand: supplied with the SOP", "handed_over_by": "none", "author": "unknown (the call attributes it to the Quality Manager; recorded beside the field, not in it)", "document_date": "unknown", "status": "unknown", "format": "PDF, 2 pages, 4 numbered sections, no document information dictionary; text by page through pdftotext when present, otherwise read as pages by the model", "type_header": "none", "strands": "as the SOP"},
        {"file": TX_FILE, "input_kind": "transcript", "sequence": 4, "call_type": "discovery", "provenance": "first-hand", "handed_over_by": "none", "type_quote": Q(3, "Yeah, that's fine. She said you'd want the real version. [laughs] Ask away."), "type_note": "The agenda sentence at %s ('I'm not going to show you anything today. I just want to ask how a sample gets through the building.') and the operator's next turn accepting it set the type; no screen-control deixis, no code or module markers, no currency figure from either side." % T(2), "date": "not stated; a working day in the last week of September 2026, from 'from October', 'Next week's the first lorry', the incident in 'September' and 'Friday the ninth' booked as the next meeting", "attendees": ["Rosalind Okonjo, Sample Reception Coordinator, client", "Speaker 2, unresolved client voice, one line", "Consultant, our side"], "voices_missing": "unknown -- no roster; the two client voices are the only roster"},
    ]
    intake["package_order"] = "not a package (A15 does not apply): three documents and one call, first-hand, ordered by each input's own date and internal evidence and never by arrival or file name: the SOP (dated 2026-03-11), then the figure and the write-up as a tie (undated; both refer to QP-07 version 3.2), then the call (last week of September 2026); the same order in both arrival runs"
    intake["export_family"] = {"file": TX_FILE, "family": "block export", "dialect": "'[HH:MM:SS] Speaker Name: text', one turn per line, elapsed time from the recording start, no end times, no header", "end_times": False, "timestamp_shape": "HH:MM:SS elapsed, zero-padded, strictly increasing, no collisions", "label_position": "prefix inside the line, uniform shape, full names plus one export placeholder ('Speaker 2')", "participant_header": "absent", "units": ts["lines"], "words": ts["words"], "max_unit_words": ts["longest_consultant"][0] if ts["longest_consultant"][0] >= max(len(re.sub(r"\[[a-z]+\]", "", t).split()) for s, t in ct.TURNS if s != ct.C) else max(len(re.sub(r"\[[a-z]+\]", "", t).split()) for s, t in ct.TURNS if s != ct.C), "adjacent_same_label_pairs": sum(1 for a, b in zip(ct.TURNS, ct.TURNS[1:]) if a[0] == b[0]), "lowercase_initial_units": sum(1 for s, t in ct.TURNS if t[0].islower()), "units_at_or_under_four_words": sum(1 for s, t in ct.TURNS if len(t.split()) <= 4), "colliding_timestamps": 0, "line_endings": "LF", "note": "measured before content is read; a small clean file, so the defect index is low and the doubt level is not lowered by it"}
    intake["detectors"] = {"composite_splitter": "runs on unit length (no end times); no unit qualifies; composite_blocks is empty", "wedge_flagger": "cannot run (no end times); says so in the intake record; wedges is empty", "rule": "both detectors run on the transcript and neither fires; neither runs on a document, because a document is not units"}
    intake["type_header"] = HDR
    intake["documents"] = {
        "author_date_status_rule": "recorded from the document's metadata and its first page; each unknown where the document does not say; never inferred from another document or from a call, never invented",
        "sop": "author from the front page 'Author:' line and dc:creator, which agree; date from 'Date of issue: 11 March 2026' and dcterms:modified 2026-03-11, which agree, while dcterms:created 2026-02-24 is the drafting date and the revision history's earlier dates belong to earlier versions; status from 'Status: Approved. Current practice.' and cp:contentStatus 'Approved'",
        "figure": "author unknown, date unknown, status unknown; the SOP's cross-reference (section 1.3) is an inference for the sequence and nothing else",
        "write_up": "author unknown, date unknown, status unknown: no information dictionary, no name, no date, no status word anywhere; 'Notes for the systems review' is a subtitle; three unknown fields and no invented author; the call's attribution to the Quality Manager (%s, %s) is a spoken fact recorded beside the field" % (T(2), T(40)),
        "citation_tier": "SOP extracts at the attributed tier (author known); figure and write-up extracts one step below, as 'the client's document', level with attributed-with-a-qualifier",
    }
    intake["section_map"] = [
        {"document": "QP-07", "section": "front page", "mark": "metadata", "feeds": "author, date, status, version, distribution; not current state"},
        {"document": "QP-07", "section": "1 Purpose and scope (1.1 to 1.3)", "mark": "current state", "feeds": "scope of the process; 1.3 names the figure"},
        {"document": "QP-07", "section": "2 Definitions (2.1)", "mark": "current state", "feeds": "the vocabulary map: sample, submitter, test request, register, bench sheet, results database, certificate, priority request, re-test, bench"},
        {"document": "QP-07", "section": "3 Sample receipt (3.1 to 3.5)", "mark": "current state", "feeds": "receipt, logging, storage, enquiries (3.4 documents the walk), volume (3.5 fills the scale section)"},
        {"document": "QP-07", "section": "4 Test allocation (4.1 to 4.3)", "mark": "current state", "feeds": "allocation (4.1, the Supervisor title); 4.2 the priority approval (the conflict's document side); 4.3 the re-test authorisation (confirmed used)"},
        {"document": "QP-07", "section": "5 Testing (5.1 to 5.4)", "mark": "current state", "feeds": "bench records and results entry; 5.4 the outage fallback"},
        {"document": "QP-07", "section": "6 Review and certification (6.1 to 6.5)", "mark": "current state", "feeds": "second-analyst check, tolerance and re-test, certificate preparation (6.3, P2's documented workaround), signatory rule (6.4), turnaround targets (6.5)"},
        {"document": "QP-07", "section": "7 Records (7.1, 7.2)", "mark": "current state", "feeds": "retention and backup; compliance signals"},
        {"document": "QP-07", "section": "8 Related documents", "mark": "reference list", "feeds": "the form and procedure numbers; nothing graded"},
        {"document": "QP-07", "section": "Revision history", "mark": "document control", "feeds": "version dates; not the document's date and not a clock"},
        {"document": "figure 1", "section": "p.1", "mark": "current state", "feeds": "the twelve documented rows below"},
        {"document": "write-up", "section": "1 Why we are looking at this (p.1)", "mark": "desired state", "feeds": "the reasons behind the wants; admitted for P1 and P2 Stated as the client's own words; never the current-state section"},
        {"document": "write-up", "section": "2 What we want, W-1 to W-10 (p.1)", "mark": "desired state", "feeds": "R6 and the requirement trace; W-3 joins the conflict block as the dependent requirement"},
        {"document": "write-up", "section": "3 Constraints (p.2)", "mark": "desired state", "feeds": "R9 (Partial document-only), compliance signals, the requested changes"},
        {"document": "write-up", "section": "4 Out of scope (p.2)", "mark": "desired state", "feeds": "scope exclusions: invoicing, the methods, the results database itself, seed health"},
    ]

    def drow(n, kind, label, owner, read_back, extra=""):
        return {"row": n, "kind": kind, "label": label, "source": "figure 1 p.1", "marker": "documented", "class": "current state", "owner": owner, "read_back": read_back, "note": extra}
    intake["documented_rows"] = [
        drow("N1", "start", "Sample received", "Sample Reception Coordinator (QP-07 section 3.1)", "not read back"),
        drow("N2", "step", "Log in sample register", "Sample Reception Coordinator (section 3.2)", "confirmed at %s with lived detail (a spreadsheet; the day book first)" % T(7)),
        drow("N3", "decision", "Priority requested?", "Sample Reception Coordinator (section 4.2)", "read back at %s; the exit to N4 contradicted at %s" % (T(20), T(21)), "exits: Yes to N4, No to N5"),
        drow("N4", "step", "Laboratory Manager approves", "Laboratory Manager (section 4.2)", "contradicted at %s and %s: the conflict" % (T(21), T(23)), "the documented approval step; the call says it is not used; kept as the conflict, the row stays documented"),
        drow("N5", "step", "Allocate to bench", "Laboratory Supervisor (section 4.1); lived: the Laboratory Manager, from a printout", "confirmed at %s with lived detail (a printout with biro; done by the Laboratory Manager)" % T(13)),
        drow("N6", "step", "Test at bench (bench sheet)", "the analyst (sections 5.1, 5.2)", "not read back"),
        drow("N7", "step", "Enter results in results database", "the analyst (section 5.3)", "confirmed at %s (three writes)" % T(45)),
        drow("N8", "decision", "Within tolerance?", "second analyst and Laboratory Manager (sections 6.1, 6.2)", "not read back", "exits: Yes to N10, No to N9"),
        drow("N9", "step", "Re-test authorised (QF-12)", "Laboratory Manager (section 4.3)", "confirmed at %s ('So that one's real.')" % T(27), "loops back to N6, labelled re-test"),
        drow("N10", "step", "Second-analyst check", "a second analyst (section 6.1)", "not read back"),
        drow("N11", "step", "Prepare and sign certificate", "Sample Reception Coordinator prepares, Laboratory Manager or Quality Manager signs (sections 6.3, 6.4)", "confirmed at %s and %s (typed from the database; signed by the Laboratory Manager, the Quality Manager if she is off)" % (T(45), T(47))),
        drow("N12", "end", "Certificate sent to submitter", "Sample Reception Coordinator (section 6.4)", "not read back"),
    ]
    intake["read_back"] = {"grade": "partial", "where": "graded by discovery-check in front of the Solution blueprint gate, as 7.1 requires where a structure inventory exists", "rows": ["N2 confirmed", "N3 read back", "N4 contradicted (conflict)", "N5 confirmed", "N7 confirmed", "N9 confirmed", "N11 confirmed"], "not_read_back": ["N1", "N6", "N8", "N10", "N12"], "rule": "the marker stays documented in both passes; read-back adds a state per row and never turns a documented row into a spoken one; in the document-only pass every row reads 'not read back'"}
    intake["extract_rule"] = "every extract is [Q/doc] with the document and its section or page and never a speaker; the SOP's author, date and status travel with each of its extracts; the figure is cited to its page; the write-up to its page; verify-quotes checks each against the intake report's text by anchor with the raw file absent"
    intake["conflicts"] = [
        {"kind": "conflict", "proposition": "whether a priority request is approved by the Laboratory Manager before allocation",
         "document": D("A priority request is approved by the Laboratory Manager before the sample is allocated.", "QP-07 section 4.2"),
         "document_status": "approved, current practice, dated 2026-03-11, author the Quality Manager",
         "dependent_requirement": D("Priority requests approved by the Laboratory Manager on screen, not on the form", "write-up p.1 section 2, W-3"),
         "call": [Q(21, "That box on the form? Nobody uses it."), Q(23, "It doesn't happen. I mean, it's in the procedure, and Annelise wrote the procedure, so it's not that nobody knows it's there.")],
         "handling": "both statements kept with their sources, the document's section standing where a speaker would, in the strand's open-questions.md as kind conflict with a conflict log entry; the current-state picture carries the lived version with the documented version beside it; no recency rule, nothing discarded, the rest of the SOP untouched; W-3 recorded as the requirement that depends on the answer; a gap question for the 9th, phrased as the procedure against reception; the priority mechanism built neither way before then",
         "callback": "the best callback material there is: 'Your procedure has the Laboratory Manager approving priority requests before allocation, and the notes want that on screen. Reception described a different route. Which should the new register do?' to the Quality Manager and the Laboratory Manager together, never to the operator alone"},
    ]
    intake["not_conflicts"] = [
        "9,000 (QP-07 section 3.5) against 'ninety-two hundred, something like that' (%s): agree within rounding; the operator attributes the figure to the procedure; not a conflict" % T(39),
        "the day book (%s) against the SOP's silence: an addition to current state, not a conflict" % T(9),
        "the bench allocation sheet (section 4.1) against 'a printout of your register' with biro (%s, %s): lived detail consistent with the document, not a conflict; the Supervisor-versus-Manager title question rides with it as a question, not a conflict" % (T(11), T(13)),
        "the figure's re-test loop against section 6.2: the two documents agree; no document-versus-document conflict",
    ]
    intake["grading_passes"] = {
        "document_only": {
            "inputs": "the SOP, the figure and the write-up, before any call; reached by the front door chaining discovery-check after the document-only intake, as after a discovery call",
            "type_header": "none: no call type is proposed for a document; its absence demotes nothing",
            "advisory_rows": 0,
            "asked_flags": "every row asked false: no question can be put to a document, and the flag is not applicable rather than a defect",
            "criteria": [
                "R1 met-with-residual: QP-07 sections 3.1 to 7.2 and the twelve documented rows, [Q/doc]; the residual is time on their own process, which no document states, routed to the operator",
                "R2 partial: P1 and P2 Stated from write-up p.1 section 1 (tier 'the client's document'), nothing Concrete anywhere",
                "R3 missing: no change, trigger or clock stated; 'Review due: March 2027' is document control",
                "R4 missing: the scale section filled from QP-07 section 3.5 (about 9,000 a year, peak September to January, over 80 a day), the missing multiplier named; no cost stated",
                "R5 missing: no value stated",
                "R6 met-with-residual: write-up section 2, W-1 to W-10, tier 'the client's document'; the residual is what leadership would count as a win, which no document states",
                "R7 missing: 'Approved by' on the front page is document control",
                "R8 missing: no priority or timing stated",
                "R9 partial: write-up p.2 section 3 states design constraints, not what could stop the work",
                "R10 missing: a document commits nobody",
                "R11 missing",
                "R12 missing: scope cannot be agreed verbally by a document",
            ],
            "pains": [
                "P1: Stated met (write-up p.1 section 1), Concrete missing, Workaround partial (QP-07 section 3.4 documents the walk as procedure), Reach missing, Cost inputs missing, Trajectory missing; not excavated",
                "P2: Stated met (write-up p.1 section 1), Concrete missing, Workaround partial (QP-07 section 6.3 documents the transcription and check), Reach missing, Cost inputs missing, Trajectory missing; not excavated",
            ],
            "verdict": "Not ready (R3, R4 and R7 Missing)",
            "gates": "none met: Solution blueprint needs R2 Met; Build and First demo (v0.1) follow it; Pricing or proposal prep and v1.0 sign-off not met",
            "should_plugin_propose_a_build": False,
            "gaps_shown": "every gap the documents cannot fill is shown as a gap with the role that can supply it: why now and the clock (Quality Manager), time on the process and cost inputs (the operator, the Laboratory Manager), upside, the leadership win and decision process (Laboratory Director), timing and scope (Quality Manager), the next step (whoever books)",
            "questions": [
                "Why now: what changed, and is there a date this must be done by? (Quality Manager)",
                "Cost: how much time do reception and each bench spend on the register, the enquiries and the certificates? (the operator; the Laboratory Manager)",
                "Decision: who decides, at what threshold, by when, and what would count as a win? (Laboratory Director)",
                "Which of the ten wants come first, and who agreed the list? (Quality Manager)",
                "Next step: who books the walk-through, and when? (Quality Manager)",
            ],
            "read_back": "every documented row 'not read back'; the read-back grade is not yet available and the blueprint gate is shut on R2 in any case",
            "vocabulary_and_structure": "the vocabulary map and the documented rows are complete from the documents alone and do not change with the call",
        },
        "with_call": {
            "inputs": "the three documents plus the call; the call's header scopes the criteria as a discovery call, the documents' extracts are admitted under the document rules, and the result is the 25 fields above",
            "moved": ["R1 met-with-residual to met (time on the process from the operator)", "R2 partial to met", "R3 missing to met-with-residual", "R4 missing to partial (effort-quantified, rate pending)", "R5 missing to not-obtainable (Laboratory Director)", "R7 missing to partial", "R8 missing to partial", "R9 partial to met", "R10 missing to met", "R12 missing to partial", "P1 excavated (Reach and Trajectory partial, Cost inputs met)", "P2 excavated (Reach and Trajectory partial, Cost inputs met-with-residual)", "read-back from not available to partial"],
            "unchanged": ["R6 met-with-residual (the leadership win still unstated by leadership)", "R11 missing", "the documented rows and their marker", "the author, date and status fields", "the section map", "the vocabulary map"],
            "operator_figure": "'It's two hours a day, some days. Most days.' (%s) grades as a client figure with the call as its source, beside the SOP's 9,000 with the document as its source; neither is superseded by the other and no arithmetic runs between them" % T(19),
            "verdict": "Nearly ready",
            "should_plugin_propose_a_build": True,
        },
        "arrival_orders": {
            "run_a": "the SOP, the figure and the write-up first, then the call",
            "run_b": "the call first, then the SOP, the figure and the write-up, from the same fixture with no new file",
            "same_end_state": "the twelve R grades and the twelve per-pain grades, the verdict and the five gates, the one conflict with both statements, the four not-conflicts, the twelve documented rows with their read-back states, the author, date and status fields of each document, the section map, the vocabulary map, the scale section, the pre-build questions and the SOP starting point are identical in both runs",
            "allowed_to_differ": ["the order and timestamps of log.md entries", "the arrival dates in the stems of the two undated documents and their intake reports"],
            "not_special": "sequence comes from each input's date and internal evidence, never from arrival; the call is sequence 4 in both runs because it is dated after the SOP; nothing waited for the other kind of input; the first input is not special for having come first",
            "intermediate": "run_a passes through the document-only state above; run_b passes through a call-only state that this key does not assert",
        },
    }
    intake["retention_stop"] = "the open question [A11-3] stops the first input of either kind before it is saved, once per client; its answer covers the three documents and the transcript; no second stop when the other kind arrives. This fixture is fictional and does not trigger it; H56 asserts the behaviour in both arrival orders."
    intake["inputs_saved"] = "each document saved unchanged through record.py add-document into inputs/ with its sha256 recorded and its snapshot (document-summary.md, input_kind document) beside it; the SOP's stem dated 2026-03-11 from its own date, the figure's and the write-up's from the arrival date with the sequence flagged as a tie; a document log entry per document and no meetings.md line; the transcript through add-transcript into calls/ with a call entry and a meetings.md line; the sha lines never quote content"
    intake["composite_blocks"] = "none: one speaker per line with clean labels; the composite detector should not fire"
    intake["wedges"] = "none: a block export with no end times; the wedge detector does not apply"
    intake["rejoined_sentences"] = [
        {"sentence": "It's about two thousand samples a year on top. Which on nine thousand -- ninety-two hundred, something like that, last year.", "owner": "Rosalind Okonjo, both halves", "units": "%s and %s, with the Consultant's %s between them" % (T(37), T(39), T(38)), "handling": "the halves are cited from their own turns and never merged into one quote across the Consultant's label; the figure 'ninety-two hundred' is read from %s with its hedge; 'On nine thousand, that's a fair chunk.' is our interjection and non-evidence" % T(39)},
    ]
    intake["alias_map"] = [
        {"canonical": "Rosalind Okonjo", "forms": ["Rosalind", "Ros"], "side": "client", "note": "the operator; 'Ros' is the vocative in the Speaker 2 line and binds to her as the addressee"},
        {"canonical": "Annelise Valdemarsson", "forms": ["Annelise", "the Quality Manager", "Author:"], "side": "client", "note": "mentioned only, absent from the call; surname from the SOP's front page and dc:creator; owner of the procedure and the project"},
        {"canonical": "Marguerite (Laboratory Manager)", "forms": ["Marguerite", "the Laboratory Manager"], "side": "client", "note": "mentioned only, absent; surname never given anywhere; the SOP names the role, the call the name; also does the allocation the SOP gives the Laboratory Supervisor"},
        {"canonical": "Cormac Delahunty", "forms": ["Cormac", "the Laboratory Director", "Approved by:"], "side": "client", "note": "mentioned only, absent; surname from the SOP's front page; the approver for spend, threshold unknown; a decision-shaped absentee never addressed by our side, recorded as a named risk row"},
        {"canonical": "Tobiah (bench analyst)", "forms": ["Tobiah"], "side": "client", "note": "mentioned only; first name only; the one analyst who would touch a screen"},
        {"canonical": "Speaker 2", "forms": ["Speaker 2"], "side": "client, inferred from the vocative and the courier context", "note": "unresolved; one unit; not bound to any named person"},
        {"canonical": "the Laboratory Supervisor", "forms": ["Laboratory Supervisor"], "side": "client", "note": "a title in QP-07 sections 4.1 and 5.4, never named on the call; in practice the Laboratory Manager allocates; one person or a vacant role is a question, never merged and never invented"},
        {"canonical": "Marlowe's (seed merchant)", "forms": ["Marlowe's", "the merchant"], "side": "the client's customer", "note": "possessive form as spoken; never a person"},
        {"canonical": "the Harrowfield growers' co-operative", "forms": ["the co-op", "the Harrowfield growers", "the co-operative"], "side": "the client's customer", "note": "signed from October; the September trial lot"},
        {"canonical": "purity / germination / moisture and vigour", "forms": ["purity", "germination", "the germinator"], "side": "benches, not people", "note": "ordinary words in a name slot ('told purity', 'whoever's on purity'); never coerced into names"},
        {"canonical": "the assessor", "forms": ["the assessor", "the accreditation body"], "side": "third party", "note": "role only; the surveillance visit in May"},
    ]
    intake["confidence"] = "every unit certain except %s (Speaker 2), unattributable, and %s (Rosalind, with a [pause]), certain; no probable or uncertain unit; the figure at %s carries its hedge; document extracts carry no confidence state, only their tier" % (T(30), T(31), T(39))
    intake["quarantine"] = "none: no screen was shared and no hypothetical frame narrates names or figures; the playback at %s is a plan for the first version, not narration" % T(72)
    intake["second_hand"] = [
        {"kind": "the operator relaying the Quality Manager's figure, which is the document's", "requote": Q(39, "-- ninety-two hundred, something like that, last year. It's in the procedure, it's Annelise's number, I don't count them."), "true_source": D("The laboratory receives approximately 9,000 samples a year.", "QP-07 section 3.5"), "status": "the document's figure is the client figure with the document as its source; the operator's restatement is hedged and second-hand, kept beside it, never averaged with it and never promoted"},
        {"kind": "the operator relaying the Quality Manager's reasons, timing and wants", "requote": Q(67, "Realistically Annelise said before the visit. But that's her saying it, not me. Ask her."), "true_source": {"quote": None, "location": None, "note": "none on the call or in the documents; the Quality Manager has not spoken"}, "also": [Q(73, "Annelise will want the turnaround numbers, she's asked for them twice."), Q(63, "And the audit finding closed, Annelise would say that.")], "status": "recorded as reported by the operator with the Quality Manager named; the facts the operator knows first-hand (the finding in May, the contract from October, the first lorry next week) are her evidence; the Quality Manager's motives, dates and wants are not attributed to her until she states them on the 9th"},
    ]
    intake["claims_by_our_side"] = [
        Q(76, "A flag that notifies someone is a normal thing for it to do.") | {"hedge": "none", "store": "claims store entry: a status flag notifying a named person; speaker our side; unhedged; standard platform behaviour; shown on the 9th or at the demo, never asserted again from memory"},
    ]
    intake["delivery_notes"] = [
        "Client share about %.0f%% (the operator, with one unresolved second voice under 1%%); the Consultant's longest turn %d words at %s, the first-cut playback; no own-side stretch longer than one turn." % (ts["client_share"], ts["longest_consultant"][0], ts["longest_consultant"][1]),
        "Defect: at %s the Consultant spoke across the operator's figure ('On nine thousand, that's a fair chunk.'); the figure completed at %s and is quoted from there." % (T(38), T(39)),
        "Good practice: the approval conflict was raised as a question and not a finding (%s, %s, %s); the September incident was not priced (%s); the bench time was routed rather than guessed (%s); the next meeting was booked with a date, a time and both owners." % (T(26), T(82), T(84), T(36), T(56)),
        "The fix-offered-mid-pain check does not fire: the playback comes after the current-state walk, and the notification answer at %s answers the operator's own question." % T(76),
    ]
    intake["voices"] = "no roster (no header, no narrated roster): voices heard are the operator and one unresolved second client voice; voices missing reads 'unknown -- no roster'. The people the documents name (the Quality Manager, the Laboratory Director, the Laboratory Manager by role) are not attendees of anything and are not counted as missing voices; the Director is a decision-shaped absentee recorded as a named risk row, with our side never having addressed him."
    intake["sop_starting_point"] = {
        "structure": "our SOP starts from QP-07's own sections in order: 1 Purpose and scope, 2 Definitions, 3 Sample receipt, 4 Test allocation, 5 Testing, 6 Review and certification, 7 Records, 8 Related documents, plus a revision history",
        "vocabulary": "sample, submitter, test request, sample register, bench sheet, results database, certificate, priority request, re-test, bench, allocation, authorised signatory",
        "what_changed": "each amended section shows what changed against QP-07 version 3.2: 3.2 the register, 3.4 the status on screen, 4.1 the bench list, 4.2 the priority flag and whatever approval the 9th settles, 6.3 the certificate draft, 6.5 turnaround measured; 4.3, 6.4 and 7 unchanged",
        "bundle": "the client's SOP reaches the drafter through the bundle (sop_tools.py inputs --from-document) as its own text and its headings in order from the snapshot's section map; the snapshot's current-state and desired-state marks, the conflict and the markers never do",
        "lint": "the copied-run rule exempts text that matches QP-07; every other rule runs on the draft",
    }
    intake["corrections_block_for_next_meeting"] = "none: nothing our side said on the call needs correcting on the 9th; the claim at %s is shown rather than restated" % T(76)
    key["intake"] = intake
    return key


# ------------------------------------------------------------ serialise
FLAT = {"export_family", "type_header", "documents", "sop_starting_point", "detectors", "read_back"}


def dump(obj, depth, expand_to, indent=0, name=None):
    pad = "  " * indent
    if name in FLAT:
        return json.dumps(obj, ensure_ascii=True)
    if isinstance(obj, dict) and obj and depth < expand_to:
        items = list(obj.items())
        out = ["{"]
        for i, (k, v) in enumerate(items):
            sub = expand_to + 1 if k in ("intake", "grading_passes") else expand_to
            s = pad + "  " + json.dumps(k) + ": " + dump(v, depth + 1, sub, indent + 1, k)
            out.append(s + ("," if i < len(items) - 1 else ""))
        out.append(pad + "}")
        return "\n".join(out)
    if isinstance(obj, list) and obj and depth < expand_to:
        out = ["["]
        for i, v in enumerate(obj):
            out.append(pad + "  " + dump(v, depth + 1, expand_to, indent + 1) + ("," if i < len(obj) - 1 else ""))
        out.append(pad + "]")
        return "\n".join(out)
    return json.dumps(obj, ensure_ascii=True)


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    docx_info = build_docx()
    pdf_info = build_pdf()
    png_info = build_png()
    stamps, ts = build_transcript()
    key = build_key(stamps, ts, docx_info, pdf_info, png_info)
    text = dump(key, 0, 2) + "\n"
    json.loads(text)
    with open(os.path.join(OUT, "answer-key.json"), "w", encoding="ascii") as f:
        f.write(text)
    print("docx", docx_info)
    print("pdf", pdf_info)
    print("png", png_info)
    print("transcript", json.dumps(ts))
    print("key: fields %d, lines %d, bytes %d" % (len(key), text.count("\n"), len(text)))
