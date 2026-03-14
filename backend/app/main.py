from fastapi import FastAPI
from app.services.vector_db import init_collection
from app.api import upload, chat

app = FastAPI(title="DocuMind AI")

@app.on_event("startup")
def startup():
    init_collection()

app.include_router(upload.router)
app.include_router(chat.router)

@app.get("/")
def root():
    return {"message": "DocuMind AI backend running"}