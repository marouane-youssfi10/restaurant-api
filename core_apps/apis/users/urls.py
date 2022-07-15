from django.urls import path, include


app_name = "user"

urlpatterns = [
    path("", include("djoser.urls")),
    path("", include("djoser.urls.jwt")),
]
