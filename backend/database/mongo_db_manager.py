from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['cryptographyScanner']
results_collection = db['results']


def add_results(_id, results):
    data = {
        "_id": str(_id),
        "results": results
    }
    results_collection.insert_one(data)


def get_results(_id):
    return results_collection.find_one({"_id": _id})
