from pydantic import BaseModel

class DocumentChunk(BaseModel):
    id: str
    text: str
    metadata: dict