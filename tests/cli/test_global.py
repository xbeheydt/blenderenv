"""
Testing `global` command.
"""

from cli import main


def test_exception(app):
    """
    Testing exception when use --unset and version in same time.
    """
    result = app.invoke(main, ["global", "--unset", "2.93"])
    assert result.exit_code == 2
    assert "--unset and version not used in same time." in result.output

    result = app.invoke(main, ["global", "2.90", "2.93"])
    assert result.exit_code == 2
    assert "Error: Got unexpected extra argument" in result.output
