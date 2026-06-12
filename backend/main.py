from fastapi import FastAPI

from backend.database import Base, engine

from backend.models.email import Email
from backend.models.thread import Thread
from backend.models.contact import Contact

from backend.routes.emails import router as email_router
from backend.routes.threads import router as thread_router
from backend.routes.classifier import router as classifier_router
from backend.routes.thread_classifier import router as thread_classifier_router

from backend.routes.agent import router as agent_router

from backend.routes.kb import router as kb_router
from backend.routes.rag import router as rag_router

from backend.routes.reply import router as reply_router
from backend.routes.agent_reply import router as agent_reply_router

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

app.include_router(email_router)
app.include_router(thread_router)

app.include_router(classifier_router)

app.include_router(thread_classifier_router)

app.include_router(agent_router)

app.include_router(kb_router)

app.include_router(rag_router)

app.include_router(reply_router)

app.include_router(agent_reply_router)

@app.get("/")
def home():
  return {
    "message": "CRM AI Agent Running"
  }
