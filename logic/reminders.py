from datetime import datetime, timedelta

REMINDERS = []


def add_reminder(text: str, date_str: str) -> str:
    """
    date_str format: YYYY-MM-DD
    """
    try:
        remind_date = datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        return "Invalid date format. Use YYYY-MM-DD."

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
