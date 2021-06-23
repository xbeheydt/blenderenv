"""
cli `uninstall` command
"""

import click


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
