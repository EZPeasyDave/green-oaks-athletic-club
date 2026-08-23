# Handoff - Goac - Multi-Club Form And Session Rosters - 2026-08-22

*This session was design and archaeology only — no code was written and nothing
was deployed. Two build items are queued for the next session.*

## What this session actually produced

Dave asked how the spring 2026 GOAC form capped signups and flipped to a
waitlist, because the school now wants the same behavior across **a large number
of clubs**. The answer was recovered, and the design was extended for the new
shape.

### The spring mechanism, recovered

A hand-written Google Apps Script named `RefreshChoices` — the Choice Eliminator
pattern, not the paid add-on. Bound to the response Spreadsheet, on-form-submit
trigger. Counts responses per grade band, removes full options from the dropdown
via `FormApp`, and when everything fills it **rewrites the form title/description
and confirmation message** to waitlist wording instead of calling
`setAcceptingResponses(false)` — which is what avoided the dead "no longer
accepting responses" page.

- Form ID `1AEJaBnvS2DnCy7yQZcr27clQ2KcMxld8GdzowNYXRrQ`, on Dave's **Oak Grove
  account**.
- Cap was 25/band, raised to 30 in `c7084ed` (2026-03-24).
- **The script source is not on the Mac Studio.** It lives at
  `/Users/davehuber/Desktop/Tech Duties/Time Slot : Choice Eliminator/`
  (`RefreshChoices Script.txt` + `Choice Eliminator READ ME.txt`) — the school
  account. Getting that folder onto this machine is the first blocker for the
  multi-club build.
- Date correction for anyone searching: this was **spring 2026** (site commits
  March 2026, session archived 2026-05-07), not 2025. Dave misremembered it as
  "April of last year."

### The multi-club design (new)

The new form uses **one checkbox question listing every club**, so a parent's
picks land comma-joined in a single cell. That changes the approach:

- **Do not remove full options.** Rename them in place —
  `Chess Club` → `Chess Club — FULL (join waitlist)`. Removing an option from a
  checkbox list makes a stale browser tab error on submit, hides *which* clubs
  are full, and destroys the waitlist path. Renaming keeps the option checkable
  and makes the response row self-labeling.
- **Never `split(", ")` the cell.** Loop the canonical club list and test for
  presence — a club named with a comma in it breaks splitting, and someone will
  name one that way.
- **Normalize the `— FULL` suffix** before tallying, and count those toward the
  waitlist tally, not seats.
- **Re-tally the whole column every submit.** Cheap at a few hundred rows, and
  self-healing: delete a row by hand and the seat comes back.
- **Race handling:** a per-response status column (`Chess:enrolled;
  Lego:waitlist`) assigned in submission order. The label is what parents see;
  the status column is the truth.
- **Two payoffs worth building:** a per-club confirmation email from Apps Script
  (Forms' single confirmation message is useless when a parent got 3 of 5
  picks), and a live roster tab per club so sponsors self-serve.

**Blocked on:** the club list with caps, grade ranges, and any same-day
conflicts. Dave has not supplied it. This is separate from the GOAC work below —
it is an OGS school-wide thing.

## Queued for the next session

### 1. New build for the next GOAC session

Dave has an actual new session to stand up. **No details were captured this
session** — dates, price, grade band, coach, and cap are all unknown. Start by
asking. Prior sessions are the template:

- Fall K–2 build: commits `fd8ec87` → `801e08c` in `~/Projects/home/goac/`.
- Setup runbook: `Docs for Huber/Stripe Registration Setup - 2026-07-16.md`.
- **The cap lives on the Stripe Payment Link**, not the product — Payment Links
  → Edit → Options → Advanced → "Limit the number of payments." This was claimed
  done and was in fact never set (caught 2026-07-18). Verify it on the live link
  with your own eyes.

### 2. Roster download page — split by session

**The requirement:** Izenstark must be able to download *this next session's*
roster by itself.

**Current behavior (verified in code today):**
`~/Projects/home/goac-roster/src/index.js` `fetchPaidSessions()` pulls **every**
paid Checkout Session in the account with no date or product filter, and dumps
them into one CSV. Add a second session and the fall signups come along with it.

Pagination is already correct (`starting_after` loop, guard of 100 pages) — that
is not the problem, do not "fix" it.

**Discriminator options, best first:**

1. **`session.payment_link` ID** — each GOAC session gets its own Payment Link,
   so this is exact and needs no date guessing. Preferred.
2. `session.created` date ranges — works, but requires hardcoded cutoffs that go
   stale.
3. Line-item price/product ID — correct but a second API call per session.

**UI:** a session picker (dropdown or a button per session) rather than one
button, since Izenstark will want the current one by default and the old one
occasionally.

**Constraints that must not be re-litigated** — all in
`handoff-2026-08-10.md`: it stays a Cloudflare Worker (not the Mac Studio), the
repo stays outside `~/Projects/home/goac/` (that one publishes to GitHub Pages),
and both auth gates stay.

## Dangling from before, still open

Carried forward from `handoff-2026-08-10.md` — read it, these are not restated:

- `goac-roster` still has **no git remote**. Local commits only, no off-machine
  backup. Dave declined pushing it on 2026-08-10; worth re-asking before more
  code lands in it.
- Fall session was at **48 paid against a 51 cap** as of 2026-08-10 — likely
  full or closed by now; check before assuming.
- Cody's Zapier/Make → Google Sheet automation was never built.

## Suggested skills for the next session

- **`/brief`** at the top — several GOAC threads are live at once.
- **`/pipe`** for any read-and-review doc that comes out of it.
- No specialist skill needed for either build item.
