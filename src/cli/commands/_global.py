"""
cli `global` command
"""

import click
from click.exceptions import UsageError


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
        raise UsageError("--unset and version not used in same time.")
