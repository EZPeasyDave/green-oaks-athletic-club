# Handoff - Goac - Grades 3-5 Session Launch - 2026-08-23

*The grades 3–5 fall session shipped end to end and is live. Nothing is blocked.
The next session starts from a working state, not a half-built one.*

## State at close

| Thing | State |
|---|---|
| greenoaksathleticclub.com | Live, 3–5 registration open, verified after deploy |
| Stripe 3–5 payment link | Live, all fields correct, cap 50 |
| Flyer + social cards | Built, rendered, public URLs verified 200 |
| Roster Worker | Split by session, deployed, **now on GitHub** |
| Parent emails | Both drafted and **handed to Izenstark 2026-08-23** |

## Grades 3–5 session

Six Fridays, **Oct 16 – Nov 20, 2026**, 3:30–4:30 PM, Junior High Gym, $120,
capped at 50. Kickball → Soccer → Bennis → Floor Hockey → **Basketball (Nov 13,
early release, club still meets 3:30)** → Capture the Flag. Coach Izenstark.

Site build is commits `8cbd092` → `8e4e366`. Assets are
`images/*-grades35.html` plus their rendered PNG/PDF, all published at
`greenoaksathleticclub.com/images/`.

**Session one (K–2) was removed from the site** mid-session — its payment link
deactivated, so nothing should point at it. What remains is one note above the
footer: session runs Aug 28 – Oct 2, a couple of spots left, email the coach.
The date range is deliberately kept there so already-paid families still have it.

## The Stripe payment link — read this before touching any future link

The 3–5 link launched **collecting nothing**: no child name, no grade, nothing.
A purchase would have produced a paid parent and no way to know which child.
Caught before any money moved; registration was pulled from the site for about
an hour while it was fixed.

**Final config, verified live by screenshot:**

| Field | State |
|---|---|
| Email | required (built-in) |
| Phone | required (**built-in**, → roster's Parent Phone column) |
| Child Name | required (custom) |
| Current Grade | required dropdown (custom) |
| Anything we should know? | optional (custom) |

Full pre-flight checklist is in project memory (`project_payments`). The three
things that cost time today:

1. **Custom fields cap at three.** Spending one on a phone costs you the notes
   field. Use Stripe's built-in phone collection instead — it is outside that
   budget and lands in `customer_details.phone`, which the roster already reads.
2. **The edit path is hidden.** Payment Links → the link → **`⋯` overflow menu**
   → Edit → *Options*. Dave could not find it; it is not on the details view.
3. **Verify by screenshot, never by trusting the dashboard.** The checkout page
   is JS-rendered so `curl` shows nothing, but headless Chrome shows exactly what
   a parent sees:
   `"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless --screenshot=out.png --virtual-time-budget=14000 "<buy.stripe.com URL>"`

Two for two now on links shipping with a missing setting — K–2 launched with no
payment cap, 3–5 with no custom fields. Treat it as expected, not unlucky.

**Cap is 50, not 51.** The +1 on K–2 existed only because a live test charge
consumed a slot. Don't cargo-cult it.

## Roster Worker — `~/Projects/home/goac-roster/`

**Now backed up: https://github.com/EZPeasyDave/goac-roster (private).** This
was the last unbacked-up piece of the system; `origin` is wired, future commits
push normally.

Split by club session, keyed on the Stripe **Payment Link ID** — each session
sells through its own link, which beats date cutoffs that go stale each term.
Per-session download buttons, plus a combined export with a leading Session
column. Unknown session param returns 404 with an explanation rather than an
empty CSV that reads like "nobody signed up."

Phone numbers render `(847) 555-1234`; anything not a recognisable US number
passes through as typed. 15 test assertions, all passing (`node test/roster.test.mjs`).

**One open item:** `SESSION_LABELS` in `wrangler.jsonc` labels K–2 only. Grades
3–5 has no `plink_` ID yet because **a session gets no group until its first paid
signup**. Once one lands, read the ID off the roster page and add it.

## Emails — handed off

**Dave shared both drafts with Izenstark on 2026-08-23, and Izenstark has them.**
Do not re-raise this as an open item.

- `Docs for Huber/Message to Izenstark - Two Emails to Send - 2026-08-23.md`
  — one paste-ready message carrying both, also in Obsidian.
- Individual drafts: `K-2 Schedule Email Draft - 2026-08-23.md`,
  `Grades 3-5 Welcome Email Draft - 2026-08-23.md`.

What remains is Izenstark actually sending them to parents, which is his to do
and outside this repo. The K–2 one is the time-sensitive one — that session
starts Friday Aug 28.

Note for any future send: it is manual. The Gmail MCP connector is installed but
**unauthenticated** (only the OAuth-start tools are exposed), and AgentMail's
domain is burned.

## Spring waitlist outreach — done and handed off

Late in the session Dave remembered the spring 2026 waitlist: kids turned away
from that session who are **now** in grades 3–5. Worth chasing — they already
asked once.

The grade rollover is the trap. Spring 2026 was the 2025–26 school year, so a
child eligible for 3–5 **now** was in **grade 2, 3, or 4** last spring, and
anyone who was in grade 5 has aged out into 6th. Dave ran a Gemini prompt
against his Oak Grove Workspace to pull the list and reconciled current grades
himself.

`Docs for Huber/Spring Waitlist Outreach Email Draft - 2026-08-23.md` is the
resulting email. **Sent to Izenstark to tweak and BCC**; parent addresses went
to him in a separate message. Nothing outstanding here.

Two things baked into that draft worth preserving in future outreach:

- **Link to `greenoaksathleticclub.com`, never the raw Stripe URL.** Emails get
  forwarded and read weeks later, and the payment link deactivates at the cap —
  a dead end costs a family.
- **State the real mechanic** ("capped at 50, first come, I can't hold a spot")
  rather than inventing urgency. It's true, and this list has already been let
  down once.

## How this club actually fills — don't over-invest in marketing

Dave, 2026-08-23: **the spring 2026 session hit its cap by word of mouth, before
the flyer or social posts ever went out.** Parents told other parents.

The flyer and both social cards are built and their URLs were handed to
Izenstark, who has them if he wants them. But treat promo assets as nice-to-have,
not as the thing that fills a session. The practical consequence: **a session can
fill faster than the site can be updated**, which is why the payment-link cap and
a working waitlist path matter more than any of the artwork. Also captured in
project memory.

## Dangling

- **The multi-club Google Form work is untouched** — that is the OGS school-wide
  thread from the 2026-08-22 handoff, still blocked on the club list with caps,
  and still needs the `RefreshChoices` script copied off the school Mac.

## Suggested skills for the next session

- **`/brief`** at the top — several GOAC threads plus the OGS multi-club one.
- **`/pipe`** for any read-and-review doc produced.
- No specialist skill needed.
