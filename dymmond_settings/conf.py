import os
from typing import TYPE_CHECKING, Any, Optional, Type

from dymmond_settings.functional import LazyObject, empty
from dymmond_settings.module_loading import import_string

if TYPE_CHECKING:
    from dymmond_settings.base import Settings

ENVIRONMENT_VARIABLE = "SETTINGS_MODULE"


class LazySettings(LazyObject):
    """
    A lazy proxy for either global application settings or a custom settings object.
    The user can manually configure settings prior to using them. Otherwise,
    The system uses the settings module pointed to by SETTINGS_MODULE.
    """

    def _setup(self, name: Optional[str] = None) -> None:
        """
        Load the settings module pointed to by the environment variable. This
        is used the first time settings are needed, if the user hasn't
        configured settings manually.
        """
        settings_module: str = os.environ.get(
            ENVIRONMENT_VARIABLE, "dymmond_settings.global_settings.Settings"
        )

        settings: Type["Settings"] = import_string(settings_module)

        for setting, _ in settings().dict().items():
            assert setting.islower(), "%s should be in lower case." % setting

        self._wrapped = settings()

    def __repr__(self: "LazySettings") -> str:
        # Hardcode the class name as otherwise it yields 'Settings'.
        if self._wrapped is empty:
            return "<LazySettings [Unevaluated]>"
        return '<LazySettings "{settings_module}">'.format(
            settings_module=self._wrapped.__class__.__name__
        )

    @property
    def configured(self) -> Any:
        """Return True if the settings have already been configured."""
        return self._wrapped is not empty


settings: Type["Settings"] = LazySettings()  # type: ignore
