from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView

from smcrm.projects.models import Project


class ProjectsView(ListView):
    model = Project

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)


class ProjectCreateView(CreateView):
    model = Project
    fields = ('name', 'description', 'user')

    def get_initial(self):
        initial = super().get_initial()
        initial['user'] = self.request.user
        return initial

    def get_success_url(self):
        return reverse('projects:projects')




