from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class DevelopersConfig(AppConfig):
    name = "smcrm.developers"
    verbose_name = _("Developers")

    def ready(self):
        try:
            import smcrm.developers.signals  # noqa F401
        except ImportError:
            pass
