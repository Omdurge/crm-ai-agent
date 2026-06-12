import os

import chromadb
from sentence_transformers import SentenceTransformer


KB_PATH = "knowledge_base"

client = chromadb.PersistentClient(path="backend/vector_db")

collection = client.get_or_create_collection(
    name="crm_knowledge_base"
)

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


def ingest_knowledge_base():

    try:
      existing = collection.get()

      if existing["ids"]:
          collection.delete(
              ids=existing["ids"]
          )
    except Exception:
        pass

    for filename in os.listdir(KB_PATH):

        filepath = os.path.join(
            KB_PATH,
            filename
        )

        if not os.path.isfile(filepath):
            continue

        with open(
            filepath,
            "r",
            encoding="utf-8"
        ) as f:
            content = f.read()

        embedding = model.encode(
            content
        ).tolist()

        collection.add(
            ids=[filename],
            documents=[content],
            embeddings=[embedding]
        )

    return "Knowledge base indexed"


def search_rag(query: str):

    embedding = model.encode(
        query
    ).tolist()

    results = collection.query(
        query_embeddings=[embedding],
        n_results=3
    )

    return results