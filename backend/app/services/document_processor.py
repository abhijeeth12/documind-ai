import uuid


def chunk_text(text: str, chunk_size: int = 500):
    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(
            {
                "id": str(uuid.uuid4()),
                "text": chunk
            }
        )
        start = end

    return chunks