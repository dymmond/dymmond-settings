from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Any, Dict, List, Optional, Tuple, Union

from typing_extensions import Annotated, Doc

from dymmond_settings import __version__
from dymmond_settings.enums import EnvironmentType


@dataclass
class BaseSettings:
    """
    Base of all the settings for any system.
    """

    def dict(self, exclude_none: bool = False) -> Dict[str, Any]:
        """
        Dumps all the settings into a python dictionary.
        """
        if not exclude_none:
            return asdict(self)
        return {k: v for k, v in self.__dict__.items() if v is not None}

    def tuple(self, exclude_none: bool = False) -> List[Tuple[str, Any]]:
        """
        Dumps all the settings into a tuple.
        """
        if not exclude_none:
            return list(self.__dict__.items())
        return [(k, v) for k, v in self.__dict__.items() if v is not None]


@dataclass
class Settings(BaseSettings):
    debug: Annotated[
        bool,
        Doc(
            """
            Boolean indicating if the application should return the debug tracebacks on
            server errors, in other words, if you want to have debug errors being displayed.

            !!! Tip
                Do not use this in production as `True`.
            """
        ),
    ] = field(default=False)
    environment: Annotated[
        Optional[str],
        Doc(
            """
            Optional string indicating the environment where the settings are running.
            You won't probably need this but it is here in case you might want to use.
            """
        ),
    ] = field(default=EnvironmentType.PRODUCTION)
    version: Annotated[
        Union[str, int, float],
        Doc(
            """
            The version of the application and defaults to the current version of the settings
            system if not set.
            """
        ),
    ] = field(default=__version__)
