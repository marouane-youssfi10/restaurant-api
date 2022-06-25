import factory


from factory import Faker

from core_apps.core.menu.models import Category, Food


class CategoryFactory(factory.django.DjangoModelFactory):
    category_name = Faker("name")

    class Meta:
        model = Category


class FoodFactory(factory.django.DjangoModelFactory):
    category = factory.SubFactory(CategoryFactory)
    food_name = Faker("name")
    price = Faker("random_digit_not_null")

    class Meta:
        model = Food
