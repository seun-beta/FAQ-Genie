from fastapi import FastAPI
from app.rag_service import get_answer

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Supernova RAG API"}

@app.get("/rag/")
def rag(query: str):
    answer = get_answer(query)
    return {"query": query, "answer": answer}
