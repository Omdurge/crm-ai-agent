from fastapi import APIRouter

from backend.services.reply_generator import generate_reply

router = APIRouter()


@router.get("/reply")
def reply(query: str):

    return {
        "reply": generate_reply(query)
    }