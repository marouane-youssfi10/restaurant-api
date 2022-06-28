import factory
from factory import Faker

from core_apps.core.profiles.models import Customer


class CustomerFactory(factory.django.DjangoModelFactory):
    user = factory.SubFactory("tests.core.users.factories.UserFactory")
    gender = Customer.Gender.MALE
    phone_number = Faker("phone_number")
    address = Faker("address")
    country = Faker("country")
    city = Faker("city")

    class Meta:
        model = Customer
