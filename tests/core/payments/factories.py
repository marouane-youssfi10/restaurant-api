import uuid
import factory
import random
from factory import Faker

from core_apps.core.payments.models import Payment


class PaymentFactory(factory.django.DjangoModelFactory):
    payment_id = factory.LazyAttribute(lambda a: str(uuid.uuid4().__str__()))
    user = factory.SubFactory("tests.core.users.factories.UserFactory")
    method = random.choice([True, False])
    amount_paid = Faker("random_digit_not_null")
    status = factory.Iterator(["paypal", "stripe"])

    class Meta:
        model = Payment
