import pymongo
from config import MONGO_URI, DB_NAME, COLLECTION_NAME

def load_to_mongodb(data):
    client = pymongo.MongoClient(MONGO_URI)
    db = client[DB_NAME]
    collection = db[COLLECTION_NAME]
    for doc in data:
        collection.update_one({"id": doc["id"]}, {"$set": doc}, upsert=True)
    client.close()