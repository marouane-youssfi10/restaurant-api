import factory
from factory import Faker

from core_apps.core.cart.models import Cart


class CartFactory(factory.django.DjangoModelFactory):
    user = factory.SubFactory("tests.core.users.factories.UserFactory")
    food = factory.SubFactory("tests.core.menu.factories.FoodFactory")
    quantity = Faker("random_digit_not_null")

    class Meta:
        model = Cart
