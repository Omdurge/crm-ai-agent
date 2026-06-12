from fastapi import APIRouter

from backend.database import SessionLocal
from backend.models.email import Email

from backend.services.thread_classifier import classify_thread

router = APIRouter()


@router.get("/classify-thread/{thread_id}")
def classify_thread_endpoint(thread_id: str):

    db = SessionLocal()

    emails = (
        db.query(Email)
        .filter(Email.thread_id == thread_id)
        .all()
    )

    if not emails:
        return {"error": "Thread not found"}

    result = classify_thread(emails)

    return {
        "thread_id": thread_id,
        **result
    }