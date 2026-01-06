from logic.contacts import add_contact, show_contacts
from logic.notes import add_note, show_notes
from logic.reminders import add_reminder, show_reminders, upcoming_reminders

def dispatch(intent_data: dict) -> str:
    intent = intent_data.get("intent")
    data = intent_data.get("data", {})

    if intent == "add_contact":
        return add_contact(**data)

    elif intent == "show_contacts":
        return show_contacts()

    elif intent == "add_note":
        return add_note(data.get("text", ""))

    elif intent == "show_notes":
        return show_notes()

    elif intent == "add_reminder":
        return add_reminder(
            data.get("text", ""),
            data.get("date", "")
        )

    elif intent == "show_reminders":
        return show_reminders()

    elif intent == "upcoming_reminders":
        return upcoming_reminders(data.get("days", 7))

    else:
        return "Unknown intent."
