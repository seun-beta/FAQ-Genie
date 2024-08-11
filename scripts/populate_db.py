import json
from rag.rag_system import add_entry
from db.mongo_db import create_vector_index
from utils.logger import setup_logger
from utils.error_handling import handle_error

logger = setup_logger(__name__)

def populate_db_from_json(json_file):
    try:
        with open(json_file, 'r') as file:
            data = json.load(file)
            for entry in data:
                add_entry(entry["question"], entry["answer"])
        logger.info("Database populated successfully")
    except FileNotFoundError as e:
        handle_error(e)
    except json.JSONDecodeError as e:
        handle_error(e)

if __name__ == "__main__":
    create_vector_index()
    populate_db_from_json('data/handbook.json')
