import pytest
from embeddings.openai_embedder import generate_embedding

def test_generate_embedding():
    text = "Test text for embedding"
    embedding = generate_embedding(text)
    assert len(embedding) > 0
