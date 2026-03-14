from fastapi import APIRouter
from app.services.rag_service import retrieve_context

router = APIRouter()

@router.post("/chat")
def chat(query: str):

    context = retrieve_context(query)

    return {
        "query": query,
        "context": context
    }