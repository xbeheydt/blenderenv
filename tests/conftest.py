"""
Configuration for pytest
"""

import pytest
from click.testing import CliRunner


class CustomCliRunner(CliRunner):
    """
    Custom cli runner which prepare project folder test.
    """

    def __init__(self, monkeypatch, tmp_path):
        monkeypatch.setenv("HOME", str(tmp_path), prepend=False)

        self.tmp_path = tmp_path

        self.root_dir = self.tmp_path / ".blenderenv"
        self.root_dir.mkdir()

        self.shims = self.root_dir / "shims"
        self.shims.mkdir()

        self.bins = self.root_dir / "bin"
        self.bins.mkdir()

        self.versions = self.root_dir / "versions"
        self.versions.mkdir()

        self.version = self.root_dir / "version"
        self.version.write_text("")

        super().__init__()


@pytest.fixture
def app(monkeypatch, tmp_path):
    """
    App object helps to run tests.
    """
    yield CustomCliRunner(monkeypatch, tmp_path)
