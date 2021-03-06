from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext as _
from django_extensions.db.models import TimeStampedModel

User = get_user_model()


class Developer(TimeStampedModel):
    name = models.CharField(max_length=255, verbose_name=_('Name'))
    productivity = models.FloatField(verbose_name=_('Productivity'), default=1)

    manager = models.ForeignKey(User, related_name='developers', verbose_name=_('manager'), on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    @property
    def owner(self):
        return self.manager
