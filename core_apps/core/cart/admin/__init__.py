from django.contrib import admin
from core_apps.core.cart.models import Cart

# class FoodInline(admin.TabularInline):
#     model = Food


class CartAdmin(admin.ModelAdmin):
    list_display = ["pkid", "user", "food", "quantity", "sub_total"]
    list_filter = ["created_at", "user"]
    search_fields = ["user"]
    list_editable = ["quantity"]
    # raw_id_fields = ["user"]
    # inlines=[FoodInline,]


admin.site.register(Cart, CartAdmin)
