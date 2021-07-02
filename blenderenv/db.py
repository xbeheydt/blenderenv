"""
Modules helps to handle database
"""

import sqlite3
from sqlite3 import Connection
from types import TracebackType
from typing import Optional, Type

from blenderenv.globals import DB_FILE, DB_SCHEMA_FILE


class Database:
    """
    Class model as Database.
    """

    def __init__(self) -> None:
        self.__con = self.__get_db()

    def init(self) -> None:
        with open(DB_SCHEMA_FILE) as schema:
            self.__con.executescript(schema.read())

    def __enter__(self):
        return self

    def __exit__(
        self,
        ext_type: Optional[Type[BaseException]],
        exc_value: Optional[BaseException],
        traceback: Optional[TracebackType],
    ) -> None:
        # FIXME : test it
        if isinstance(exc_value, Exception):
            self.__con.rollback()
        else:
            self.__con.commit()
        self.__con.close()

    def __get_db(self) -> Connection:
        db = sqlite3.connect(DB_FILE, detect_types=sqlite3.PARSE_DECLTYPES)
        db.row_factory = sqlite3.Row
        return db
