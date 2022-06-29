from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
    path("api/", include("core_apps.apis.users.urls", namespace="user")),
    path("api/menu/", include("core_apps.apis.menu.urls", namespace="menu")),
    path("api/carts/", include("core_apps.apis.cart.urls", namespace="cart")),
    path("api/profiles/", include("core_apps.apis.profiles.urls", namespace="profile")),
    path("api/orders/", include("core_apps.apis.orders.urls", namespace="order")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_header = "Restaurant API Admin"
admin.site.index_title = "Welcome to the Restaurant Haven API Portal"
