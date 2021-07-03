"""
Test file `blenderenv/db.py`
"""

from tests.conftest import AppSetup


def test_init_database(app: AppSetup):
    """
    Testing database initialization
    """
    from blenderenv.db import Database
    from blenderenv.globals import DB_FILE, DB_SCHEMA_FILE

    with Database(DB_FILE) as db:
        db.executescript(DB_SCHEMA_FILE)

    db_file = app.blenderenv_home / "database"
    assert db_file.exists()
