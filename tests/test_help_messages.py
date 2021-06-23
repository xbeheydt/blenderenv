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
        Testing main help message.
        """
        self.result = cli.invoke(main, ["--help"])

        assert 0 == self.result.exit_code
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
