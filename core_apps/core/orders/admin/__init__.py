from django.contrib import admin

from core_apps.core.orders.models import (
    Order,
    AcceptedOrder,
    CompletedOrder,
    OrderItem,
    CancledOrder,
)


class OrderAdmin(admin.ModelAdmin):
    list_display = [
        "pkid",
        "user",
        "order_number",
        "address",
        "country",
        "city",
        "order_total",
        "status",
        "is_ordered",
    ]
    list_display_links = ["pkid", "user", "order_number"]
    search_fields = ["user"]

    class Meta:
        model = Order

    def get_queryset(self, request):
        return Order.objects.all_new_orders()


class AcceptedOrderAdmin(admin.ModelAdmin):
    list_display = [
        "pkid",
        "user",
        "order_number",
        "address",
        "country",
        "city",
        "order_total",
        "status",
        "is_ordered",
    ]
    list_display_links = ["pkid", "user", "order_number"]
    search_fields = ["user"]

    class Meta:
        model = AcceptedOrder

    def get_queryset(self, request):
        return AcceptedOrder.objects.all_order_accepted()


class CompletedOrderAdmin(admin.ModelAdmin):
    list_display = [
        "pkid",
        "user",
        "order_number",
        "address",
        "country",
        "city",
        "order_total",
        "status",
        "is_ordered",
    ]
    list_display_links = ["pkid", "user", "order_number"]
    search_fields = ["user"]

    class Meta:
        model = CompletedOrder

    def get_queryset(self, request):
        return CompletedOrder.objects.all_order_completed()


class CancledOrderAdmin(admin.ModelAdmin):
    list_display = [
        "pkid",
        "user",
        "order_number",
        "address",
        "country",
        "city",
        "order_total",
        "status",
        "is_ordered",
    ]
    list_display_links = ["pkid", "user", "order_number"]
    search_fields = ["user"]

    class Meta:
        model = CancledOrder

    def get_queryset(self, request):
        return CancledOrder.objects.all_order_cancled()


class OrderItemAdmin(admin.ModelAdmin):
    list_display = [
        "pkid",
        "user",
        "order",
        "quantity",
        "food_price",
        "ordered",
    ]
    list_display_links = ["pkid", "user", "order"]
    list_filter = ["ordered"]
    search_fields = ["user"]


admin.site.register(Order, OrderAdmin)
admin.site.register(AcceptedOrder, AcceptedOrderAdmin)
admin.site.register(CompletedOrder, CompletedOrderAdmin)
admin.site.register(CancledOrder, CancledOrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
