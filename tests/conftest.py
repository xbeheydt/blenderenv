"""
Configuration for pytest
"""

import pytest
from click.testing import CliRunner


@pytest.fixture
def cli(monkeypatch, tmp_path):
    """
    Make a runner for cli entrepoint.
    """
    monkeypatch.setenv("HOME", str(tmp_path), prepend=False)
    b_dir = tmp_path / ".blenderenv"
    b_dir.mkdir()
    yield CliRunner()
