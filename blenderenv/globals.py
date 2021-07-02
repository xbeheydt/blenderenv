"""
Globals vars module

`blenderenv/globals.py`
"""

from os import environ
from pathlib import Path


BLENDERENV_HOME = Path(environ["BLENDERENV_HOME"])
CONFIG_FILE = BLENDERENV_HOME / "config.cfg"

BIN_FOLDER = BLENDERENV_HOME / "bin"
SHIMS_FOLDER = BLENDERENV_HOME / "shims"
CACHE_FOLDER = BLENDERENV_HOME / "cache"
VERSIONS_FOLDER = BLENDERENV_HOME / "versions"

LIB_FOLDER = BLENDERENV_HOME / "lib"
VENDOR_FOLDER = LIB_FOLDER / "_vendor"

RELEASES_DB_FILE = BLENDERENV_HOME / "database"
RELEASE_TYPE_DEFAULT = "prebuilt"
RELEASES_TYPES = ["all", "prebuilt", "source"]
