#!/usr/bin/env python3
"""Export GOAC Stripe Checkout Sessions -- including custom fields -- to signups.csv.

Stripe's built-in Payments CSV export walks charges, which do not carry Checkout
custom fields. Those live on the session object, so we pull them from the API.

Usage:
    STRIPE_API_KEY=rk_live_... .venv/bin/python export_signups.py
    .venv/bin/python export_signups.py          # prompts for the key

Use a RESTRICTED key with "Checkout Sessions: Read" and nothing else.
"""

import csv
import os
import sys
from datetime import datetime
from getpass import getpass

try:
    import stripe
except ModuleNotFoundError:
    sys.exit(
        "The 'stripe' package is not installed.\n"
        "Run:  python3 -m venv .venv && .venv/bin/pip install stripe\n"
        "Then: .venv/bin/python export_signups.py"
    )

OUTFILE = "signups.csv"

BASE_COLUMNS = [
    "session_id",
    "created",
    "customer_name",
    "customer_email",
    "customer_phone",
    "amount_total",
    "currency",
    "payment_status",
]


def get_api_key():
    key = os.environ.get("STRIPE_API_KEY", "").strip()
    if not key:
        print("Paste your restricted Stripe API key (input is hidden).")
        key = getpass("STRIPE_API_KEY: ").strip()
    if not key:
        sys.exit("No API key given -- nothing to do.")
    if key.startswith("sk_"):
        print(
            "\n  WARNING: that is a SECRET key (sk_), not a restricted key (rk_).\n"
            "  It can read and WRITE everything in the account. Consider creating a\n"
            "  restricted read-only key instead: Developers -> API keys -> Create\n"
            "  restricted key -> Checkout Sessions: Read.\n"
        )
    return key


def custom_field_value(field):
    """Pull the populated value out of a custom_fields entry.

    Each entry carries its value under a sub-object named for its type:
    text / dropdown / numeric. Dropdowns return the option's stored *value*,
    not the label shown to the parent (so "K" may come back as "k").
    """
    for kind in ("text", "dropdown", "numeric"):
        holder = field.get(kind)
        if holder:
            value = holder.get("value")
            if value not in (None, ""):
                return value
    return ""


def flatten(session):
    details = session.get("customer_details") or {}
    amount = session.get("amount_total")
    created = session.get("created")

    row = {
        "session_id": session.get("id", ""),
        "created": (
            datetime.fromtimestamp(created).strftime("%Y-%m-%d %H:%M") if created else ""
        ),
        "customer_name": details.get("name") or "",
        "customer_email": details.get("email") or "",
        "customer_phone": details.get("phone") or "",
        "amount_total": f"{amount / 100:.2f}" if amount is not None else "",
        "currency": (session.get("currency") or "").upper(),
        "payment_status": session.get("payment_status") or "",
    }

    custom = {}
    for field in session.get("custom_fields") or []:
        key = field.get("key")
        if key:
            custom[f"custom_{key}"] = custom_field_value(field)

    return row, custom


def main():
    stripe.api_key = get_api_key()

    print("\nFetching Checkout Sessions from Stripe...")
    rows = []
    custom_columns = []
    try:
        for session in stripe.checkout.Session.list(limit=100).auto_paging_iter():
            # to_dict() recurses, converting the whole StripeObject tree into plain
            # dicts. StripeObject supports [] but not .get(), so convert at the boundary.
            row, custom = flatten(session.to_dict())
            for column in custom:
                if column not in custom_columns:
                    custom_columns.append(column)
            row.update(custom)
            rows.append(row)
            if len(rows) % 100 == 0:
                print(f"  ...{len(rows)} sessions so far")
    except stripe.AuthenticationError:
        sys.exit(
            "\nStripe rejected that API key. Check it was copied whole and that you\n"
            "are looking at the same mode (live vs test) the payments were taken in."
        )
    except stripe.PermissionError:
        sys.exit(
            "\nThat key is missing permission to read Checkout Sessions.\n"
            "In Stripe: Developers -> API keys -> edit the restricted key ->\n"
            "set 'Checkout Sessions' to Read."
        )
    except stripe.StripeError as exc:
        sys.exit(f"\nStripe error: {exc}")

    if not rows:
        sys.exit(
            "\nNo Checkout Sessions returned.\n"
            "Most likely causes: the key is for TEST mode but payments were LIVE\n"
            "(or vice versa), or this key belongs to a different Stripe account."
        )

    # Union of every custom field key seen, so a session missing one field gets an
    # empty cell instead of a shifted row.
    columns = BASE_COLUMNS + sorted(custom_columns)

    with open(OUTFILE, "w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=columns, restval="")
        writer.writeheader()
        writer.writerows(rows)

    summarize(rows, custom_columns)


def summarize(rows, custom_columns):
    print(f"\nWrote {OUTFILE}")
    print(f"  sessions found : {len(rows)}")
    print(f"  rows written   : {len(rows)}")
    print(f"  custom fields  : {', '.join(sorted(custom_columns)) or '(none found)'}")

    paid = [r for r in rows if r["payment_status"] == "paid"]
    print(f"  paid sessions  : {len(paid)}")

    dates = sorted(r["created"] for r in rows if r["created"])
    if dates:
        print(f"  date range     : {dates[0]}  ->  {dates[-1]}")
        print(
            "\n  Sanity check: if the oldest date above is newer than your first real\n"
            "  signup, Stripe is not returning the full history and some sessions are\n"
            "  missing from this file. Compare the paid count against the Stripe\n"
            "  dashboard's payment count."
        )

    empty = [r for r in rows if not any(r.get(c) for c in custom_columns)]
    empty_paid = [r for r in empty if r["payment_status"] == "paid"]
    abandoned = len(empty) - len(empty_paid)

    # Only PAID sessions missing data are a problem. Abandoned carts have no
    # answers by definition -- listing them individually buries the real signal.
    if abandoned:
        print(
            f"\n  {abandoned} abandoned cart(s) with no custom fields -- this is NORMAL.\n"
            "  Stripe opens a session the moment someone clicks the button, before\n"
            "  they fill anything in. They did not pay and are not on your roster."
        )

    if not empty_paid:
        print("\n  OK: every PAID session captured its custom fields. Roster is complete.")
        return

    verb = "was" if len(empty_paid) == 1 else "were"
    print(
        f"\n  *** {len(empty_paid)} PAID session(s) {verb} missing custom field data. That is the\n"
        "  real red flag -- money collected without the child's info. Follow up:"
    )
    for r in empty_paid:
        print(
            f"    {r['created']:<16} {r['customer_email'] or '(no email)':<32} "
            f"{r['session_id']}"
        )


if __name__ == "__main__":
    main()
