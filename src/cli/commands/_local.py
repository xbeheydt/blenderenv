"""
cli `local` command
"""

from typing import List

import click
from click.exceptions import UsageError


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
