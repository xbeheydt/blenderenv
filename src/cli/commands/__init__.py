"""
Sub module commands
"""

from cli.commands._global import _global
from cli.commands._install import _install
from cli.commands._local import _local
from cli.commands._uninstall import _uninstall
from cli.commands._version import _version
from cli.commands._versions import _versions


__all__ = [
    "_global",
    "_install",
    "_local",
    "_uninstall",
    "_version",
    "_versions",
]
