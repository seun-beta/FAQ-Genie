from rag.rag_system import retrieve_answer
from utils.logger import setup_logger

logger = setup_logger(__name__)

if __name__ == "__main__":
    query = "What is the mission of Supernova Limited?"
    answers = retrieve_answer(query)
    logger.info(f"Top answers for '{query}':\n")
    for i, answer in enumerate(answers, start=1):
        print(f"{i}. {answer}")
