from data.libraries_data import data
from db_manger import DbManager

dbManager = DbManager()

for language in list(data.keys()):
    dbManager.add_language(language)
    libraries = list(data[language].keys())
    language_id=1
    category_id=1
    for library in libraries:
        dbManager.add_library(library, language_id, category_id)





