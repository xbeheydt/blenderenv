"""
Top-level for Cli entrypoint blenderenv.
"""

from sys import exit as sys_exit
from typing import List

import click
from click.exceptions import UsageError

from blenderenv import __name__, __version__
from cli.helpers import _register_commands


@click.group(name=__name__)
@click.version_option(
    version=__version__, prog_name=__name__, message="%(prog)s v%(version)s"
)
def main():
    """
    Blender version and env manager.
    """
    pass


@click.command(
    name="local", short_help="Set or show the local specific Blender version."
)
@click.argument("version", nargs=-1)
# TODO help unset
@click.option("--unset", is_flag=True)
def _local(unset: bool, version: List[str]) -> None:
    """
    Sets the local application-specific Blender version by writing the
    version name to a file named ".blender-version".

    When you run a blender command, blenderenv will look for a
    ".blender-version" file in the current directory and each parent directory.
    If no such file is found in the tree, pyenv will use the global Blender
    version specified with "blenderenv global". A version specified with the
    "BLENDERENV_VERSION" environment variable takes precedence over local
    and global versions.

    <version> can be specified multiple times and should be a version
    tag known to blenderenv. The special version string "system" will use
    your default system Python. Run "blendenv versions" for a list of
    available Blender versions.
    """
    if unset and version:
        raise UsageError("--unset and version not used in same time.")


@click.command(
    name="global", short_help="Set or show the global Blender version."
)
@click.argument("version")
# TODO help unset
@click.option("--unset", is_flag=True)
def _global(unset: bool, version: str) -> None:
    """
    Sets the global Blender version. You can override the global version at
    any time by setting a directory-specific version with "blenderenv local"
    or by setting the "BLENDER_VERSION" environment variable.
    """
    if unset and version:
        try:
            raise UsageError("--unset and version not used in same time.")
        except UsageError:
            sys_exit(1)
    sys_exit(0)


@click.command(name="install")
@click.option(
    "-f",
    "--force",
    is_flag=True,
    help="Install even if the version appears to be installed already.",
)
@click.option(
    "-c",
    "--clear",
    is_flag=True,
    help="Removes downloaded installers from the cache to free space.",
)
@click.option(
    "-l", "--list", is_flag=True, help="List all available versions."
)
def _install():
    """
    Install a Blender version.
    """
    pass


@click.command(name="uninstall")
@click.option(
    "-f",
    "--force",
    is_flag=True,
    help="Attempt to remove the specified version without prompting"
    " for confirmation. If the version does not exist, do not"
    " display an error message.",
)
@click.option(
    "-a",
    "--all",
    is_flag=True,
    help="*Caution* Attempt to remove all installed versions.",
)
@click.argument("version", nargs=-1)
def _uninstall():
    """
    Uninstall a specific Blender version.
    """
    pass


@click.command(name="version")
def _version():
    """
    Show the current Blender version and its origin.
    """
    pass


@click.command(name="versions")
def _versions():
    """
    List all Python versions available to blenderenv.
    """
    pass


# Main group register
_register_commands(
    main, [_local, _global, _install, _uninstall, _version, _versions]
)

if __name__ == "__main__":
    sys_exit(main())
