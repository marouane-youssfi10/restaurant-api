import pytest

from tests.core.menu.factories import (
    CategoryFactory,
    FoodGalleryFactory,
    ReviewRatingFactory,
)


@pytest.mark.django_db
def test_category__str__(user):
    category = CategoryFactory()
    assert category.__str__() == f"{category.category_name}"


@pytest.mark.django_db
def test_food_gallery__str__(user):
    foodgallery = FoodGalleryFactory()
    assert foodgallery.__str__() == f"{foodgallery.food} gallery"


@pytest.mark.django_db
def test_review_rating__str__(user):
    review_rating = ReviewRatingFactory()
    assert review_rating.__str__() == f"{review_rating.user.username} review"
