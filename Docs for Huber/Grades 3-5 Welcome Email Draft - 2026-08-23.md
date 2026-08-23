# Grades 3–5 Welcome Email Draft - 2026-08-23

*For Coach Izenstark to send to each family after they register for the grades
3–5 session (Oct 16 – Nov 20). Its real job is the last section — checkout no
longer asks about allergies or medical needs, so this email is where that
information gets collected.*

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

## Why the reply section matters

The K–2 payment link asked about allergies at checkout. The 3–5 link doesn't —
the third custom field is now Parent Cell Phone, and Stripe caps custom fields
at three.

That trade is defensible: Stripe's own documentation says not to collect
personal, protected, or sensitive data in custom fields, and a coach needs a
reachable phone number more than he needs a text box. **But it means this email
is now the only place medical information gets collected for grades 3–5.** If
this email doesn't go out, nobody knows which kid has the EpiPen.

Replies land in Izenstark's normal inbox rather than a payments system, which
is where health information belongs.

## Notes for Dave

- **No student PII in this document** — no names, no grades. Safe in the repo.
- Dates cross-checked against the live site and the 3–5 flyer.
- If you'd rather not depend on an email going out, the alternative is moving
  the phone number to Stripe's **built-in** phone collection (Options →
  "Require customers to provide a phone number"). That frees the third custom
  field to go back to "Anything we should know?" — you'd get both. See the
  note in the session summary.
