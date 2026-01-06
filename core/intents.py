def validate_intent(ai_response: dict) -> dict:
    if "intent" not in ai_response:
        raise ValueError("No intent detected")

    return ai_response