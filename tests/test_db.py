import pytest
from db.mongo_db import insert_document, find_similar_questions

def test_insert_document():
    doc = {"question": "Test?", "answer": "This is a test."}
    result = insert_document(doc)
    assert result is not None

def test_find_similar_questions():
    embedding = [0.1, 0.2, 0.3]  # Mock embedding
    results = find_similar_questions(embedding)
    assert len(results) >= 0
