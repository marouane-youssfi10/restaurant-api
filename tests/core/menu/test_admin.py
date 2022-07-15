import pytest
from django.contrib.admin import AdminSite

from core_apps.core.menu.admin import (
    CategoryAdmin,
    FoodAdmin,
    FoodGalleryAdmin,
    ReviewRatingAdmin,
)
from core_apps.core.menu.models import Category, Food, FoodGallery, ReviewRating
from tests.conftest import CustomRequest
from tests.core.menu.factories import (
    CategoryFactory,
    FoodFactory,
    FoodGalleryFactory,
    ReviewRatingFactory,
)
from tests.core.users.factories import UserFactory


@pytest.mark.django_db
def test_category_admin__save_model(client):
    user = UserFactory(superuser=True)
    category = CategoryFactory.create()
    category_admin = CategoryAdmin(model=Category, admin_site=AdminSite())
    category_admin.save_model(obj=category, request=None, form=None, change=None)
    assert category_admin.has_add_permission(CustomRequest(user)) == True
    assert category_admin.has_change_permission(CustomRequest(user)) == True
    assert category_admin.has_delete_permission(CustomRequest(user)) == True


@pytest.mark.django_db
def test_food_admin__save_model(client):
    user = UserFactory(superuser=True)
    food = FoodFactory.create()
    food_admin = FoodAdmin(model=Food, admin_site=AdminSite())
    food_admin.save_model(obj=food, request=None, form=None, change=None)
    assert food_admin.has_add_permission(CustomRequest(user)) == True
    assert food_admin.has_change_permission(CustomRequest(user)) == True
    assert food_admin.has_delete_permission(CustomRequest(user)) == True


@pytest.mark.django_db
def test_food_gallery_admin__save_model(client):
    user = UserFactory(superuser=True)
    food_gallery = FoodGalleryFactory.create()
    food_gallery_admin = FoodGalleryAdmin(model=FoodGallery, admin_site=AdminSite())
    food_gallery_admin.save_model(
        obj=food_gallery, request=None, form=None, change=None
    )
    assert food_gallery_admin.has_add_permission(CustomRequest(user)) == True
    assert food_gallery_admin.has_change_permission(CustomRequest(user)) == True
    assert food_gallery_admin.has_delete_permission(CustomRequest(user)) == True


@pytest.mark.django_db
def test_review_rating_admin__save_model(client):
    user = UserFactory(superuser=True)
    review_rating = ReviewRatingFactory(user=user)
    review_rating_admin = ReviewRatingAdmin(model=ReviewRating, admin_site=AdminSite())
    review_rating_admin.save_model(
        obj=review_rating, request=None, form=None, change=None
    )
    assert review_rating_admin.has_add_permission(CustomRequest(user)) == False
    assert review_rating_admin.has_change_permission(CustomRequest(user)) == False
    assert review_rating_admin.has_delete_permission(CustomRequest(user)) == False
