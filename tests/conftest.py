"""
Configuration for pytest
"""

import pytest
from click.testing import CliRunner


@pytest.fixture
def cli():
    """
    Make a runner for cli entrepoint.
    """
    return CliRunner()
