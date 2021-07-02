"""
This module represents application configuration.

`blenderenv/config.py`
"""

from configparser import ConfigParser
from platform import architecture
from sys import platform as sys_platform
from typing import Any

from blenderenv.globals import CONFIG_FILE, RELEASE_TYPE_DEFAULT


class Config(ConfigParser):
    """
    Class gets or handles app configuration.
    """

    def __init__(self) -> None:
        super().__init__()
        self.__detect_platform()

    @property
    def platform(self) -> str:
        """TODO"""
        return self.__platform

    def init_default(self) -> None:
        """TODO"""
        self["main"] = {"type": RELEASE_TYPE_DEFAULT, "system-version": ""}
        self.save()

    def save(self) -> None:
        """TODO"""
        with open(CONFIG_FILE, "w") as config_file:
            super().write(config_file)

    def read_config(self) -> None:
        """TODO"""
        if not CONFIG_FILE.exists():
            raise ConfigNotFoundError
        super().read(CONFIG_FILE)

    def __getitem__(self, section: str) -> Any:
        if section == "platform":
            return self.__platform
        return super().__getitem__(section)

    def __detect_platform(self) -> None:
        """TODO"""
        if sys_platform == "win32":
            self.__platform = "windows"
        elif sys_platform == "linux":
            self.__platform = "linux"
        elif sys_platform == "darwin":
            self.__platform = "macOS"
        else:
            raise PlatformNotImplementedError
        if architecture()[0] == "32bit":
            raise Architecture32BitError


class ConfigNotFoundError(FileNotFoundError):
    """
    Blenderenv configuration not found.
    """


class Architecture32BitError(NotImplementedError):
    """
    32bits architectures are not supported.
    """


class PlatformNotImplementedError(NotImplementedError):
    """
    Platform not supported.
    """
