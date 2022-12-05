from abc import ABC

from backend.database.dal import DAL
import pymysql as mysql
from backend.database.sql_queries import *
from typing import List
from backend.database.constants.configuration import *


class DbManager(DAL, ABC):
    def __init__(self, user: str = DEFAULT_USER, pwd: str = DEFAULT_PWD, db: str = DEFAULT_DB,
                 host: str = DEFAULT_HOST):
        self.connection = mysql.connect(
            host=host, user=user, password=pwd, db=db, charset="utf8", cursorclass=mysql.cursors.DictCursor,
            autocommit=True)

    def get_data_by_organization(self, organization_name: str) -> List[object]:
        pass

    def get_data_by_repository(self, repository_name: str) -> List[object]:
        pass

    def get_data_by_file(self, file_name: str) -> List[object]:
        pass

    def add_library(self, library_name: str, language_id: int, category: int) -> None:
        pass

    def add_word(self, word: str) -> None:
        pass

    def add_language(self, language_name: str) -> None:
        pass


CONNECTOR = None


def get_db_connector():
    global CONNECTOR
    if CONNECTOR is None:
        try:
            CONNECTOR = DalSQL()
        except Exception as e:
            print(e)
    return CONNECTOR
