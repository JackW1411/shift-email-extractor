# shift-email-extractor

Turns pharmacy shift-request emails into structured records using Claude.

An email like *"any chance you can cover this Saturday, 9 til 1? Pharmacist please. We can do $70 an hour."* becomes:

```
pharmacy:   Oakridge Pharmacy
shift_date: 2026-11-21
start_time: 09:00
end_time:   13:00
role:       pharmacist
rate:       70.0
```

## How it works

- `schema.py` defines `ShiftRequest`, a Pydantic model with the fields above. `pharmacy` and `shift_date` are required; the rest can be `None` when the email doesn't say (for example, no rate given).
- `emails.py` holds three synthetic test emails (no real data), each with a hand-labelled `expected` answer.
- `extract.py` sends each email, together with the date it was sent, to Claude using `client.messages.parse()` with `ShiftRequest` as the output format. The sent date is included so relative dates like "this Saturday" can be resolved.

## Setup

Requires Python 3.10 or later.

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install anthropic pydantic python-dotenv
```

Create a file named `.env` in the project folder containing your Anthropic API key:

```
ANTHROPIC_API_KEY=your-key-here
```

`.env` is listed in `.gitignore` and must never be committed.

## Running

From the terminal, with the virtual environment active:

```bash
python extract.py
```

For each email it prints the `stop_reason` and the extracted `ShiftRequest`. This makes one API call per email.

## Current status

Scored by exact match against the hand-labelled answers (3 emails × 6 fields), the extractor gets **15/18**. Every field is correct except `role`, which misses on all three emails because of wording rather than misreading: the model returns things like `Locum pharmacist`, `Pharmacist` and `Dispensary Technician` where the labels say `pharmacist` and `dispensary tech`. Its wording also changes between runs.

## Known gaps and next steps

- **Role values:** restrict `role` to a fixed set (e.g. `Literal["pharmacist", "dispensary tech"]`) so the output is consistent and can be compared exactly.
- **Scoring:** add field-by-field comparison against `expected` to `extract.py`.
- **Error handling:** handle `refusal` and `max_tokens` stop reasons, and add sanity checks such as `end_time` being after `start_time`.
- **Ambiguous dates:** numeric dates like `3/4/26` can be misread (3 April vs 4 March) and still pass validation. Stating the date format in the prompt and adding a labelled test email for this case would guard against it.
