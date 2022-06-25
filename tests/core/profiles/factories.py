import factory
from factory import Faker

from django.core.files.base import ContentFile
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

    class Params:
        profile_photo = factory.LazyAttribute(
            lambda _: ContentFile(
                factory.django.ImageField()._make_data({"width": 1024, "height": 768}),
                "example.jpg",
            )
        )
