from dataclasses import dataclass, field

from dymmond_settings import Settings


@dataclass
class CustomSettings(Settings):
    """
    A custom settings that allows the __repr__
    """

    my_sett: str = field(default="works")

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}()"


def test_fields():
    settings = CustomSettings()

    assert settings.my_sett == "works"

    assert repr(settings) == "CustomSettings()"
