from django.contrib import admin
from django.utils.html import format_html

from core_apps.core.profiles.models import Customer
from core_apps.utils.admin import ReadOnlyWithDetailAdmin

from dal_admin_filters import AutocompleteFilter
from import_export.admin import ImportExportModelAdmin


class UserFilter(AutocompleteFilter):
    title = "By user name"
    field_name = "user"
    autocomplete_url = "user-autocomplete"
    is_placeholder_title = True


class CustomerAdmin(ReadOnlyWithDetailAdmin, ImportExportModelAdmin):
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
    list_filter = (UserFilter, "city")

    def has_change_permission(self, request, obj=None) -> bool:
        return True

    def user_name(self, obj: Customer):
        return format_html(
            '<a href="/admin/users/user/?q={}">{} {}</a>',
            obj.user.username,
            obj.user.first_name,
            obj.user.last_name,
        )


admin.site.register(Customer, CustomerAdmin)
