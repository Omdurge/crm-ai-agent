from sqlalchemy import Column, Integer, String, Text

from backend.database import Base

class Email(Base):
    __tablename__ = "emails"

    id = Column(Integer, primary_key=True)
    message_id = Column(String, unique=True)
    sender = Column(String)
    subject = Column(String)
    body = Column(Text)
    thread_id = Column(String)
    timestamp = Column(String)