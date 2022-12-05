from configuration.libraries import libraries_data
from backend.database.db_manger import DbManager

dbManager = DbManager()

for language, libraries in list(libraries_data.items()):
    dbManager.add_language(language)
    libs = list(libraries.items())
    language_id=1
    category_id=1
    for library in libs:
        dbManager.add_library(library, language_id, category_id)





