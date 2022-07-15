from dal import autocomplete
from django.db.models import Q

from core_apps.core.orders.models import OrderItem


class OrderAutocompleteView(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = OrderItem.objects.all()
        if self.q:
            qs = qs.filter(Q(order__order_number__istartswith=self.q))
        return qs
