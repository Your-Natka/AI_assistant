from datetime import datetime, timedelta
import re

def parse_natural_date(text: str) -> str | None:
    text = text.lower()
    today = datetime.today().date()

    if "today" in text:
        return today.isoformat()

    if "tomorrow" in text:
        return (today + timedelta(days=1)).isoformat()

    if "next week" in text:
        return (today + timedelta(days=7)).isoformat()

    match = re.search(r"in (\d+) days", text)
    if match:
        days = int(match.group(1))
        return (today + timedelta(days=days)).isoformat()

    return None
