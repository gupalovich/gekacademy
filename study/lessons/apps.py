from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class LessonsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'lessons.core'
    verbose_name = _("Lessons")

    def ready(self):
        try:
            import study.lessons.signals  # noqa F401
        except ImportError:
            pass
