from django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
    path("api/", include("core_apps.apis.users.urls", namespace="user")),
]


admin.site.site_header = "Restaurant API Admin"
admin.site.index_title = "Welcome to the Restaurant Haven API Portal"
