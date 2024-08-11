from embeddings.openai_embedder import generate_embedding
from db.mongo_db import insert_document, find_similar_questions
from utils.logger import setup_logger
from utils.error_handling import handle_error

logger = setup_logger(__name__)

def add_entry(question, answer):
    try:
        logger.info(f"Adding entry for question: {question}")
        embedding = generate_embedding(question)
        document = {
            "question": question,
            "answer": answer,
            "embedding": embedding.tolist()
        }
        insert_document(document)
        logger.info("Entry added successfully")
    except Exception as e:
        handle_error(e)

def retrieve_answer(query):
    try:
        logger.info(f"Retrieving answer for query: {query}")
        embedding = generate_embedding(query).tolist()
        similar_docs = find_similar_questions(embedding)
        answers = [doc['answer'] for doc in similar_docs]
        logger.info("Answer retrieval successful")
        return answers
    except Exception as e:
        handle_error(e)
