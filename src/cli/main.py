"""
Cli main entrypoint
"""

from sys import exit as sys_exit

import click

from blenderenv import __name__, __version__
from cli.commands import (
    _global,
    _install,
    _local,
    _uninstall,
    _version,
    _versions,
)
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


# Main group register
_register_commands(
    main, [_local, _global, _install, _uninstall, _version, _versions]
)

if __name__ == "__main__":
    sys_exit(main())
