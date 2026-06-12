from fastapi import APIRouter

from backend.services.kb_search import search_knowledge_base

router = APIRouter()


@router.get("/kb/search")
def kb_search(query: str):

    results = search_knowledge_base(query)

    return {
        "query": query,
        "matches": results
    }