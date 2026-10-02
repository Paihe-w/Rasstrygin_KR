from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("scenario/<slug:scenario>/", views.run_scenario, name="run_scenario"),
]
