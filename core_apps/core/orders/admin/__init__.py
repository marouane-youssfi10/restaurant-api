from django.contrib import admin
from django.utils.html import format_html

from core_apps.core.orders.models import (
    Order,
    AcceptedOrder,
    CompletedOrder,
    OrderItem,
    CancledOrder,
)
from core_apps.utils.admin import ReadOnlyWithDetailAdmin
from core_apps.utils.generators import generate_order_number


class OrderInline(admin.TabularInline):
    model = OrderItem
    extra = 1


class OrderMain(ReadOnlyWithDetailAdmin):
    list_display = [
        "pkid",
        "user_name",
        "user_payment",
        "order_number",
        "address",
        "country",
        "city",
        "order_total",
        "user_status",
        "is_ordered",
        "created_at",
        "updated_at",
    ]
    list_display_links = ["pkid", "order_number"]
    readonly_fields = (
        "user",
        "payment",
        "order_number",
        "address",
        "order_total",
        "country",
        "city",
        "order_note",
        "is_ordered",
    )
    search_fields = ["user__username", "user__email"]
    inlines = [OrderInline]

    def has_change_permission(self, request, obj=None):
        return True

    def user_name(self, obj: Order):
        return format_html(
            '<a href="/admin/users/user/?q={}">{} {}</a>',
            obj.user.username,
            obj.user.first_name,
            obj.user.last_name,
        )

    def user_payment(self, obj: Order):
        payment = "-"
        if obj.payment:
            return format_html(
                '<a href="/admin/payments/payment/{}/change/">{}</a>',
                obj.payment.pkid,
                obj.payment,
            )
        return payment


class OrderAdmin(OrderMain):
    class Meta:
        model = Order

    def get_queryset(self, request):
        return Order.objects.all_new_orders()

    def save_model(self, request, obj, form, change):
        obj.order_number = generate_order_number()
        super().save_model(request, obj, form, change)

    def user_status(self, obj: Order):
        return format_html(
            '<b class="button" style="background-color:#47CAC2;">{}</b>'.format(
                obj.status
            )
        )


class AcceptedOrderAdmin(OrderMain):
    class Meta:
        model = AcceptedOrder

    def get_queryset(self, request):
        return AcceptedOrder.objects.all_order_accepted()

    def user_status(self, obj: AcceptedOrder):
        return format_html(
            '<b class="button" style="background-color:#70bf2c;">{}</b>'.format(
                obj.status
            )
        )


class CompletedOrderAdmin(OrderMain):
    class Meta:
        model = CompletedOrder

    def get_queryset(self, request):
        return CompletedOrder.objects.all_order_completed()

    def user_status(self, obj: CompletedOrder):
        return format_html(
            '<b class="button" style="background-color:#46C0D9;">{}</b>'.format(
                obj.status
            )
        )


class CancledOrderAdmin(OrderMain):
    class Meta:
        model = CancledOrder

    def get_queryset(self, request):
        return CancledOrder.objects.all_order_cancled()

    def user_status(self, obj: CancledOrder):
        return format_html(
            '<b class="button" style="background-color:#E15648;">{}</b>'.format(
                obj.status
            )
        )


class OrderItemAdmin(ReadOnlyWithDetailAdmin):
    list_display = [
        "pkid",
        "user_name",
        "order_id",
        "user_payment",
        "quantity",
        "food_price",
        "ordered",
        "created_at",
    ]
    list_display_links = ["pkid"]
    list_filter = ["ordered"]
    readonly_fields = (
        "user",
        "food",
        "order",
        "payment",
        "quantity",
        "food_price",
        "created_at",
        "updated_at",
    )
    search_fields = ["user__username", "user__email"]

    def has_change_permission(self, request, obj=None) -> bool:
        return True

    def user_name(self, obj: OrderItem):
        return format_html(
            '<a href="/admin/users/user/?q={}">{} {}</a>',
            obj.user.username,
            obj.user.first_name,
            obj.user.last_name,
        )

    def user_payment(self, obj: OrderItem):
        return format_html(
            '<a href="/admin/payments/payment/{}/change/">{}</a>',
            obj.payment.pkid,
            obj.payment,
        )

    def order_id(self, obj: OrderItem):
        return format_html(
            '<a href="/admin/orders/{}order/{}/change">{}</a>',
            obj.order.status,
            obj.order.pkid,
            obj.order,
        )


admin.site.register(Order, OrderAdmin)
admin.site.register(AcceptedOrder, AcceptedOrderAdmin)
admin.site.register(CompletedOrder, CompletedOrderAdmin)
admin.site.register(CancledOrder, CancledOrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
