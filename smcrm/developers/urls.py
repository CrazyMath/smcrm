from django.urls import path
from rest_framework import routers

from smcrm.developers.views import DevelopersView, DeveloperModelViewSet

router = routers.SimpleRouter()
router.register(r'api/projects', DeveloperModelViewSet, basename='developers')
urlpatterns = router.urls


app_name = "developers"
urlpatterns += [
    path("developers/", view=DevelopersView.as_view(), name="developers"),
]

