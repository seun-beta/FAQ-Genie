import os
from dotenv import load_dotenv

load_dotenv()

MONGODB_URI = os.getenv("MONGODB_URI", "mongodb://localhost:27017/")
DB_NAME = os.getenv("DB_NAME", "supernova_rag")
COLLECTION_NAME = os.getenv("COLLECTION_NAME", "employee_handbook")

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "your-openai-api-key")
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
