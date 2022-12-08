class DALMongoDB:

    def __init__(self, libraries_data: object):
        self.libraries_data = libraries_data

    def get_libraries_names(self, language: str):
        return self.libraries_data[language].keys()

    def get_functions_words_from_libraries(self, language: str, library: str):
        return list(map(lambda l: l["word"], self.libraries_data[language][library]["words"]))

    def get_function_details(self, language: str, library: str, function_name: str):
        return list(filter(lambda l: l["word"] == function_name, self.libraries_data[language][library]["words"]))[0]


CONNECTOR = None


def get_db_connector(libraries_data: object):
    global CONNECTOR
    if CONNECTOR is None:
        try:
            CONNECTOR = DALMongoDB(libraries_data)
        except Exception as e:
            print(e)
    return CONNECTOR
