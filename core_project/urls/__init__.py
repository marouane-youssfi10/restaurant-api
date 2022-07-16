import logging

from django.conf import settings
from django.urls import include, path, re_path as url
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.http import HttpResponse

logger = logging.getLogger(__name__)


def welcome(request):
    html = "<h1 style='font-size:36px;text-align: center;'>Welcome</h1>"
    logger.info("\n ======= Welcome ======= \n")
    return HttpResponse(html)


urlpatterns = [
    url(r"^$", welcome, name="welcome"),
    # Public APIs URLs
    path(f"api/", include("core_project.urls.apis")),
    # Private APIs & Admin
    path(f"", include("core_project.urls.admin")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
