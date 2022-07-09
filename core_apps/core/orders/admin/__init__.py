from django.contrib import admin
from django.utils.html import format_html

from core_apps.core.orders.models import (
    Order,
    AcceptedOrder,
    CompletedOrder,
    OrderItem,
    CancledOrder,
)
from core_apps.core.orders.utils import order_ref_generator


class OrderInline(admin.TabularInline):
    model = OrderItem
    extra = 1


class OrderAdmin(admin.ModelAdmin):
    list_display = [
        "pkid",
        "user_name",
        "payment",
        "order_number",
        "address",
        "country",
        "city",
        "order_total",
        "status",
        "is_ordered",
        "created_at",
    ]
    list_display_links = ["pkid", "order_number"]
    search_fields = ["user__username", "user__email"]

    class Meta:
        model = Order

    def get_queryset(self, request):
        return Order.objects.all_new_orders()

    def save_model(self, request, obj, form, change):
        obj.order_number = order_ref_generator()
        super().save_model(request, obj, form, change)

    def user_name(self, obj):
        return format_html(
            '<a href="/admin/users/user/?q={}">{} {}</a>',
            obj.user.username,
            obj.user.first_name,
            obj.user.last_name,
        )


class AcceptedOrderAdmin(admin.ModelAdmin):
    list_display = [
        "pkid",
        "user_name",
        "user_payment",
        "order_number",
        "address",
        "country",
        "city",
        "order_total",
        "status",
        "is_ordered",
        "updated_at",
    ]
    list_display_links = ["pkid", "order_number"]
    search_fields = ["user__username", "user__email"]
    inlines = [OrderInline]

    class Meta:
        model = AcceptedOrder

    def get_queryset(self, request):
        return AcceptedOrder.objects.all_order_accepted()

    def user_payment(self, obj):
        return format_html(
            '<a href="/admin/payments/payment/{}/change/">{}</a>',
            obj.payment.pkid,
            obj.payment,
        )

    def user_name(self, obj):
        return format_html(
            '<a href="/admin/users/user/?q={}">{} {}</a>',
            obj.user.username,
            obj.user.first_name,
            obj.user.last_name,
        )


class CompletedOrderAdmin(admin.ModelAdmin):
    list_display = [
        "pkid",
        "user_name",
        "order_number",
        "address",
        "country",
        "city",
        "order_total",
        "status",
        "is_ordered",
        "updated_at",
    ]
    list_display_links = ["pkid", "order_number"]
    search_fields = ["user__username", "user__email"]
    inlines = [OrderInline]

    class Meta:
        model = CompletedOrder

    def get_queryset(self, request):
        return CompletedOrder.objects.all_order_completed()

    def user_name(self, obj):
        return format_html(
            '<a href="/admin/users/user/?q={}">{} {}</a>',
            obj.user.username,
            obj.user.first_name,
            obj.user.last_name,
        )


class CancledOrderAdmin(admin.ModelAdmin):
    list_display = [
        "pkid",
        "user_name",
        "order_number",
        "address",
        "country",
        "city",
        "order_total",
        "status",
        "is_ordered",
        "updated_at",
    ]
    list_display_links = ["pkid", "order_number"]
    search_fields = ["user__username", "user__email"]
    inlines = [OrderInline]

    class Meta:
        model = CancledOrder

    def get_queryset(self, request):
        return CancledOrder.objects.all_order_cancled()

    def user_name(self, obj):
        return format_html(
            '<a href="/admin/users/user/?q={}">{} {}</a>',
            obj.user.username,
            obj.user.first_name,
            obj.user.last_name,
        )


class OrderItemAdmin(admin.ModelAdmin):
    list_display = [
        "pkid",
        "user_name",
        "order_id",
        "payment",
        "quantity",
        "food_price",
        "ordered",
        "created_at",
    ]
    list_display_links = ["pkid"]
    list_filter = ["ordered"]
    search_fields = ["user__username", "user__email"]

    def user_name(self, obj):
        return format_html(
            '<a href="/admin/users/user/?q={}">{} {}</a>',
            obj.user.username,
            obj.user.first_name,
            obj.user.last_name,
        )

    def order_id(self, obj):
        return format_html(
            '<a href="/admin/orders/acceptedorder/{}/change">{}</a>',
            obj.order.pkid,
            obj.order,
        )


admin.site.register(Order, OrderAdmin)
admin.site.register(AcceptedOrder, AcceptedOrderAdmin)
admin.site.register(CompletedOrder, CompletedOrderAdmin)
admin.site.register(CancledOrder, CancledOrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
