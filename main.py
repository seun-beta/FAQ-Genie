from scripts.populate_db import populate_db_from_json
from scripts.query_rag import retrieve_answer

if __name__ == "__main__":
    # Example usage: populate database and query it
    populate_db_from_json('data/handbook.json')
    query = "What is the mission of Supernova Limited?"
    answers = retrieve_answer(query)
    for i, answer in enumerate(answers, start=1):
        print(f"{i}. {answer}")
