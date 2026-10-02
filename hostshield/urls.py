from django.urls import include, path

urlpatterns = [path("", include("security_console.urls"))]
