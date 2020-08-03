from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext as _
from django_extensions.db.models import TimeStampedModel

User = get_user_model()


class Project(TimeStampedModel):
    name = models.CharField(max_length=255, verbose_name=_('Name'))
    description = models.TextField(verbose_name=_('Description'), blank=True, null=True)

    user = models.ForeignKey(User, related_name='projects', verbose_name=_('User'), on_delete=models.CASCADE)

    developers = models.ManyToManyField('developers.Developer', blank=True, related_name='projects')

    @property
    def total_tasks(self):
        return self.tasks.all().count()

    @property
    def total_developers(self):
        return self.developers.count()

    def __str__(self):
        return self.name


class Task(TimeStampedModel):
    name = models.CharField(max_length=255, verbose_name=_('Name'))
    description = models.TextField(verbose_name=_('Description'), blank=True, null=True)
    estimate = models.FloatField(verbose_name=_('Estimate'), null=True)

    project = models.ForeignKey(Project, related_name='tasks', verbose_name=_('Project'), on_delete=models.CASCADE)
