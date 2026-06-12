def classify_email(email_text: str):

    text = email_text.lower()

    category = "General"
    urgency = "Low"
    sentiment = "Neutral"
    requires_human = False

    # Security

    SECURITY_KEYWORDS = [
    "ransomware",
    "breach",
    "bitcoin",
    "btc",
    "crypto",
    "hack",
    "hacked",
    "security incident",
    "compromised",
    "malware",
    "attack",
    "data leak",
    "login attempt",
    "unknown location",
    "admin account",
    "credentials",
    "unauthorized",
    "suspicious login",
    "north korea",
    "ip address"
]

    if any(keyword in text for keyword in SECURITY_KEYWORDS):
        category = "Security"
        urgency = "Critical"
        requires_human = True

    # Billing

    elif any(word in text for word in [
        "refund",
        "invoice",
        "payment",
        "subscription"
    ]):
        category = "Billing"

    # Technical

    elif any(word in text for word in [
        "error",
        "500",
        "bug",
        "crash",
        "not working"
    ]):
        category = "Technical"

    # Legal

    elif any(word in text for word in [
        "cease and desist",
        "lawsuit",
        "legal"
    ]):
        category = "Legal"
        requires_human = True

    # Urgency

    if any(word in text for word in [
        "urgent",
        "asap",
        "immediately"
    ]):
        urgency = "High"

    # Sentiment

    if any(word in text for word in [
        "unhappy",
        "angry",
        "terrible",
        "cancel",
        "frustrated"
    ]):
        sentiment = "Negative"

    return {
        "category": category,
        "urgency": urgency,
        "sentiment": sentiment,
        "requires_human": requires_human
    }