from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ProjectsConfig(AppConfig):
    name = "smcrm.projects"
    verbose_name = _("Projects")
    def ready(self):
        try:
            import smcrm.projects.signals  # noqa F401
        except ImportError:
            pass
