from django.contrib import admin

from core_apps.core.payments.models import Payment


class PaymentAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "payment_id",
        "user",
        "method",
        "amount_paid",
        "status",
    ]
    list_display_links = ["id", "payment_id", "user"]
    list_filter = ["method"]


admin.site.register(Payment, PaymentAdmin)
