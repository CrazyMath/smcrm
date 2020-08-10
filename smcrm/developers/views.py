from django.views.generic import ListView
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from smcrm.developers.serializers import DeveloperSerializer
from smcrm.projects.permissions import IsOwner
from smcrm.developers.models import Developer


class DevelopersView(ListView):
    model = Developer

    def get_queryset(self):
        return super().get_queryset().filter(manager=self.request.user)


class DeveloperModelViewSet(ModelViewSet):
    queryset = Developer.objects.all()
    permission_classes = (IsAuthenticated, IsOwner)
    serializer_class = DeveloperSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(manager=self.request.user)

    def perform_create(self, serializer):
        serializer.save(manager=self.request.user)
