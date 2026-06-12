from fastapi import APIRouter

from backend.database import SessionLocal
from backend.models.email import Email

router = APIRouter()


@router.get("/emails")
def get_emails():

    db = SessionLocal()

    emails = db.query(Email).all()

    return [
        {
            "message_id": email.message_id,
            "sender": email.sender,
            "subject": email.subject,
            "thread_id": email.thread_id
        }
        for email in emails
    ]