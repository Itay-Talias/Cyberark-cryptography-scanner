from abc import ABC
from fastapi import status

from constants import configuration as c
from backend.database.dal import DAL
import pymysql as mysql
from typing import List
from fastapi.responses import JSONResponse

from sql_queries.queries import ADD_LANGUAGE, ADD_LIBRARY


class DbManager(DAL):
    def __init__(self, user: str = c.DEFAULT_USER, pwd: str = c.DEFAULT_PWD, db: str = c.DEFAULT_DB,
                 host: str = c.DEFAULT_HOST):
        self.connection = mysql.connect(
            host=host, user=user, password=pwd, db=db, charset="utf8", cursorclass=mysql.cursors.DictCursor,
            autocommit=True)

    def get_data_by_organization(self, organization_name: str) -> List[object]:
        pass

    def get_data_by_repository(self, repository_name: str) -> List[object]:
        pass

    def get_data_by_file(self, file_name: str) -> List[object]:
        pass

    def add_library(self, library_name: str, language_id: int, category_id: int) -> None:
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(ADD_LIBRARY, library_name, language_id, category_id)
                self.connection.commit()

        except Exception as e:
            return JSONResponse({"Error": e},
                                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def add_word(self, word: str) -> None:
        pass

    def add_language(self, language_name: str) -> None:
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(ADD_LANGUAGE, language_name)
                result = cursor.fetchall()
                print(result)
                self.connection.commit()

        except Exception as e:
            return JSONResponse({"Error": e},
                                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


CONNECTOR = None


def get_db_connector():
    global CONNECTOR
    if CONNECTOR is None:
        try:
            CONNECTOR = DalSQL()
        except Exception as e:
            print(e)
    return CONNECTOR
