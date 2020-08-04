from django.urls import reverse
from django.views.generic import ListView, CreateView
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from projects.permissions import IsOwner
from projects.serializers import ProjectSerializer
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


class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    permission_classes = (IsAuthenticated, IsOwner)
    serializer_class = ProjectSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)
