from fastapi import FastAPI

app = FastAPI(title="DocuMind AI")

@app.get("/")
def root():
    return {"message": "DocuMind AI backend running"}