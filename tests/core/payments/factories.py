import factory
import random
from factory import Faker

from core_apps.core.payments.models import Payment


class PaymentFactory(factory.django.DjangoModelFactory):
    user = factory.SubFactory("tests.core.users.factories.UserFactory")
    method = random.choice(["paypal", "stripe"])
    amount_paid = Faker("random_digit_not_null")
    status = factory.Iterator(["successful", "failed"])

    class Meta:
        model = Payment
