from fastapi import APIRouter, UploadFile
from app.services.embedding_service import embedding_service
from app.services.vector_db import add_document
from app.services.document_processor import chunk_text

router = APIRouter()

@router.post("/upload")
async def upload_file(file: UploadFile):
    content = await file.read()
    text = content.decode()

    chunks = chunk_text(text)

    for chunk in chunks:
        embedding = embedding_service.embed_text(chunk["text"])

        add_document(
            chunk["id"],
            embedding,
            {"text": chunk["text"]}
        )

    return {"status": "uploaded", "chunks": len(chunks)}