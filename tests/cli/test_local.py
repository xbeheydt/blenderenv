"""
Testing `local` command.
"""

from cli import main


def test_exception(cli):
    """
    Testing exception when use --unset and version in same time.
    """
    result = cli.invoke(main, ["local", "--unset", "2.93"])
    assert result.exit_code == 2
    assert "--unset and version not used in same time." in result.output
