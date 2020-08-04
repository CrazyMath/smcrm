from django.urls import path
from rest_framework import routers

from smcrm.projects.views import ProjectsView, ProjectCreateView, ProjectModelViewSet

router = routers.SimpleRouter()
router.register(r'api/projects', ProjectModelViewSet)
urlpatterns = router.urls

app_name = "projects"
urlpatterns += [
    path("projects/", view=ProjectsView.as_view(), name="projects"),
    path("projects/create/", view=ProjectCreateView.as_view(), name="project_create"),
]

