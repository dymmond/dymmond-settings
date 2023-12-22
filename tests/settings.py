from dataclasses import dataclass

from dymmond_settings.base import Settings
from dymmond_settings.enums import EnvironmentType


@dataclass
class TestSettings(Settings):
    debug: bool = True
    environment: str = EnvironmentType.TESTING.value
