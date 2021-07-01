"""
Testing cli help messages.
"""

from cli import main


class TestHelpMessages:
    """
    Class tests all cli help messages
    """

    def _run_test_messages(self):
        for message in self.messages:
            assert message in self.result.output

    def test_main(self, app):
        """
        Testing main help messages.
        """
        self.result = app.invoke(main, ["--help"])

        self.messages = [
            "Usage: blenderenv",
            "Show the version and exit.",
            "Blender version and env manager.",
            "Set or show the global Blender version.",
            "Set or show the local specific Blender version.",
            "Install a Blender version.",
            "Uninstall a specific Blender version.",
            "Show the current Blender version and its origin.",
            "List all Python versions available to blenderenv.",
        ]
        self._run_test_messages()

    def test_local(self, app):
        """
        Testing `local` command messages.
        """
        self.result = app.invoke(main, ["local", "--help"])

        self.messages = [
            "Usage: blenderenv local [OPTIONS] [VERSION]...",
            "Sets the local application-specific Blender version by writing the version",
            'name to a file named ".blender-version".',
            # 'When you run a blender command, blenderenv will look for a ".blender-',
            # "file in the current directory and each parent directory. If no such",
            # "file is found in the tree, pyenv will use the global Blender version",
            # 'specified with "blenderenv global". A version specified with the',
            # '"BLENDERENV_VERSION" environment variable takes precedence over local and',
            # "global versions.",
            "<version> can be specified multiple times and should be a version tag known ",
            'The special version string "system" will use your default',
            'Run "blendenv versions" for a list of available Blender',
            "versions.",
            "--unset",
        ]
        self._run_test_messages()

    def test_global(self, app):
        """
        Testing `global` command messages.
        """
        self.result = app.invoke(main, ["global", "--help"])

        self.messages = [
            "Usage: blenderenv global [OPTIONS] VERSION",
            "Sets the global Blender version. You can override the global version at any",
            'time by setting a directory-specific version with "blenderenv local" or by',
            'setting the "BLENDER_VERSION" environment variable.',
            "--unset",
        ]
        self._run_test_messages()

    def test_install(self, app):
        """
        Testing `install` command messages.
        """
        self.result = app.invoke(main, ["install", "--help"])

        self.messages = [
            "Usage: blenderenv install [OPTIONS]",
            "Install a Blender version.",
            "-f",
            "--force",
            "Install even if the version appears to be installed already.",
            "-c",
            "--clear",
            "Removes downloaded installers from the cache to free space.",
            "-l",
            "--list",
            "List all available versions.",
        ]
        self._run_test_messages()

    def test_uninstall(self, app):
        """
        Testing `uninstall` command messages.
        """
        self.result = app.invoke(main, ["uninstall", "--help"])

        self.messages = [
            "Usage: blenderenv uninstall [OPTIONS] [VERSION]...",
            "Uninstall a specific Blender version.",
            "-f",
            "--force",
            "Attempt to remove the specified version without prompting for",
            "confirmation. If the version does not exist, do not display an",
            "error message.",
            "-a",
            "--all",
            "*Caution* Attempt to remove all installed versions.",
        ]
        self._run_test_messages()

    def test_version(self, app):
        """
        Testing `version` command messages.
        """
        self.result = app.invoke(main, ["version", "--help"])

        self.messages = [
            "Usage: blenderenv version [OPTIONS]",
            "Show the current Blender version and its origin.",
        ]
        self._run_test_messages()

    def test_versions(self, app):
        """
        Testing `versions` command messages.
        """
        self.result = app.invoke(main, ["versions", "--help"])

        self.messages = [
            "Usage: blenderenv versions [OPTIONS]",
            "List all Python versions available to blenderenv.",
        ]
        self._run_test_messages()
