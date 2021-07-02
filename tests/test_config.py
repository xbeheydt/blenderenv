"""
Test file `blenderenv/config.py`
"""

from os import remove

import pytest
from pytest_mock import MockerFixture

from tests.conftest import AppSetup


# region Methods test


def test_config_default_values(app: AppSetup):
    """
    Testing default values from app config.
    """
    assert app.config["main"]["type"] == "prebuilt"
    assert app.config["main"]["system-version"] == ""
    with open(app.blenderenv_home / "config.cfg") as conf_file:
        assert ["[main]", "type = prebuilt", "system-version = ", ""] == [
            line.replace("\n", "")
            for line in conf_file.readlines()
            if line != ""
        ]


def test_config_detect_platform(mocker: MockerFixture):
    """
    Testing detect all platform.
    """
    from blenderenv.config import Config

    mocker.patch("blenderenv.config.sys_platform", new="linux")
    conf = Config()
    assert conf.platform == "linux"
    assert conf["platform"] == "linux"

    mocker.patch("blenderenv.config.sys_platform", new="darwin")
    conf = Config()
    assert conf.platform == "macOS"
    assert conf["platform"] == "macOS"

    mocker.patch("blenderenv.config.sys_platform", new="win32")
    conf = Config()
    assert conf.platform == "windows"
    assert conf["platform"] == "windows"


def test_config_read(app: AppSetup):
    """
    Testing read config from file.
    """
    from blenderenv.config import Config

    app.config["main"]["type"] = "all"
    app.config["main"]["system-version"] = "2.90"
    app.config.save()

    conf = Config()
    conf.read_config()

    assert conf["main"]["type"] == "all"
    assert conf["main"]["system-version"] == "2.90"


# endregion

# region Exceptions test
def test_config_not_found(app: AppSetup):
    """
    Testing ConfigNotFoundError exception.
    """
    from blenderenv.config import ConfigNotFoundError

    remove(app.blenderenv_home / "config.cfg")
    with pytest.raises(ConfigNotFoundError):
        app.config.read_config()


def test_config_platform_not_implemented(mocker: MockerFixture):
    """
    Testing PlatformNotImplementedError exception
    """
    mocker.patch("blenderenv.config.sys_platform", new="foo")

    from blenderenv.config import Config, PlatformNotImplementedError

    with pytest.raises(PlatformNotImplementedError):
        Config()


def test_config_architecture_32bit(mocker: MockerFixture):
    """
    Testing Architecture32BitError exception
    """

    mocker.patch(
        "blenderenv.config.architecture", return_value=["32bit", "foo"]
    )

    from blenderenv.config import Architecture32BitError, Config

    with pytest.raises(Architecture32BitError):
        Config()


# endregion
