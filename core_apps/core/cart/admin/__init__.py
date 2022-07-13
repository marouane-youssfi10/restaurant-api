from django.contrib import admin
from django.utils.html import format_html

from core_apps.core.cart.models import Cart
from core_apps.utils.admin import ReadOnlyWithDetailAdmin


class CartAdmin(ReadOnlyWithDetailAdmin):
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "pkid",
                    "user_name",
                    "food_name",
                    "food_price",
                    "quantity",
                    "sub_total",
                    "created_at",
                    "updated_at",
                )
            },
        ),
    )
    list_display = [
        "pkid",
        "user_name",
        "food_name",
        "food_price",
        "quantity",
        "sub_total",
        "created_at",
        "updated_at",
    ]
    list_filter = ["created_at"]
    search_fields = ["user__username", "user__email"]
    list_editable = ["quantity"]

    def user_name(self, obj: Cart):
        return format_html(
            '<a href="/admin/users/user/?q={}">{} {}</a>',
            obj.user.username,
            obj.user.first_name,
            obj.user.last_name,
        )

    def food_name(self, obj: Cart):
        return format_html(
            '<a href="/admin/menu/food/{}/change">{}</a>',
            obj.food.pkid,
            obj.food.food_name,
        )

    def sub_total(self, obj: Cart):
        return str(obj.sub_total()) + str(" dh")

    def food_price(self, obj: Cart):
        return str(obj.food.price) + str(" dh")


admin.site.register(Cart, CartAdmin)
