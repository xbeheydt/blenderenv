"""
Testing `main` command.
"""

from blenderenv import __name__ as prog_name, __version__ as prog_version
from cli import main


def test_main_version(app):
    """
    Testing `main --version`.
    """
    result = app.invoke(main, ["--version"])
    assert f"{prog_name} v{prog_version}\n" == result.output
