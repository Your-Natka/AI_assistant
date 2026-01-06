NOTES = []

def add_note(text: str) -> str:
    NOTES.append(text)
    return "Note added."

def show_notes() -> str:
    return "\n".join(NOTES) or "No notes."