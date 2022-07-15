from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions


schema_view = get_schema_view(
    openapi.Info(
        title="API Documentation",
        default_version="v1",
        description="API endpoints form the Restaurant API",
        contact=openapi.Contact(email="marouaneyoussfi@gmail.com"),
        basePath="/api/",
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    urlconf="core_project.urls",
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    path("", include("core_apps.apis.users.urls", namespace="user")),
    path("menu/", include("core_apps.apis.menu.urls", namespace="menu")),
    path("carts/", include("core_apps.apis.cart.urls", namespace="cart")),
    path("profiles/", include("core_apps.apis.profiles.urls", namespace="profile")),
    path("orders/", include("core_apps.apis.orders.urls", namespace="order")),
    path("payments/", include("core_apps.apis.payments.urls", namespace="payment")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_header = "Restaurant API Admin"
admin.site.index_title = "Welcome to the Restaurant API"
