"""
Configuration for pytest
"""

import os

import pytest
from click.testing import CliRunner
from pytest import TempPathFactory


# region Class Tools
class AppSetup:
    """
    AppSetup configures app environment in temporary path.
    """

    def __init__(self, tmp_path_factory: TempPathFactory):
        self.tmp_path = tmp_path_factory.mktemp("test")

        self.blenderenv_home = self.tmp_path / ".blenderenv"
        self.blenderenv_home.mkdir()
        os.environ["BLENDERENV_HOME"] = str(self.blenderenv_home)

        self.shims = self.blenderenv_home / "shims"
        self.shims.mkdir()
        self.cache = self.blenderenv_home / "cache"
        self.cache.mkdir()
        self.bin = self.blenderenv_home / "bin"
        self.bin.mkdir()
        self.versions = self.blenderenv_home / "versions"
        self.versions.mkdir()

        self.lib = self.blenderenv_home / "lib"
        self.lib.mkdir()
        self.vendor = self.lib / "_vendor"
        self.vendor.mkdir()

        from blenderenv.config import Config

        self.config = Config()
        self.config.init_default()


class CustomCliRunner(CliRunner):
    """
    Custom cli runner which prepare project folder test.
    """

    def __init__(self, tmp_path):
        super().__init__()


# endregion

# region Fixtures
@pytest.fixture(scope="session", autouse=True)
def app(tmp_path_factory):
    """
    Configure app application for tests.
    """
    yield AppSetup(tmp_path_factory)


@pytest.fixture
def cli():
    """
    App object helps to run tests.
    """
    yield CustomCliRunner()


# endregion
