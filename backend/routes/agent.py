# backend/routes/agent.py

from fastapi import APIRouter

from backend.database import SessionLocal
from backend.models.email import Email

from backend.services.thread_classifier import classify_thread
from backend.services.agent import decide_action

router = APIRouter()


@router.get("/agent/{thread_id}")
def run_agent(thread_id: str):

    db = SessionLocal()

    emails = (
        db.query(Email)
        .filter(Email.thread_id == thread_id)
        .all()
    )

    if not emails:
        return {"error": "Thread not found"}

    classification = classify_thread(emails)

    decision = decide_action(classification)

    return {
        "thread_id": thread_id,
        "classification": classification,
        "decision": decision
    }