"""
Top-level for Cli entrypoint blenderenv.
"""

import click

from blenderenv import __name__, __version__
from cli.helpers import _register_commands


@click.group(name=__name__)
@click.option("--version", help="Print version", is_flag=True)
def main(version: bool):
    """
    Blender version and env manager.
    """
    if version:
        click.echo(f"{__name__} v{__version__}")
        exit(1)


@click.command(name="local")
def _local():
    """
    Set or show the local specific Blender version.
    """
    pass


@click.command(name="global")
def _global():
    """
    Set or show the global Blender version.
    """
    pass


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
    exit(main())
