import factory
from random import randint, random
from django.core.files.base import ContentFile


from factory import Faker

from core_apps.core.menu.models import Category, Food, FoodGallery, ReviewRating


class CategoryFactory(factory.django.DjangoModelFactory):
    category_name = Faker("name")

    class Meta:
        model = Category

    class Params:
        with_image = factory.Trait(
            category_image=factory.LazyAttribute(
                lambda _: ContentFile(
                    factory.django.ImageField()._make_data(
                        {"width": 1024, "height": 768}
                    ),
                    "category_image.jpg",
                )
            )
        )


class FoodFactory(factory.django.DjangoModelFactory):
    category = factory.SubFactory(CategoryFactory)
    food_name = Faker("name")
    price = Faker("random_digit_not_null")

    class Meta:
        model = Food


class FoodGalleryFactory(factory.django.DjangoModelFactory):
    food = factory.SubFactory(FoodFactory)

    class Meta:
        model = FoodGallery

    class Params:
        with_image = factory.Trait(
            food_images=factory.LazyAttribute(
                lambda _: ContentFile(
                    factory.django.ImageField()._make_data(
                        {"width": 1024, "height": 768}
                    ),
                    "food_image.jpg",
                )
            )
        )


class ReviewRatingFactory(factory.django.DjangoModelFactory):
    user = factory.SubFactory("tests.core.users.factories.UserFactory")
    food = factory.SubFactory(FoodFactory)
    review = factory.Faker("name")
    rating = factory.LazyAttribute(lambda a: round(randint(1, 5) + random(), 2))

    class Meta:
        model = ReviewRating
