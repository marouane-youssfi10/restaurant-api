import uuid
import factory

from random import randint, random
from factory import Faker

from core_apps.core.orders.models import Order, OrderItem


class OrderFactory(factory.django.DjangoModelFactory):
    user = factory.SubFactory("tests.core.users.factories.UserFactory")
    payment = factory.SubFactory("tests.core.payments.factories.PaymentFactory")
    address = factory.Faker("address")
    country = factory.Faker("country")
    city = factory.Faker("city")
    order_number = factory.LazyAttribute(lambda a: str(uuid.uuid4().__str__())[:8])
    order_total = factory.LazyAttribute(lambda a: round(randint(1, 100) + random(), 2))
    is_ordered = True

    class Meta:
        model = Order

    class Params:
        with_address_country_city = factory.Trait(
            status=Order.Gender.NEW, is_ordered=False
        )
        with_status_and_is_ordered = factory.Trait(
            status=Order.Gender.NEW, is_ordered=False
        )


class OrderItemFactory(factory.django.DjangoModelFactory):
    user = factory.SubFactory("tests.core.users.factories.UserFactory")
    food = factory.SubFactory("tests.core.menu.factories.FoodFactory")
    payment = factory.SubFactory("tests.core.payments.factories.PaymentFactory")
    order = factory.SubFactory(OrderFactory)
    quantity = Faker("random_digit_not_null")
    food_price = factory.LazyAttribute(lambda a: round(randint(1, 100) + random(), 2))
    ordered = True

    class Meta:
        model = OrderItem
