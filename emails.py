# Synthetic shift-request emails with hand-labelled expected answers.
# No real data. Fill in each "expected" dict yourself before running the extractor.

EMAILS = [
    {
        "id": "clean",
        "sent_date": "2026-11-16",
        "text": """Subject: Locum pharmacist needed, Fri 27 Nov

Hi,

Marlow Street Pharmacy is looking for a locum pharmacist on Friday 27 November 2026, 9:00am to 5:30pm. The rate is $62 per hour.

Please reply to confirm.

Regards,
Dana""",
        "expected": {
            "pharmacy": "Marlow Street Pharmacy",
            "shift_date": "2026-11-27",
            "start_time": "09:00",
            "end_time": "17:30",
            "role": "pharmacist",
            "rate": 62.0,
        },
    },
    {
        "id": "missing_rate",
        "sent_date": "2026-11-16",
        "text": """Subject: bit of a scramble

Hi all, hope the week's going well. We've had a tech call in sick for next Thursday week, so we need a dispensary tech on 3 December, from 8.30 till we close at 6. Happy to talk pay if someone can help out.

Cheers,
Priya
Bayside Community Pharmacy""",
        "expected": {
            "pharmacy": "Bayside Community Pharmacy",
            "shift_date": "2026-12-03",
            "start_time": "08:30",
            "end_time": "18:00",
            "role": "dispensary tech",
            "rate": None,
        },
    },
    {
        "id": "loose_date",
        "sent_date": "2026-11-16",
        "text": """Subject: this weekend?

Hey, any chance you can cover this Saturday, 9 til 1? Pharmacist please. We can do $70 an hour.

Thanks,
Oakridge Pharmacy""",
        "expected": {
            "pharmacy": "Oakridge Pharmacy",
            "shift_date": "2026-11-21",
            "start_time": "09:00",
            "end_time": "13:00",
            "role": "pharmacist",
            "rate": 70.0,
        },
    },
]