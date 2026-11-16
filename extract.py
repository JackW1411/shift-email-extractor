from anthropic import Anthropic
from dotenv import load_dotenv

from emails import EMAILS
from schema import ShiftRequest

load_dotenv()
client = Anthropic()

MODEL = "claude-haiku-5-5"


def extract(email: dict):
    prompt = (
        f"This email was sent on {email['sent_date']}. Use that date to resolve "
        "relative dates like 'this Saturday'.\n\n"
        "Extract the shift request from the email below.\n\n"
        f"{email['text']}"
    )
    return client.messages.parse(
        model=MODEL,
        max_tokens=1024,
        messages=[{"role": "user", "content": prompt}],
        output_format=ShiftRequest,
    )


if __name__ == "__main__":
    for email in EMAILS:
        response = extract(email)
        print(f"--- {email['id']} ---")
        print("stop_reason:", response.stop_reason)
        print(response.parsed_output)
