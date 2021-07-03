"""
Modules helps to handle database
"""

import sqlite3
from pathlib import Path
from sqlite3 import Connection
from types import TracebackType
from typing import Optional, Type


class Database:
    """
    Class model as Database.
    """

    def __init__(self, path: Path) -> None:
        self.__path = path
        self.__con = self.__get_connexion()

    @property
    def path(self) -> Path:
        return self.__path

    def close(self) -> None:
        self.__con.close()

    def commit(self) -> None:
        self.__con.commit()

    def executescript(self, path: Path) -> None:
        with open(path) as script:
            self.__con.executescript(script.read())

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

    def __get_connexion(self) -> Connection:
        db = sqlite3.connect(self.__path, detect_types=sqlite3.PARSE_DECLTYPES)
        db.row_factory = sqlite3.Row
        return db
