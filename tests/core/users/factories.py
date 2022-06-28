import factory
from factory import Faker

from django.core.files.base import ContentFile
from core_apps.core.users.models import User


class UserFactory(factory.django.DjangoModelFactory):
    email = Faker("email")
    first_name = Faker("first_name")
    last_name = Faker("last_name")
    username = Faker("first_name")
    profile_photo = factory.LazyAttribute(
        lambda _: ContentFile(
            factory.django.ImageField()._make_data({"width": 1024, "height": 768}),
            "example.jpg",
        )
    )

    class Meta:
        model = User

    class Params:
        superuser = factory.Trait(is_staff=True, is_superuser=True)
        staff = factory.Trait(is_staff=True)
