from django.contrib import admin
from django.utils.html import format_html

from core_apps.core.profiles.models import Customer

from dal_admin_filters import AutocompleteFilter


class UserFilter(AutocompleteFilter):
    title = "By user name"
    field_name = "user"
    autocomplete_url = "user-autocomplete"
    is_placeholder_title = True


class CustomerAdmin(admin.ModelAdmin):
    list_display = [
        "pkid",
        "user_name",
        "phone_number",
        "gender",
        "address",
        "country",
        "city",
    ]
    list_display_links = ["pkid"]
    list_filter = (UserFilter,)

    def has_delete_permission(self, request, obj=None) -> bool:
        return False

    def user_name(self, obj: Customer):
        return format_html(
            '<a href="/admin/users/user/?q={}">{} {}</a>',
            obj.user.username,
            obj.user.first_name,
            obj.user.last_name,
        )


admin.site.register(Customer, CustomerAdmin)
