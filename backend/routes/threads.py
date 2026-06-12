from fastapi import APIRouter

from backend.database import SessionLocal
from backend.models.email import Email

router = APIRouter()


@router.get("/threads")
def get_threads():

    db = SessionLocal()

    try:

        emails = db.query(Email).all()

        threads = {}

        for email in emails:

            if email.thread_id not in threads:
                threads[email.thread_id] = {
                    "thread_id": email.thread_id,
                    "subject": email.subject,
                    "sender": email.sender
                }

        return list(threads.values())

    finally:
        db.close()


@router.get("/threads/{thread_id}")
def get_thread(thread_id: str):

    db = SessionLocal()

    try:

        emails = (
            db.query(Email)
            .filter(Email.thread_id == thread_id)
            .all()
        )

        return [
            {
                "message_id": email.message_id,
                "sender": email.sender,
                "subject": email.subject,
                "body": email.body,
                "timestamp": email.timestamp
            }
            for email in emails
        ]

    finally:
        db.close()