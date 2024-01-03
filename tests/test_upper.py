from dataclasses import dataclass, field
from typing import Union

from dymmond_settings import Settings, __version__
from dymmond_settings.enums import EnvironmentType


@dataclass
class CustomSettings(Settings):
    """
    A custom settings that allows the __repr__
    """

    my_sett: str = field(default="works")
    my_custom: Union[str, None] = None

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}()"


def test_upper_dict_exclude_none():
    settings = CustomSettings()

    dict_settings = settings.dict(exclude_none=True, upper=True)

    assert "my_custom" not in dict_settings

    assert dict_settings == {
        "DEBUG": False,
        "ENVIRONMENT": EnvironmentType.PRODUCTION,
        "VERSION": __version__,
        "MY_SETT": "works",
    }


def test_upper_dict():
    settings = CustomSettings()

    dict_settings = settings.dict(upper=True)

    assert "my_custom" not in dict_settings

    assert dict_settings == {
        "DEBUG": False,
        "ENVIRONMENT": EnvironmentType.PRODUCTION,
        "VERSION": __version__,
        "MY_SETT": "works",
        "MY_CUSTOM": None,
    }


def test_upper_tuple_exclude_none():
    settings = CustomSettings()

    tuple_settings = settings.tuple(exclude_none=True, upper=True)

    assert tuple_settings == [
        ("DEBUG", False),
        ("ENVIRONMENT", EnvironmentType.PRODUCTION),
        ("VERSION", __version__),
        ("MY_SETT", "works"),
    ]


def test_upper_tuple():
    settings = CustomSettings()

    tuple_settings = settings.tuple(upper=True)

    assert tuple_settings == [
        ("DEBUG", False),
        ("ENVIRONMENT", EnvironmentType.PRODUCTION),
        ("VERSION", __version__),
        ("MY_SETT", "works"),
        ("MY_CUSTOM", None),
    ]
