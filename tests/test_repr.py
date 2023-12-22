from dataclasses import dataclass

from dymmond_settings import Settings


@dataclass
class CustomSettings(Settings):
    """
    A custom settings that allows the __repr__
    """

    debug: bool = True
    is_repr: bool = True

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(repr={self.is_repr})"


def test_repr():
    settings = CustomSettings()

    assert repr(settings) == "CustomSettings(repr=True)"


def test_override():
    settings = CustomSettings()

    assert settings.debug is True
