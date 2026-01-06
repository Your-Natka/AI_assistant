CONTACTS = []

def add_contact(name: str, phone: str) -> str:
    CONTACTS.append({"name": name, "phone": phone})
    return f"Contact {name} added."

def show_contacts() -> str:
    if not CONTACTS:
        return "No contacts."

    return "\n".join(
        f"{c['name']}: {c['phone']}" for c in CONTACTS
    )