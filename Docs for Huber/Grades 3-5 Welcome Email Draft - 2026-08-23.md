# Grades 3–5 Welcome Email Draft - 2026-08-23

*For Coach Izenstark to send to each family after they register for the grades
3–5 session (Oct 16 – Nov 20).*

> **Updated later on 2026-08-23:** phone moved to Stripe's built-in collection,
> which freed the third custom field for "Anything we should know?" (optional).
> Checkout now asks too, so this email's medical ask is a **backstop rather than
> the only channel**. Keep it — optional fields get skipped, and parents often
> remember the inhaler after they've paid.

---

## When to send

Not a one-time blast. Send it **as registrations come in** — or in batches every
few days — pulling new families off
**roster.greenoaksathleticclub.com** → Grades 3–5 download.

> **Send BCC if you batch it.** Parent addresses go in BCC, never To or CC.

---

## Subject

```
Welcome to Green Oaks Athletic Club — grades 3–5 details inside
```

## Body

```
Hi, and thanks for registering!

Your child is in for the Green Oaks Athletic Club grades 3–5 fall session.
Here's everything you need, plus one quick thing I need back from you.

WHEN
Six Fridays, 3:30–4:30 PM, in the Junior High Gym.

  Week 1  —  Fri, Oct 16  —  Kickball
  Week 2  —  Fri, Oct 23  —  Soccer
  Week 3  —  Fri, Oct 30  —  "Bennis"  (baseball with a tennis racket — a club favorite)
  Week 4  —  Fri, Nov 6   —  Floor Hockey
  Week 5  —  Fri, Nov 13  —  Basketball   ** see note below **
  Week 6  —  Fri, Nov 20  —  Capture the Flag

ONE DATE TO WATCH
Friday, November 13 is an early-release day at school — but club still meets
at the regular time, 3:30–4:30 PM. Teachers aren't dismissed early, so nothing
about our schedule changes that day. Please plan pickup for 4:30 as usual.

WHAT TO BRING
Comfortable clothes, athletic shoes, and a water bottle. That's the whole list
— we provide all the equipment.

WEATHER
Club runs rain or shine. Some weeks we may head outside; when the weather
isn't right for it, we have the gym. Club is not cancelled for weather.

PICKUP
Kids head straight from class to the gym after school. Please pick up at 4:30
at the Junior High Gym.

>>> PLEASE REPLY IF ANY OF THIS APPLIES <<<
Just hit reply and tell me about anything that affects your child at club —
allergies, asthma or an inhaler, an EpiPen, a recent injury, or anything else
I should know to keep them safe and having fun. If your child carries
medication, tell me where they keep it.

If none of that applies, no reply needed.

Looking forward to a great six weeks.

Coach Izenstark
Green Oaks Athletic Club
greenoaksathleticclub.com
```

---

## Why the reply section stays

Checkout's notes field is **optional**, so plenty of parents will skip past it
in a hurry to pay — and medical details are exactly the thing people remember
afterwards. The email ask catches those. It also routes detail into Izenstark's
inbox rather than a payments system, which is where Stripe's own documentation
says health information should not live.

## Final checkout configuration (verified live 2026-08-23)

| Field | State |
|---|---|
| Email | required |
| Phone | required — Stripe built-in, lands in the roster's **Parent Phone** column |
| Child Name | required |
| Current Grade | required dropdown |
| Anything we should know? | optional |

Payment cap: **50** — no test charge was run on this link, so no +1 needed.

## Notes for Dave

- **No student PII in this document** — no names, no grades. Safe in the repo.
- Dates cross-checked against the live site and the 3–5 flyer.
