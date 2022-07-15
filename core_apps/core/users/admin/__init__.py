from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.db.models import Count
from django.utils.translation import gettext_lazy as _

from core_apps.core.users.admin.forms import UserChangeForm, UserCreationForm

User = get_user_model()


class UserAdmin(BaseUserAdmin):
    ordering = ["-pkid"]
    add_form = UserCreationForm
    form = UserChangeForm
    model = User
    list_display = [
        "pkid",
        "email",
        "username",
        "first_name",
        "last_name",
        "orders_count",
        "is_staff",
        "is_active",
    ]
    list_display_links = ["email"]
    list_filter = ("is_staff",)
    fieldsets = (
        (
            _("Login Credentials"),
            {"fields": ("email", "password")},
        ),
        (
            _("Personal Information"),
            {
                "fields": (
                    "username",
                    "first_name",
                    "last_name",
                    "profile_photo",
                    "display_picture",
                )
            },
        ),
        (
            _("Permissions and Groups"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        (_("Important Dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2", "is_staff", "is_active"),
            },
        ),
    )
    readonly_fields = ("display_picture",)
    search_fields = ["email", "username", "first_name", "last_name"]

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.annotate(
            _orders_count=Count("user_order", distinct=True),
        ).order_by("-_orders_count")
        return queryset

    def orders_count(self, obj):
        return obj._orders_count

    orders_count.admin_order_field = "_orders_count"


admin.site.register(User, UserAdmin)
