from django.urls import path

from smcrm.projects.views import ProjectsView, ProjectCreateView

app_name = "projects"
urlpatterns = [
    path("", view=ProjectsView.as_view(), name="projects"),
    path("create/", view=ProjectCreateView.as_view(), name="project_create"),
]

