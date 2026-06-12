import json

from backend.database import SessionLocal
from backend.models.email import Email

db = SessionLocal()

with open("email-data-advanced.json", "r", encoding="utf-8") as f:
    emails = json.load(f)

count = 0

for item in emails:

    existing = (
        db.query(Email)
        .filter(Email.message_id == item["message_id"])
        .first()
    )

    if existing:
        continue

    email = Email(
        message_id=item["message_id"],
        sender=item["sender"],
        subject=item["subject"],
        body=item["body"],
        timestamp=item["timestamp"],
        thread_id=item["thread_id"]
    )

    db.add(email)
    count += 1

db.commit()

print(f"Imported {count} emails")