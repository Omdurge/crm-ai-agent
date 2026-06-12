from fastapi import APIRouter

from backend.services.rag import (
    ingest_knowledge_base,
    search_rag
)

router = APIRouter()


@router.get("/rag/index")
def index_kb():

    return {
        "message": ingest_knowledge_base()
    }


@router.get("/rag/search")
def rag_search(query: str):

    results = search_rag(query)

    return results