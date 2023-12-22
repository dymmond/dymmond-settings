from dymmond_settings import __version__
from dymmond_settings.base import Settings
from dymmond_settings.conf import settings
from dymmond_settings.enums import EnvironmentType


def test_defaults():
    settings = Settings()

    assert settings.debug is False


def test_test_dict():
    settings = Settings()

    settings_dict = settings.dict()

    assert settings_dict["debug"] is False

    assert settings_dict == {
        "debug": False,
        "environment": EnvironmentType.PRODUCTION,
        "version": __version__,
    }


def test_test_tuple():
    settings = Settings()

    settings_tuple = settings.tuple()

    assert settings_tuple == [
        ("debug", False),
        ("environment", EnvironmentType.PRODUCTION),
        ("version", __version__),
    ]

    assert len(settings_tuple) == 3


def test_conf_settings():
    assert settings.debug is True
    assert settings.environment == EnvironmentType.TESTING
