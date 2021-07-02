"""
Test file `blenderenv/db.py`
"""

from tests.conftest import AppSetup


def test_init_database(app: AppSetup):
    """
    Testing database initialization
    """
    from blenderenv.db import Database

    with Database() as db:
        db.init()

    db_file = app.blenderenv_home / "database"
    assert db_file.exists()
