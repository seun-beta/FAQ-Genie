from pymongo import MongoClient, errors
from pymongo.collection import Collection
from pymongo.database import Database
from config.settings import MONGODB_URI, DB_NAME, COLLECTION_NAME
from utils.logger import setup_logger
from utils.error_handling import handle_error

logger = setup_logger(__name__)

try:
    client = MongoClient(MONGODB_URI)
    db: Database = client[DB_NAME]
    collection: Collection = db[COLLECTION_NAME]
    logger.info(f"Connected to MongoDB at {MONGODB_URI}")
except errors.ConnectionFailure as e:
    handle_error(e)

def insert_document(document):
    try:
        collection.insert_one(document)
        logger.info("Document inserted successfully")
    except errors.PyMongoError as e:
        handle_error(e)

def create_vector_index():
    try:
        collection.create_index([("embedding", "2dsphere")])
        logger.info("2dsphere index created on 'embedding'")
    except errors.PyMongoError as e:
        handle_error(e)

def find_similar_questions(embedding, top_n=3):
    try:
        logger.info("Searching for similar questions")
        return collection.find({
            "embedding": {
                "$near": {
                    "$geometry": {
                        "type": "Point",
                        "coordinates": embedding
                    },
                    "$maxDistance": 1000
                }
            }
        }).limit(top_n)
    except errors.PyMongoError as e:
        handle_error(e)
