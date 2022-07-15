import logging

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path

logger = logging.getLogger(__name__)


urlpatterns = [
    # Public APIs URLs
    path(f"api/", include("core_project.urls.apis")),
    # Private APIs & Admin
    path(f"", include("core_project.urls.admin")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
