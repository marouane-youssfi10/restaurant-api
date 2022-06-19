from django.contrib import admin
from django.urls import path
from django.conf import settings

urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls)
]
