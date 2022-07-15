import pytest

from tests.core.menu.factories import (
    CategoryFactory,
    FoodFactory,
    FoodGalleryFactory,
    ReviewRatingFactory,
)


@pytest.mark.django_db
def test_category_factory():
    instance = CategoryFactory()
    assert instance.pkid


@pytest.mark.django_db
def test_food_factory():
    instance = FoodFactory()
    assert instance.pkid


@pytest.mark.django_db
def test_food_gallery_factory():
    instance = FoodGalleryFactory()
    assert instance.pkid


@pytest.mark.django_db
def test_review_rating_factory():
    instance = ReviewRatingFactory()
    assert instance.pkid
