"""
Helpers submodule
"""

from typing import List

from click.core import Command, Group


def register_commands(group: Group, commands: List[Command]) -> None:
    """
    Function helps to registered commands in group.
    """
    for command in commands:
        group.add_command(command)
