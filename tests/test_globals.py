"""
Test file `blenderenv/globals.py
"""

from tests.conftest import AppSetup


def test_globals_var(app: AppSetup):
    """
    Testing all globals var values.
    """
    from blenderenv.globals import (
        BIN_FOLDER,
        BLENDERENV_HOME,
        CACHE_FOLDER,
        CONFIG_FILE,
        LIB_FOLDER,
        RELEASE_TYPE_DEFAULT,
        RELEASES_DB_FILE,
        RELEASES_TYPES,
        SHIMS_FOLDER,
        VENDOR_FOLDER,
        VERSIONS_FOLDER,
    )

    assert BLENDERENV_HOME == app.blenderenv_home
    assert CONFIG_FILE == app.blenderenv_home / "config.cfg"
    assert BIN_FOLDER == app.bin
    assert SHIMS_FOLDER == app.shims
    assert CACHE_FOLDER == app.cache
    assert VERSIONS_FOLDER == app.versions
    assert LIB_FOLDER == app.lib
    assert VENDOR_FOLDER == app.vendor
    assert RELEASES_DB_FILE == app.blenderenv_home / "database"
    assert RELEASE_TYPE_DEFAULT == "prebuilt"
    assert RELEASES_TYPES == ["all", "prebuilt", "source"]
