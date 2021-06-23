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
@click.option("--version", help="Print version", is_flag=True)
def main(version: bool) -> None:
    """
    Blender version and env manager.
    """
    if version:
        click.echo(f"{__name__} v{__version__}")
        exit(0)


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
        try:
            raise UsageError("--unset and version not used in same time.")
        except UsageError:
            sys_exit(1)
    sys_exit(0)


@click.command(
    name="global", short_help="Set or show the global Blender version."
)
@click.argument("version")
# TODO help unset
@click.option("--unset", is_flag=True)
def _global(unset: bool, version: str) -> None:
    """
    Sets the global Blenderenv version. You can override the global version at
    any time by setting a directory-specific version with "blenderenv local"
    or by setting the `BLENDER_VERSION' environment variable.
    """
    if unset and version:
        try:
            raise UsageError("--unset and version not used in same time.")
        except UsageError:
            sys_exit(1)
    sys_exit(0)


@click.command(name="install")
def _install():
    """
    Install a Blender version.
    """
    pass


@click.command(name="uninstall")
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
