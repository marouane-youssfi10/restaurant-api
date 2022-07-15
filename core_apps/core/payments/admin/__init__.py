from django.contrib import admin

from dal_admin_filters import AutocompleteFilter

from core_apps.core.payments.models import Payment
from core_apps.utils.admin import ReadOnlyWithDetailAdmin


class UserFilter(AutocompleteFilter):
    title = "By user name"
    field_name = "user"
    autocomplete_url = "user-autocomplete"
    is_placeholder_title = True


class PaymentAdmin(ReadOnlyWithDetailAdmin):
    list_display = [
        "pkid",
        "user",
        "method",
        "amount_paid",
        "status",
        "created_at",
    ]
    list_display_links = ["pkid", "user"]
    list_filter = (UserFilter, "method", "status")


admin.site.register(Payment, PaymentAdmin)
