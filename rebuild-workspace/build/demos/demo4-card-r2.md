# Approval card: sales pipeline v0.2, revision 2 (finishing the follow-up workflow)

Industrial supplies distributor, Toledo. Version v0.2, revision 2, frozen (sha256 starts `bc57a91d`). Written by the main session at the user's word ("Yes, plan v0.2 r2 with the two mirror columns and the workflow fix, and show me the card."). It finishes the one piece revision 1's build left undone and changes nothing else. One yes covers the whole card.

## 1. Where

The same account, the CRM test workspace, and the folder "Industrial supplies distributor, Toledo – CRM". Only the Opportunities board and the draft workflow already in the folder are touched.

## 2. What this build rests on

Unchanged from revision 1. The follow-up draft is still an assumed term, not from the call: on the morning a quoted deal's follow-up date arrives, at 8:00, only when Stage is Quoted; it drafts a next step, sets Follow-up check to Waiting and notifies you; the owner confirms by hand.

## 3. The boards

Opportunities gains two columns, both mirrors of links every deal already has:
- **Account name:** the linked customer's name, from Account.
- **Contact name:** the linked contact's name, from Contacts.

Nothing else changes on any board.

## 4. Views, forms and the dashboard

Nothing new.

## 5. Automations and the AI layer

**Quiet quote follow-up draft**, the workflow revision 1's build left unpublished, finished in place (no second workflow is made):

| step | what it does |
|---|---|
| trigger | the Next follow-up date arrives, 8:00 in the account's time zone |
| condition | only when Stage is Quoted |
| AI step | drafts the next step from the quote's columns, now reading Account name and Contact name |
| change a column | writes the draft into Drafted next step |
| change a column | sets Follow-up check to Waiting |
| notify | you only: "Follow-up drafted for [Name]: [the draft]. Set Follow-up check to Confirmed when it is done." |

- **One more test run** on "Harborview Metal Works stocking agreement": it rewrites that deal's Drafted next step, sets it to Waiting, and sends you one notification.
- **Then published switched on.** From then on it runs on each Quoted deal whose follow-up date arrives, sending you one notification each time; among the sample quotes that is eleven deals, from 26 October to 12 November (read from the board on 2026-10-23).

Prompt for the AI step:

```text
Draft the next follow-up step on this quote, for its owner to confirm.
Quote: [Name], for [Account name], contact [Contact name].
Quote number [Quote number], type [Quote type], deal value [Deal value].
Last logged contact [Last activity]; follow-up due [Next follow-up].
Write one or two sentences the owner can act on today: who to contact, what to ask, and one reason to get in touch now, such as the stock held on the shelf for a stocking agreement. Use only the facts above. Never invent a price, a discount, a date, a product or a person's name, and never write to the customer: this note is for the owner.
```

The workflow's AI step uses the account's AI. No credit figure is given.

## 6. Sample data

None new. The two name columns fill from the links all 32 sample quotes already have.

## 7. Hard to undo

- Two more columns on the CRM's own Opportunities board; a column added to it is not removed by the build.
- The workflow's publication cannot be taken back through the API; switching it off is a step in monday (U8).
- The AI columns built in revision 1 stay on; the demonstration's boards are yours to clear afterwards (A42).

## 8. Left for you in monday

- U6: add the Enquiry question to the New lead form.
- U7: run the forecast job once, or wait for 1 November, and read the note.
- U8: switch the workflow off when the demonstration is over.
- U9 and U10 close when the build publishes the workflow.

## 9. Build checks

- **Unproved: a mirror of a linked item's name.** monday's own mirror schema shows it as its example. *Fallback:* the mirror departs with its reason, and the workflow stays an unpublished draft with U9 and U10 open.
- **The AI step's fields:** given all at once in the first request that touches the step, then checked one by one for a real field rather than plain text (G-136); the test run is the proof: the draft must name Harborview's real customer and contact and hold no column id.
- The condition, the trigger time and the notify step were set and read back in revision 1's build; they are read back again before the test run.

## 10. Lint warnings

None. The frozen revision is clean on the leak lint; the record check warns only that revision 2 is not yet approved, which the build's first step records.
