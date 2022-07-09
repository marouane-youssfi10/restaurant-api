from django.contrib import admin
from django.utils.html import format_html

from core_apps.core.cart.models import Cart

# class FoodInline(admin.TabularInline):
#     model = Food


class CartAdmin(admin.ModelAdmin):
    list_display = [
        "pkid",
        "user_name",
        "food_name",
        "quantity",
        "sub_total",
        "created_at",
        "updated_at",
    ]
    list_filter = ["created_at"]
    search_fields = ["user__username", "user__email"]
    list_editable = ["quantity"]
    # raw_id_fields = ["user"]
    # inlines=[FoodInline,]

    def user_name(self, obj):
        return format_html(
            '<a href="/admin/users/user/?q={}">{} {}</a>',
            obj.user.username,
            obj.user.first_name,
            obj.user.last_name,
        )

    def food_name(self, obj):
        return format_html(
            '<a href="/admin/menu/food/{}/change">{}</a>',
            obj.food.pkid,
            obj.food.food_name,
        )


admin.site.register(Cart, CartAdmin)
