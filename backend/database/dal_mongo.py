from pymongo import MongoClient
from database.data.libraries_data import libraries_data


class DALMongoDB:

    def __init__(self):
        client = MongoClient('mongodb://localhost:27017/')
        db = client['cryptographyScanner']
        self.results_collection = db['results']
        self.libraries_data_collection = db['libraries_data']
        self.libraries_data_collection.insert_one(libraries_data)
        self.libraries_data = libraries_data

    def add_results(self, _id, results):
        data = {
            "_id": str(_id),
            "results": results
        }
        self.results_collection.insert_one(data)

    def get_results(self, _id):
        return self.results_collection.find_one({"_id": _id})

    def get_libraries_names(self, language: str):
        return self.libraries_data[language].keys()

    def get_functions_words_from_libraries(self, language: str, library: str):
        return list(map(lambda l: l["word"], self.libraries_data[language][library]["words"]))

    def get_function_details(self, language: str, library: str, function_name: str):
        return list(filter(lambda l: l["word"] == function_name, self.libraries_data[language][library]["words"]))[0]


CONNECTOR = None


def get_db_connector():
    global CONNECTOR
    if CONNECTOR is None:
        try:
            CONNECTOR = DALMongoDB()
        except Exception as e:
            print(e)
    return CONNECTOR
