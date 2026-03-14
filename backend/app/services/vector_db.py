from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams

client = QdrantClient(":memory:")

COLLECTION_NAME = "documents"


def init_collection():
    collections = client.get_collections().collections
    names = [c.name for c in collections]

    if COLLECTION_NAME not in names:
        client.create_collection(
            collection_name=COLLECTION_NAME,
            vectors_config=VectorParams(
                size=384,
                distance=Distance.COSINE
            ),
        )


def add_document(doc_id, embedding, payload):
    client.upsert(
        collection_name=COLLECTION_NAME,
        points=[
            {
                "id": doc_id,
                "vector": embedding,
                "payload": payload,
            }
        ],
    )


def search(query_vector):
    results = client.search(
        collection_name=COLLECTION_NAME,
        query_vector=query_vector,
        limit=5
    )
    return results