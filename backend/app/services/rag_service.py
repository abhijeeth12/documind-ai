from app.services.embedding_service import embedding_service
from app.services.vector_db import search


def retrieve_context(query: str):
    query_embedding = embedding_service.embed_text(query)

    results = search(query_embedding)

    context = []
    for r in results:
        context.append(r.payload["text"])

    return context