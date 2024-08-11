from openai import OpenAI
import numpy as np
from config.settings import OPENAI_API_KEY
from utils.logger import setup_logger
from utils.error_handling import handle_error

client = OpenAI()

logger = setup_logger(__name__)

def generate_embedding(text):
    try:
        logger.info(f"Generating embedding for text: {text}")
        response = client.embeddings.create(
            input=[text],
            model="text-embedding-3-small"
        )
        embedding = np.array(response['data'][0]['embedding'])
        logger.info("Embedding generated successfully")
        return embedding
    except Exception as e:
        handle_error(e)
        