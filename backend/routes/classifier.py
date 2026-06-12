from fastapi import APIRouter

from backend.database import SessionLocal
from backend.models.email import Email
from backend.services.classifier import classify_email

router = APIRouter()


@router.get("/classify/{message_id}")
def classify(message_id: str):

    db = SessionLocal()

    email = (
        db.query(Email)
        .filter(Email.message_id == message_id)
        .first()
    )

    if not email:
        return {"error": "Email not found"}

    result = classify_email(email.body)

    return {
        "message_id": email.message_id,
        "subject": email.subject,
        **result
    }