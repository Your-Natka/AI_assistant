from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

SYSTEM_PROMPT = """
You are an assistant that extracts user intent and returns ONLY valid JSON.

Possible intents:
- add_contact(name, phone)
- show_contacts
- add_note(text)
- show_notes
- add_reminder(text, date)
- show_reminders
- upcoming_reminders(days)

Rules:
- Return ONLY JSON
- If the user mentions time like "tomorrow", "next week", "in 3 days",
  DO NOT convert it to a date. Pass the original text.
- Use this format:

{
  "intent": "...",
  "data": {...}
}
"""

def analyze(text: str) -> dict:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": text}
        ]
    )

    return json.loads(response.choices[0].message.content)

def ask_ai(user_text):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are an assistant that extracts intent"},
            {"role": "user", "content": user_text}
        ]
    )
    return response.choices[0].message.content