from backend.services.classifier import classify_email


def classify_thread(emails):

    full_text = ""

    for email in emails:
        full_text += email.body + "\n"

    result = classify_email(full_text)

    text = full_text.lower()

    # Escalation signals

    if any(word in text for word in [
        "trustpilot",
        "g2",
        "public review",
        "canceling my subscription",
        "cancel subscription",
        "leaving"
    ]):
        result["urgency"] = "Critical"
        result["requires_human"] = True

    return result