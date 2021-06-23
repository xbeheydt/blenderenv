"""
Testing `main` command.
"""

from blenderenv import __name__, __version__
from cli import main


def test_main_version(cli):
    """
    Testing `main --version`.
    """
    result = cli.invoke(main, ["--version"])
    assert f"{__name__} v{__version__}\n" == result.output
