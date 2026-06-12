from fastapi import APIRouter

from backend.database import SessionLocal
from backend.models.email import Email

from backend.services.thread_classifier import classify_thread
from backend.services.agent import decide_action
from backend.services.reply_generator import generate_reply

router = APIRouter()


@router.get("/agent-reply/{thread_id}")
def agent_reply(thread_id: str):

    db = SessionLocal()

    try:

        emails = (
            db.query(Email)
            .filter(Email.thread_id == thread_id)
            .all()
        )

        if not emails:
            return {
                "error": "Thread not found"
            }

        classification = classify_thread(emails)

        decision = decide_action(classification)

        latest_email = emails[-1]

        reply = generate_reply(
            latest_email.body
        )

        return {
            "thread_id": thread_id,
            "classification": classification,
            "decision": decision,
            "reply": reply
        }

    finally:
        db.close()