from django.contrib import admin

from core_apps.core.profiles.models import Customer


class CustomerAdmin(admin.ModelAdmin):
    list_display = [
        "pkid",
        "user",
        "phone_number",
        "gender",
        "address",
        "country",
        "city",
    ]
    list_display_links = ["pkid", "user"]


admin.site.register(Customer, CustomerAdmin)
