"""
cli `install` command
"""

import click


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
