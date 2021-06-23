"""
cli `version` command
"""

import click


@click.command(name="version")
def _version():
    """
    Show the current Blender version and its origin.
    """
    pass
