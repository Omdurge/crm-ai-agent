def decide_action(classification):

    category = classification["category"]
    urgency = classification["urgency"]
    requires_human = classification["requires_human"]

    if category == "Security":
        return {
            "action": "ESCALATE_SECURITY_TEAM"
        }

    if category == "Legal":
        return {
            "action": "ESCALATE_LEGAL_TEAM"
        }

    if urgency == "Critical":
        return {
            "action": "ESCALATE_HUMAN_AGENT"
        }

    if requires_human:
        return {
            "action": "ESCALATE_HUMAN_AGENT"
        }

    return {
        "action": "AUTO_REPLY"
    }