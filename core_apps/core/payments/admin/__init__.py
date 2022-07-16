from django.contrib import admin
from django.utils.html import format_html
from dal_admin_filters import AutocompleteFilter

from core_apps.core.payments.models import Payment
from core_apps.utils.admin import ReadOnlyWithDetailAdmin


class UserFilter(AutocompleteFilter):
    title = "By user name"
    field_name = "user"
    autocomplete_url = "user-autocomplete"
    is_placeholder_title = True


class PaymentAdmin(ReadOnlyWithDetailAdmin):
    readonly_fields = ("created_at", "updated_at")
    list_display = [
        "pkid",
        "user_name",
        "method",
        "amount_paid",
        "status_payment",
        "created_at",
    ]
    list_display_links = ["pkid"]
    list_filter = (UserFilter, "method", "status")

    def user_name(self, obj: Payment):
        return format_html(
            '<a href="/admin/users/user/?q={}">{} {}</a>',
            obj.user.username,
            obj.user.first_name,
            obj.user.last_name,
        )

    def status_payment(self, obj: Payment):
        method = "#E14321"
        if obj.status == "successful":
            method = "#4D9C42"

        return format_html(
            '<b class="button" style="background-color:{};">{}</b>'.format(
                method,
                obj.status,
            )
        )


admin.site.register(Payment, PaymentAdmin)
