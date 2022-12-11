from pymongo import MongoClient
from database.data.libraries_data import libraries_data

client = MongoClient('mongodb://localhost:27017/')
db = client['cryptographyScanner']
libraries_data_collection = db['libraries_data']
libraries_data_collection.insert_one({"_id": "libraries",
                                      "data": libraries_data})
