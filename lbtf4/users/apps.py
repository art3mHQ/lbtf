import contextlib

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "lbtf4.users"
    verbose_name = _("Users")

    def ready(self):
        with contextlib.suppress(ImportError):
            import lbtf4.users.signals  # noqa: F401
