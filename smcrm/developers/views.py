from django.views.generic import ListView

from smcrm.developers.models import Developer


class DevelopersView(ListView):
    model = Developer

    def get_queryset(self):
        return super().get_queryset().filter(manager=self.request.user)
