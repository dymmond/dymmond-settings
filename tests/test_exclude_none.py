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


def test_exclude_none_dict():
    settings = CustomSettings()

    dict_settings = settings.dict(exclude_none=True)

    assert "my_custom" not in dict_settings

    assert dict_settings == {
        "debug": False,
        "environment": EnvironmentType.PRODUCTION,
        "version": __version__,
        "my_sett": "works",
    }


def test_exclude_none_tuple():
    settings = CustomSettings()

    tuple_settings = settings.tuple(exclude_none=True)

    assert tuple_settings == [
        ("debug", False),
        ("environment", EnvironmentType.PRODUCTION),
        ("version", __version__),
        ("my_sett", "works"),
    ]
