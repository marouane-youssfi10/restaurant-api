from django.contrib import admin
from django.utils.html import format_html

from core_apps.core.profiles.models import Customer


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
