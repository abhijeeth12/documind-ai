from fastapi import FastAPI
from app.services.vector_db import init_collection

app = FastAPI(title="DocuMind AI")

@app.on_event("startup")
def startup_event():
    init_collection()

@app.get("/")
def root():
    return {"message": "DocuMind AI backend running"}