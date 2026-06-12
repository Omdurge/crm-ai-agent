CREATE TABLE contacts (
    id INTEGER PRIMARY KEY,
    email VARCHAR UNIQUE,
    name VARCHAR,
    company VARCHAR
);

CREATE TABLE threads (
    id INTEGER PRIMARY KEY,
    thread_id VARCHAR UNIQUE,
    subject VARCHAR,
    sender_email VARCHAR
);

CREATE TABLE emails (
    id INTEGER PRIMARY KEY,
    message_id VARCHAR UNIQUE,
    sender VARCHAR,
    subject VARCHAR,
    body TEXT,
    thread_id VARCHAR,
    timestamp VARCHAR
);