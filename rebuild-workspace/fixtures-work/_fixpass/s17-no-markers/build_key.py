"""s17-no-markers fix pass: every change to answer-key.json, in the brief's order, by script.
Load, change, dump (keystyle.py reproduces the file's own layout byte for byte). Every quote the
readiness block introduces is looked up in the transcript at its stamp and label and must be a
verbatim substring of that turn before anything is written. Run once; the script refuses to run
twice (it checks that `readiness` and `direction` are absent first)."""
import json, re, sys, collections
sys.path.insert(0, "/Users/caramelm4/DelOps/rebuild-workspace/fixtures-work/_fixpass/s17-no-markers")
import keystyle

F = "/Users/caramelm4/DelOps/rebuild-workspace/fixtures/s17-no-markers/"
OD = collections.OrderedDict
raw = open(F + "answer-key.json", encoding="utf-8").read()
k = json.loads(raw, object_pairs_hook=OD)
assert keystyle.dumps(k) == raw, "round trip of the untouched key failed"
assert "readiness" not in k and "direction" not in k["intake"]["type_header"], "already applied"

# ---------- transcript, for quote proofs and counts ----------
lines = open(F + "transcript.txt", encoding="utf-8").read().split("\n")
hdr = re.compile(r"^(Consultant|Teodora Okoro|Rasmus Wrenfield|Ilse Salvesen) (\d\d:\d\d)$")
turns = []
i = 0
while i < len(lines):
    m = hdr.match(lines[i])
    if m:
        turns.append(dict(n=len(turns) + 1, label=m.group(1), stamp=m.group(2), text=lines[i + 1])); i += 2
    else:
        i += 1
by_stamp = {}
for t in turns:
    by_stamp.setdefault((t["stamp"], t["label"]), []).append(t)
words = lambda s: len(s.split())
TOTAL = sum(words(t["text"]) for t in turns)
BLOCK = next(t for t in turns if t["n"] == 183)
assert BLOCK["stamp"] == "21:36" and words(BLOCK["text"]) == 410
CLIENT = sum(words(t["text"]) for t in turns if t["label"] != "Consultant")
share = round(410 / TOTAL, 3)
cl_incl = round(100 * CLIENT / TOTAL)
cl_excl = round(100 * (CLIENT - 410) / (TOTAL - 410))
print("total words", TOTAL, "block share", share, "client incl/excl", cl_incl, cl_excl)

proofs = 0
def L(stamp, label):
    c = by_stamp[(stamp, label)]
    assert len(c) == 1, (stamp, label, len(c))
    return f"turn {c[0]['n']}, {stamp}, {label}"

def Q(stamp, label, text):
    """Prove `text` verbatim in the turn at (stamp, label); return (text, location)."""
    global proofs
    t = by_stamp[(stamp, label)][0]
    assert text in t["text"], ("NOT IN TURN", stamp, label, text[:60])
    proofs += 1
    return text, L(stamp, label)

SEGS = {s["k"]: s for s in k["intake"]["composite_blocks"][0]["segments"]}
def QS(kseg, text):
    global proofs
    s = SEGS[kseg]
    b = BLOCK["text"]
    a, z = b.index(s["from"]), b.index(s["to"]) + len(s["to"])
    assert text in b[a:z], ("NOT IN SEGMENT", kseg, text[:60])
    proofs += 1
    return text, f"turn 183, 21:36, labelled Teodora Okoro, segment {kseg} (side-only)"

def O(stamp, label, text):
    """An outcome string in the client's words: proven verbatim, returned as text only."""
    return Q(stamp, label, text)[0]

# ---------- 1. FEEDBACK entry for s17: stage 1b input only; no fixture change ----------

# ---------- 2. direction rename, position kept ----------
th = k["intake"]["type_header"]
k["intake"]["type_header"] = OD((("direction" if kk == "direction_of_show" else kk), v) for kk, v in th.items())
assert list(k["intake"]["type_header"].keys())[3] == "direction"

# ---------- 3. sweep: fields corrected (a builder reading the field alone would build the flaw) ----------
v = k["vocabulary"]
assert v[0]["their_term"] == "the avail"
v[0]["likely_monday_object"] = ("the Availability board (product lines rolled up from bed counts, each line showing the age of its count) "
    "plus the emailed export of it, stamped with the count date and the send time; a confirmation is checked on the board, "
    "never on the emailed copy (readiness leanings 4 and 5)")
assert v[1]["their_term"] == "bed / bed count"
v[1]["likely_monday_object"] = ("item on a Bed counts board, entered from a phone with the date it was counted, connected to the "
    "product line it rolls up to (readiness leaning 5)")

# ---------- 4. the "never written to" rule (FEEDBACK s14; s17 is one of the eleven keys) ----------
RULE = ("writeback and integration direction unresolved; v0.1 does not depend on either; staying clear of the "
        "accounting system is our safe default, labelled as ours")
im = k["integrations_mentioned"]
assert im[0].startswith("The accounting system: sales orders")
im[0] = ("The accounting system: sales orders, invoices, credits and the year end; stays as the invoicing system in the client's "
         "words ('And the accounting system stays.'); " + RULE + "; its stock module was tried and abandoned")
cs = k["compliance_or_security_signals"]
assert cs[3].startswith("The accounting system is the book of record")
cs[3] = ("The accounting system is the book of record for orders, invoices and credits (the client's words: it stays, she "
         "invoices out of it, the accountant and the owner read it); " + RULE)
rc = k["requested_changes"]
assert rc[2]["quote"] == "And the accounting system stays."
rc[2]["description"] = ("Pre-build constraint: the accounting system stays the invoicing system (the client's words); " + RULE + ".")
es = k["expected_structures"]
old = "the accounting system is never written to;"
assert old in es["notes"]
es["notes"] = es["notes"].replace(old, "the accounting system stays the invoicing system, with " + RULE + ";")

# ---------- 5. standing lines where they bite ----------
# s21: a commitment is committed, with owner, purpose and when; done only on evidence
c0 = k["commitments_and_next_steps"][0]
assert c0["what"].startswith("Walkthrough of a first version")
c0["what"] = ("Committed on the call: walkthrough of a first version (availability, orders, quotes) at the nursery with Teodora, "
              "Rasmus and Ilse; the owner to be brought by Teodora once the invite reaches him (attendance not yet confirmed); "
              "the bookkeeper to be asked by Ilse (offered at turn 242, not confirmed with her); forty-five minutes. "
              "Nothing is sent or confirmed yet")
c0["owner"] = "Consultant (hosts; sends the invite); Teodora forwards it to the owner and frames the session for him"
# s22: a board status set by a person is a claim, never evidence that the source system changed
assert v[9]["their_term"] == "standing order"
v[9]["likely_monday_object"] = ("item on the Orders board with a recurrence and a cancelled status, set by whoever reads the "
    "chain's email, that notifies the grower; the status is a claim about the email, not evidence of it")

# ---------- counts moved by the mess pass (brief section 5) ----------
tf = k["transcript_format"]
assert "about 5,612 spoken words" in tf
k["transcript_format"] = tf.replace("about 5,612 spoken words", f"about {TOTAL:,} spoken words")
ef = k["intake"]["export_family"]
assert ef["words"] == 5612
ef["words"] = TOTAL
cb = k["intake"]["composite_blocks"][0]
assert cb["share_of_file_words"] == 0.073
cb["share_of_file_words"] = share
ts = k["intake"]["silence"]["talk_share"]
assert "7.3 percent" in ts["reason"]
ts["reason"] = ts["reason"].replace("7.3 percent", f"{100*share:.1f} percent")
assert ts["if_computed_anyway"].startswith("about 69 percent client by words with the block counted under its label, or 67 percent")
ts["if_computed_anyway"] = (f"about {cl_incl} percent client by words with the block counted under its label, or {cl_excl} percent "
                            "with the block excluded; reported only as an estimate labelled unreliable, never as the call's share")
tr = k["traps"]
assert tr[5].startswith("Talk share is refused: the composite block holds 7.3 percent")
tr[5] = tr[5].replace("7.3 percent", f"{100*share:.1f} percent")

# ---------- 6. the readiness block ----------
SM, GR, OF = "sales manager", "grower and production manager", "office and despatch coordinator"
P = k["pains"]
def pain(pid, idx, role, se, outcome):
    e = P[idx]
    return OD(id=pid, quote=e["quote"], location=e["location"], speaker_role=role, stated_or_excavated=se, outcome=outcome)
out_T1 = O("20:18", "Teodora Okoro", "want to say yes to a customer and know it's true. That's it.")
out_T2 = O("20:18", "Teodora Okoro", "I want to look at a line and say yes, three hundred, Thursday, and not phone anybody.")
out_R1 = O("20:29", "Rasmus Wrenfield", "I want to see what's sold before I pot on.")
out_R2 = O("20:29", "Rasmus Wrenfield", "I want to see what's sold before I pot on. And I want to see it on my phone, standing in the tunnel, not on a printout from Friday.")
out_I1 = O("20:39", "Ilse Salvesen", "I want to stop building the avail on a Monday morning by hand.")
pains = [
    pain("P1.1", 0, SM, "excavated", out_T1),
    pain("P1.2", 1, SM, "excavated", out_T2),
    pain("P1.3", 2, OF, "excavated", None),
    pain("P2.1", 3, GR, "excavated", out_R1),
    pain("P2.2", 4, GR, "excavated", out_R2),
    pain("P3.1", 5, SM, "stated", None),
    pain("P3.2", 6, GR, "stated", None),
    pain("P4", 7, OF, "stated", out_I1),
    pain("P1.4", 8, OF, "stated", None),
    pain("P5", 9, OF, "stated", None),
    pain("P6", 10, GR, "stated", None),
]
assert len(pains) == len(P) == 11

def sig(q, pain_id, nc):
    return OD(quote=q[0], location=q[1], pain=pain_id, not_confirmed=nc)
signals = [
    sig(Q("21:08", "Teodora Okoro", "He'd say he wants to walk the tunnels with it on a tablet and see bed twelve on the screen and see that it matches bed twelve."),
        "P1.1", "the owner's own test; relayed by the sales manager, recorded by the Consultant 'as his, from you' (turn 180), and never heard from him"),
    sig(QS(3, "Anything over ten thousand a year on a system, or anything that touches the accounting side, that's him, he signs it."),
        None, "who spoke, and whether the threshold and the delegation are the owner's; the segment is speaker-unresolved and side-only, so the decision process beyond 'the owner signs' rests on it until the owner confirms it in person"),
    sig(QS(1, "So I've got, what, forty of those live at any one time and they're in my sent folder."),
        "P3.1", "who spoke; the live-quote count and the spreadsheet-per-schedule workaround are side-only until the user confirms the speaker"),
    sig(Q("24:54", "Teodora Okoro", "Never again. That's exactly it."),
        "P3.2", "a closed yes to our own framing at turn 186; evidence that the avail is checked once at pricing, not of the framing around it"),
    sig(Q("15:57", "Teodora Okoro", "Their buyer said it. I'm not counting it till the trial's done. But yes."),
        "P2.2", "the chain's figure and its terms; relayed from the buyer, refused as a count by the client, and never asked of the chain"),
    sig(Q("29:43", "Teodora Okoro", "if this replaces that he'll fight it quietly."),
        "P5", "the sales coordinator's own view; he was not on the call, and the Consultant has yet to meet him (turn 226)"),
]

def ent(name, parent, mi, sr, gs, src, ev):
    return OD(name=name, parent=parent, moves_independently=mi, shared_resource=sr, goes_stale=gs, source=src, evidence=ev)
T, R, I = "Teodora Okoro", "Rasmus Wrenfield", "Ilse Salvesen"
entities = [
    ent("Availability list (the avail)", None, "yes", False, True, "spoken", L("05:45", T)),
    ent("Product line (species, cultivar, size)", "Availability list (the avail)", "yes", True, False, "spoken", L("03:43", I)),
    ent("Bed (a numbered growing bed)", None, "yes", False, False, "spoken", L("14:24", I)),
    ent("Bed count", "Bed (a numbered growing bed)", "yes", False, True, "spoken", L("03:43", I)),
    ent("Friday clipboard sheet", "Bed count", "no", False, True, "spoken", L("03:43", I)),
    ent("Emailed availability (Monday, and Wednesday for the chain)", "Availability list (the avail)", "no", False, True, "spoken", L("17:27", I)),
    ent("Customer account (landscaper, garden centre, the chain, parks department)", None, "yes", False, False, "spoken", L("01:44", T)),
    ent("Price (list, tier, contract)", "Customer account (landscaper, garden centre, the chain, parks department)", "yes", False, False, "spoken", L("05:12", T)),
    ent("Order (sales order)", "Customer account (landscaper, garden centre, the chain, parks department)", "yes", False, False, "spoken", L("04:25", T)),
    ent("Order line", "Order (sales order)", "yes", False, False, "spoken", L("18:01", I)),
    ent("Reservation (a confirmed order line against a product line; our word for 'spoken for')", "Order line", "no", False, False, "assumed", L("18:59", T)),
    ent("Pick list", "Order (sales order)", "no", False, True, "spoken", L("04:38", I)),
    ent("Delivery (a driver's run; the signed pick list back)", "Order (sales order)", "yes", False, False, "spoken", L("18:01", I)),
    ent("Refusal or substitution", "Order line", "yes", False, False, "spoken", L("08:46", I)),
    ent("Credit (raised in the accounting system)", "Order (sales order)", "yes", False, False, "spoken", L("08:11", I)),
    ent("Standing order (the chain's recurring order)", "Order (sales order)", "yes", False, True, "spoken", L("12:30", R)),
    ent("Pre-order (the chain's March trial, a season ahead)", "Order (sales order)", "yes", False, True, "spoken", L("16:02", R)),
    ent("Purchase order number (parks departments)", "Order (sales order)", "yes", False, False, "spoken", L("18:24", I)),
    ent("Plant schedule (quote)", "Customer account (landscaper, garden centre, the chain, parks department)", "yes", False, True, "spoken", L("18:44", T)),
    ent("Quote line", "Plant schedule (quote)", "yes", False, True, "spoken", L("24:59", R)),
    ent("Potting batch (pot on)", "Product line (species, cultivar, size)", "yes", False, False, "spoken", L("11:49", R)),
    ent("Field stock (lifted in winter)", "Product line (species, cultivar, size)", "yes", False, False, "spoken", L("01:44", T)),
    ent("Crew lead (the four leads)", None, "unknown", False, False, "spoken", L("02:53", R)),
    ent("Trucks and drivers (three drivers, two trucks and a van)", None, "unknown", True, False, "spoken", L("18:01", I)),
    ent("Bed map (the drawing on the yard office wall)", None, "no", False, True, "documented", L("32:52", R)),
    ent("The sales coordinator's purchase-order spreadsheet", None, "yes", False, True, "spoken", L("18:24", I)),
    ent("The sales coordinator's task-app list", None, "unknown", False, True, "spoken", L("29:43", T)),
]

PAT = ["one row where the call describes many", "a pain with no element that fixes it", "an alias-map entry that names more than one entity",
       "our framing labelled as the client's", "a shared resource with no reservation tracking",
       "an artefact that can go stale with nothing to flag it", "an expected output the input cannot support"]
def lean(question, option, qs, condition, pattern):
    assert pattern in PAT
    return OD(question=question, option=option, quotes=[q[0] for q in qs], locations=[q[1] for q in qs], condition=condition, pattern=pattern)
leanings = [
    lean("Is an order one row with one status, or a parent with one row per line?",
         "Order as the parent row; order lines as child rows, each connected to its availability line, with reservation, substitution and refusal per line and the order's status rolled up",
         [Q("07:52", T, "And the garden centre got the forty that were left and a hundred and sixty of something else that Rasmus found, a different cultivar,"),
          Q("18:01", I, "The pick list, signed, with anything refused crossed off."),
          Q("06:47", I, "And then they come back and change the order I've already printed.")],
         "how many lines an order carries in season and whether the yard pulls by line; settled by the avail spreadsheet and a sample of pick lists from the office coordinator",
         PAT[0]),
    lean("Where is the order keyed: once on the board, or twice, as the stock module was?",
         "Keyed once, on the Orders board; the pick list prints from it; the office coordinator raises the sales order and invoice in the accounting system from the signed pick list, as she invoices today; nothing writes to the accounting system in v0.1 and the direction stays unresolved",
         [Q("04:25", T, "we write it up as a sales order in the accounting system,"),
          Q("04:38", I, "I invoice off the pick list when the driver's paperwork comes back."),
          Q("14:24", I, "So I was typing it twice and it was still wrong. It lasted a season."),
          Q("28:06", I, "And the accounting system stays. I invoice out of it, the accountant does the year end out of it, Gunnar reads the reports out of it.")],
         "whether the accounting system needs the sales order before a pick list can exist (pick lists print from it today) and whether the office coordinator accepts raising it at invoice time; asked at the walkthrough",
         PAT[5]),
    lean("Does a live quote hold stock, and how does the grower see what is promised?",
         "Quote lines as child rows of the quote, each connected to its availability line and shown there as promised without dropping the line; no quote holds stock until the client says one should",
         [Q("24:59", R, "So I could be holding four hundred Thuja for a bid that lost, or I could sell them to a garden centre and the bid wins. I don't know which."),
          Q("18:59", T, "because nothing on the avail said they were spoken for"),
          Q("19:45", T, "And Rasmus, because I've now promised his plants twice, once to the landscaper in March and once to whoever bought them in")],
         "whether a live quote should reserve stock at all, for how long, and whether the owner's over-fifteen-thousand quotes differ; the client has not said, so the first version shows promised quantities only",
         PAT[4]),
    lean("What stops the emailed list being the same stale artefact with a new source?",
         "The Monday and Wednesday emails are exports of the Availability board stamped with the count date and the send time; the fifty-unit confirmation is checked on the board, never on the emailed copy",
         [Q("05:45", T, "So it's wrong before it's sent."),
          Q("31:25", I, "And the customers still get the email."),
          Q("06:25", T, "If it's over fifty units of anything I don't confirm it till one of us has looked at the bed. That's the rule.")],
         "the send mechanism (an export the office coordinator sends, an automation, or an integration) and whether the chain's Wednesday list continues; settled with her before the thirteenth",
         PAT[5]),
    lean("How fresh is a count once it comes from a phone?",
         "Each bed count carries the date it was taken; the availability line is the latest count less the confirmed order lines since that count, and shows the count's age; the build does not make counting more frequent",
         [Q("03:43", I, "So on Friday Rasmus or one of the leads walks the beds with a clipboard and counts. Every bed, every size."),
          Q("26:57", R, "The avail, but the avail is only right if the counts come from the beds, from my leads, on their phones.")],
         "how often the leads will count once entry is a phone, and whether one bed can be recounted on its own; asked of the grower",
         PAT[5]),
    lean("What happens to a refused line when the plants come back?",
         "A refused status on the order line that returns the quantity to its availability line or flags it for the grower to recount, so a returned plant is sold again instead of found on the dock",
         [Q("18:01", I, "They ring me from the road if it's a refusal and I try to find a home for it before they get back,"),
          Q("18:17", R, "and I find it Monday. Two weeks later, sometimes.")],
         "whether a refused plant goes back on the bed as saleable and who decides; the grower, asked at the walkthrough",
         PAT[1]),
    lean("Where does a parks purchase-order number live?",
         "A purchase-order-number column on the order for parks accounts, required before the order is invoiced, replacing the sales coordinator's own spreadsheet only when he agrees",
         [Q("18:24", I, "They want a purchase order number on everything or they won't pay."),
          Q("18:24", I, "So Kenji has to chase the number before I can invoice, and that's a separate spreadsheet that only he understands.")],
         "the sales coordinator's own list and his willingness; the Consultant has yet to meet him; not in the first version",
         PAT[1]),
    lean("What is the chain's season-ahead pre-order against: counted stock, or planned production?",
         "A pre-order is an order row with a delivery season, reserving against planned production rather than a counted bed; out of the first version until the March trial is confirmed, with the cancelled-order notification covering it when it comes",
         [Q("16:02", R, "And if we get it, the blind bit gets worse, not better, because now I'm growing to an order I can't see."),
          Q("16:11", R, "If they pre-order six thousand hydrangea in March for September, I need to know that in March, and I need to know if they cancel it in July,")],
         "the March trial and the shape of the chain's pre-order; nothing is built for it before the trial is confirmed",
         PAT[0]),
]

def epp(p, element, verdict):
    assert verdict in ("fixes", "copies-today's-tool", "none")
    return OD(pain=p, element=element, verdict=verdict)
element_per_pain = [
    epp("P1.1", "Availability lines rolled up from phone bed counts, with a confirmed order line dropping the line for everyone (leanings 1 and 5)", "fixes"),
    epp("P1.2", "The board as the live source; the emailed copy stamped with its count date and send time; confirmation checked on the board (leaning 4)", "fixes"),
    epp("P1.3", "Substitution status and reason on the order line; fewer substitutions follow from a true list; the credit itself is still raised by hand in the accounting system", "fixes"),
    epp("P1.4", "none today; leaning 6 proposes a refused status that returns the quantity to its line", "none"),
    epp("P2.1", "Orders and promised quantities visible against the availability lines on the grower's phone", "fixes"),
    epp("P2.2", "A cancelled status on the order, standing orders included, that notifies the grower; the status is set by a person and is a claim about the chain's email, not evidence of it", "fixes"),
    epp("P3.1", "Plant schedules as deals on the native Deals/Opportunities board relabelled Quotes, one per schedule, with sent, won and lost states", "fixes"),
    epp("P3.2", "Quote lines connected to availability lines and shown there as promised (leaning 3); without the connection the board is the sent folder in monday", "fixes"),
    epp("P4", "The list generated from the Availability board instead of typed from the clipboard; the Monday and Wednesday sends are exports of it (leaning 4)", "fixes"),
    epp("P5", "none in the first version; leaning 7", "none"),
    epp("P6", "none: no element changes whose number the customers ring; fewer wrong lists mean fewer calls, which is P1's element, not this pain's", "none"),
]
assert {e["pain"] for e in element_per_pain} == {p["id"] for p in pains}

structure = OD(
    products=["Work Management", "CRM"],
    build_target="own-account",
    build_target_reason="prospect, so the user's own account by default (A21)",
    workspaces=["Fenwater \u2013 Ops", "Fenwater \u2013 CRM"],
    native_reuse=("CRM: the native Deals/Opportunities board relabelled 'Quotes' for plant schedules, and the native Accounts board for "
                  "landscapers, garden centres, the chain and the parks departments; Contacts only if named buyers are to be tracked, "
                  "which was never discussed. The Work Management boards (Bed counts, Availability, Orders) are built structure; "
                  "no native board is reused for them"),
    leanings=leanings,
    patterns=["parent-row-with-roll-up: product line (species, cultivar, size) with bed counts as child rows, available quantity and count age on the parent",
              "parent-row-with-roll-up: order with order lines as child rows, each line's reservation rolling up to its availability line, order status on the parent",
              "parent-row-with-roll-up: plant schedule (quote) with quote lines as child rows, promised quantity shown on the availability line"],
    element_per_pain=element_per_pain,
)

def inc(system, authority, ev):
    return OD(system=system, authority=authority, evidence=ev)
existing = OD(
    account=("none: the client has no monday account of any kind (account_context); under A21 the proof of concept goes into the "
             "user's own account, whose products and tier are read at preflight; the client's eventual account and who administers "
             "it (the office coordinator, by the client's own choice at turns 257 and 258) move to handover"),
    incumbents=[
        inc("The accounting system",
            "stays system of record for: sales orders as keyed today, invoices, credits, the year end and the owner's reports; follower for: nothing in v0.1 (its abandoned stock module is not revived); " + RULE,
            L("28:06", I)),
        inc("The availability spreadsheet",
            "stays system of record for: nothing once the Availability board is live; follower for: the emailed Monday and Wednesday lists, generated from the board; today's file seeds the product lines",
            L("32:42", I)),
        inc("The sales manager's sent folder and pricing spreadsheets",
            "stays system of record for: the pricing arithmetic on a plant schedule and the owner's paper pricing over fifteen thousand; follower for: the quote register, which moves to the Quotes board",
            "turn 183, 21:36, labelled Teodora Okoro, segment 1 (side-only)"),
        inc("Email to customers",
            "stays system of record for: nothing; stays the channel for: the availability list and outgoing quotes; customers never log in",
            L("31:25", I)),
        inc("The Friday clipboard and the yard office board",
            "stays system of record for: nothing once counts and pick lists are on phones; follower for: nothing; the paper stays as the fallback the client has not asked us to remove",
            L("03:43", I)),
        inc("The sales coordinator's purchase-order spreadsheet and task app",
            "stays system of record for: parks purchase-order numbers and his own list of who wants what, until he agrees otherwise; follower for: nothing",
            L("18:24", I)),
        inc("The bed map on the yard office wall",
            "stays system of record for: bed numbers and positions (the numbers are still on the posts); follower for: the Bed counts board's bed list, seeded from the photo",
            L("32:52", R)),
    ],
)

def asm(s, q):
    return OD(statement=s, question=q)
assumptions = [
    asm("A product line is species plus cultivar plus size; one bed holds one line at a time and one line spans several beds.",
        "Can a bed hold more than one line, and how many beds does a line span in spring?"),
    asm("The list price is the only price on any board a lead can see; tier and contract prices stay in the sales manager's hands.",
        "Which prices, if any, may appear on the Orders and Quotes boards, and who may see them?"),
    asm("In v0.1 the Monday and Wednesday lists are exports the office coordinator sends from the board; an automated send is a later element.",
        "Which columns go out, to which list, at what time, and does the Wednesday list for the chain continue?"),
    asm("The order is keyed once, on the Orders board, and the office coordinator raises the accounting sales order and invoice from the signed pick list (leaning 2).",
        "Does the accounting system need a sales order before a pick list can exist, and is she willing to raise it at invoice time?"),
    asm("A confirmed order line drops the availability line for everyone at once; the fifty-unit rule becomes a check on the board.",
        "Who confirms an order over fifty units once the count is live, and does the rule stay?"),
    asm("Counting stays weekly, on Friday; the build shows a count's age and does not change its rhythm.",
        "How often will the leads count once it is a phone, and can one bed be recounted on its own?"),
    asm("A plant schedule is one deal with lines as child rows; the owner's over-fifteen-thousand quotes are the same shape with the owner as approver.",
        "Which fields of the pricing spreadsheet belong on a quote line, and are the owner's quotes handled differently?"),
    asm("A live quote shows as promised on the availability line and reserves nothing (leaning 3).",
        "Should a live quote hold stock, and for how long?"),
    asm("A substitution is recorded on the order line with a reason; the credit is still raised by hand in the accounting system, and the reason on the line is the record the credit lacks today.",
        "Should the credit's reason be copied from the order line, and by whom?"),
    asm("The pre-order trial, potting batches and field stock are out of the first version.",
        "If the March trial is confirmed, what does the chain's pre-order look like line by line?"),
    asm("The seasonal crew only read a pick list on a phone and never enter anything; there is no training for a different forty people each spring.",
        "What does a crew member need to see on a pick list, and on whose phone?"),
    asm("The walkthrough on the thirteenth runs on sample data in the user's own account: product lines and bed numbers from the spreadsheet and the bed map once they arrive, customer names and credit amounts invented.",
        "What may the avail spreadsheet and the credits list seed, and what is invented? (for the user, at preflight)"),
    asm("Contacts are out; accounts are enough for the first version.",
        "Are named buyers or estimators at the landscapers and the chain to be tracked?"),
    asm("Rain and gloves are met by one number per bed typed on a phone, with a photo as the fallback; nothing in the product guarantees it.",
        "Which phones do the leads carry, and does a gloved hand work on them?"),
    asm("The decision process is as the clean turns say it: the owner signs. The threshold, the delegation and the bookkeeper's review inside the block are unconfirmed.",
        "What is the owner's own threshold, and does he want the sales manager and the grower to pick?"),
]

def need(n, clock, why):
    return OD(need=n, clock=clock, why_not_met=why)
unmet_needs = [
    need("Phone entry that works in the rain with gloves on", "before spring; the avail right by the first week of February",
         "a device and interface requirement no board setting guarantees; stays a named requirement for the walkthrough, tried on the leads' own phones (turn 253)"),
    need("The Monday list reaching about a hundred and forty customers as an emailed attachment without anyone typing it", "first week of February",
         "the send is a workflow or integration question not settled on the call; v0.1 shows the list and its export, not the send (leaning 4)"),
    need("Prices invisible to the leads", "before any lead has a login",
         "column-level visibility depends on the tier of the account the client eventually buys, which is unknown; in the user's own account the proof of concept keeps prices off the boards leads see"),
    need("A system the seasonal crew can use with no training", "every spring, a different forty people",
         "met only if the crew never touch anything but a phone view of a pick list; not probed on the call (turn 223)"),
    need("Refused deliveries found and resold instead of sitting on the dock", None, "no element yet; leaning 6"),
    need("Parks purchase-order numbers out of one person's spreadsheet", None, "not in the first version; the sales coordinator has not been met (leaning 7)"),
    need("Credits with a reason the office can report on", "the credits list arrives by the Friday after the call",
         "the credit stays in the accounting system, whose reason field nobody fills; the order line carries the reason and the accounting credit does not, until a direction is agreed"),
]

def ai(p, kind, probe, idea):
    assert kind in ("agent", "ai_column", "workflow", "vibe_app", "sequence") and probe in ("P-19", "P-20", "P-21", "unprobed")
    return OD(pain_or_need=p, kind=kind, round=2, probe_basis=probe, idea=idea)
ai_opportunities = [
    ai("P2.2", "workflow", "P-21", "A workflow that tells the grower on his phone when an order against a line he is growing is confirmed or cancelled, standing orders included, instead of a Friday printout."),
    ai("P3.1", "ai_column", "unprobed", "An AI column that reads an emailed plant schedule into quote lines (species, size, quantity) so the sales manager prices from the board rather than retyping sixty lines."),
    ai("P3.2", "agent", "P-19", "An agent, limited to the client's workspaces, that flags a line promised on a live quote and sold on an order in the same week to the grower and the sales manager."),
    ai("P1.3", "ai_column", "unprobed", "An AI column that drafts the credit reason from the driver's refusal note on the order line, for the office coordinator to confirm."),
]

verdict = OD(
    cleared_for="build",
    conditions=[
        "approval stop",
        "no A11 question first matters for an own-account build (A21: sample data in the user's own account needs no decision); the three A11 decisions stay open",
        "the user confirms who spoke each segment of turn 183 before the decision process or the quote workaround is treated as attributed; until then both are side-only",
        "leaning 2 (where the order is keyed) answered by the office coordinator, or carried as assumption 4 into the walkthrough and said so on the card",
        "the walkthrough on Tuesday the thirteenth at four is committed, not held: the invite is to be sent, the owner's attendance to be confirmed by the sales manager, the bookkeeper to be asked",
        "seeds from the avail spreadsheet and the credits list only once they arrive, names and amounts removed; everything else sample data",
    ],
    reason=("Three pains carry a named entity and a wanted outcome in the client's words (the availability line, the order, the quote), "
            "two products are chosen in the client's order, the structure is stated with eight leanings and three roll-up patterns, "
            "and the build target is the user's own account."),
)

def qn(text, kind, role, known):
    assert kind in ("read-back", "discovery")
    return OD(text=text, kind=kind, role=role, known=known)
questions = [
    qn("Read back what the call recorded about decisions: that nothing is bought without his nod, that anything over ten thousand a year on a system or touching the accounting side is his to sign, that under that he wants the sales manager and the grower to pick, and that the bookkeeper looks at anything touching the accounting system. Which of that is his, and what is his test for the first version?",
       "read-back", "the owner, in person at the walkthrough, with the sales manager",
       "clean turns 12 and 237: the owner decides. The threshold, the delegation and the bookkeeper's review come only from the composite block (turn 183, segments 3 and 4), speaker-unresolved and side-only; the tablet test at turn 179 is relayed by the sales manager; the Consultant committed at turn 184 to ask him in person."),
    qn("Does the accounting system need a sales order before a pick list can exist, or can the sales order and the invoice be raised from the signed pick list once the order lives on the board? Who keys what, and when?",
       "discovery", "office and despatch coordinator",
       "today the sales order is keyed in the accounting system and the pick list prints from it (turn 35); the invoice is raised off the signed pick list (turn 36); the stock module failed because counts were typed twice (turn 124); the accounting system stays (turn 212); writeback is unresolved and v0.1 does not depend on it."),
    qn("How many beds are there, how are they numbered, can one line span several beds and one bed hold several lines, and how often will the leads count once it is a number on a phone?",
       "discovery", "grower and production manager",
       "counts are by bed, every bed, every size, on Friday (turn 31); the stock module wanted them by product (turn 124); the counts must come from the leads' phones, by bed (turns 202, 233); the bed map photo is coming (turn 248); the owner's test is bed twelve on a tablet, relayed (turn 179)."),
    qn("Read back the grower's words, holding four hundred Thuja for a bid that lost or selling them and the bid wins, and the forty live quotes in the sent folder: should a live quote hold stock, for how long, and who described the pricing workaround in the long passage at 21:36?",
       "read-back", "sales manager and grower",
       "turns 188 and 164 are clean; the forty live quotes and the spreadsheet-per-schedule workaround are side-only (turn 183, segment 1); turn 187 is a yes to our framing; quotes are third in the client's order and may trail bid season (turn 205)."),
    qn("For the emailed list: which columns go out, to which list, at what time on Monday, does the Wednesday list for the chain continue, and is the list price the only price that may appear on any board a lead can see?",
       "discovery", "office and despatch coordinator and sales manager",
       "about a hundred and forty customers, Monday by ten (turns 31 and 33); Wednesday again for the chain (turn 149); customers want the email and will not log in (turns 176, 235); a list price on the avail, tiers, a contract price and list for parks, none of it on a lead's screen (turn 42)."),
]
assert len(questions) <= 5

k["readiness"] = OD(
    schema="readiness/1",
    note=("Derived from this key's pains, entities, products, structure, forks and questions in the fixture fix pass of 2026-10-13. "
          "Structure assertions stay provisional until the user has seen a real build (FEEDBACK, top)."),
    pains=pains, signals=signals, entities=entities, structure=structure, existing=existing,
    assumptions=assumptions, unmet_needs=unmet_needs, ai_opportunities=ai_opportunities, verdict=verdict, questions=questions,
)

# ---------- checks before writing ----------
blob = json.dumps(k["readiness"], ensure_ascii=False)
for pat in (r"\bR\d{1,2}\b", r"\bPartial\b", r"\bMissing\b", r"\bMet\b", r"Nearly ready", r"Discovery complete", r"Not ready", r"\bgate", r"met-with-residual"):
    assert not re.search(pat, blob), ("sales word in block", pat)
assert list(k.keys())[-1] == "readiness" and len(k) == 27
for e in entities:
    if e["parent"] is not None:
        assert e["moves_independently"] in ("yes", "no", "unknown")
print("quote proofs in the block:", proofs)
out = keystyle.dumps(k)
json.loads(out)
open(F + "answer-key.json", "w", encoding="utf-8").write(out)
print("written", len(out.split("\n")) - 1, "lines; ascii:", out.isascii())
print("counts: pains", len(pains), "signals", len(signals), "entities", len(entities), "leanings", len(leanings),
      "epp", len(element_per_pain), "incumbents", len(existing["incumbents"]), "assumptions", len(assumptions),
      "unmet", len(unmet_needs), "ai", len(ai_opportunities), "questions", len(questions))
