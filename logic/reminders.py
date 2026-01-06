from datetime import datetime, timedelta
from core.dates import parse_natural_date

REMINDERS = []


def add_reminder(text: str, date_str: str | None = None) -> str:
    if not date_str:
        date_str = parse_natural_date(text)

    if not date_str:
        return "I couldn't understand the date."

    remind_date = datetime.strptime(date_str, "%Y-%m-%d").date()

    REMINDERS.append({
        "text": text,
        "date": remind_date
    })

    return f"Reminder added for {remind_date}: {text}"


def show_reminders() -> str:
    if not REMINDERS:
        return "No reminders."

    return "\n".join(
        f"{r['date']} — {r['text']}" for r in REMINDERS
    )


def upcoming_reminders(days: int = 7) -> str:
    today = datetime.today().date()
    limit = today + timedelta(days=days)

    upcoming = [
        r for r in REMINDERS
        if today <= r["date"] <= limit
    ]

    if not upcoming:
        return f"No reminders in next {days} days."

    return "\n".join(
        f"{r['date']} — {r['text']}" for r in upcoming
    )
