from dal import autocomplete
from django.db.models import Q

from core_apps.core.users.models import User


class UserAutocompleteView(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = User.objects.all()
        print("\n\nself.q = ", self.q, "\n\n")
        if self.q:
            qs = qs.filter(
                Q(first_name__istartswith=self.q) | Q(last_name__istartswith=self.q)
            )
        return qs
