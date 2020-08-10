from django.urls import path

from smcrm.developers.views import DevelopersView

app_name = "developers"
urlpatterns = [
    path("developers/", view=DevelopersView.as_view(), name="developers"),
]

