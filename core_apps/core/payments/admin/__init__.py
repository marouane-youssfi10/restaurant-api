from django.contrib import admin

from core_apps.core.payments.models import Payment


class PaymentAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "pkid",
        "user",
        "method",
        "amount_paid",
        "status",
    ]
    list_display_links = ["id", "pkid", "user"]
    list_filter = ["method", "status"]


admin.site.register(Payment, PaymentAdmin)
