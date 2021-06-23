"""
Testing cli help messages.
"""

from cli import main


class TestHelpMessages:
    """
    Class tester all help messages
    """

    def _run_test_messages(self):
        for message in self.messages:
            assert message in self.result.output

    def test_main(self, cli):
        """
        Testing main help messages.
        """
        self.result = cli.invoke(main, ["--help"])

        self.messages = [
            "Usage: blenderenv",
            "Print version",
            "Blender version and env manager.",
            "Set or show the global Blender version.",
            "Set or show the local specific Blender version.",
            "Install a Blender version.",
            "Uninstall a specific Blender version.",
            "Show the current Blender version and its origin.",
            "List all Python versions available to blenderenv.",
        ]
        self._run_test_messages()

    def test_local(self, cli):
        """
        Testing `local` command messages.
        """
        self.result = cli.invoke(main, ["local", "--help"])

        self.messages = [
            "Usage: blenderenv local [OPTIONS] [VERSION]...",
            "<version> can be specified multiple times and should be a version",
            "--unset",
        ]
        self._run_test_messages()
