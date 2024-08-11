import pytest
from rag.rag_system import add_entry, retrieve_answer

def test_add_entry():
    question = "What is a test?"
    answer = "This is a test answer."
    add_entry(question, answer)

def test_retrieve_answer():
    query = "What is a test?"
    answers = retrieve_answer(query)
    assert len(answers) > 0
