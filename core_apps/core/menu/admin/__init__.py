from django.contrib import admin
from django.utils.html import format_html

from core_apps.core.menu.models import Category, Food, FoodGallery, ReviewRating


class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        "pkid",
        "category_name",
        "slug",
    ]
    list_display_links = ["pkid", "category_name"]


class FoodAdmin(admin.ModelAdmin):
    list_display = [
        "pkid",
        "food_name",
        "slug",
        "price",
        "category",
    ]
    list_display_links = ["pkid", "food_name"]
    search_fields = ["food_name"]


class FoodGalleryAdmin(admin.ModelAdmin):
    def thumbnail(self, obj):
        return format_html('<img src="{}" width="150">'.format(obj.food_images.url))

    list_display = [
        "pkid",
        "food",
        "thumbnail",
    ]
    list_display_links = ["pkid", "food"]


class ReviewRatingAdmin(admin.ModelAdmin):
    list_display = [
        "pkid",
        "user",
        "food",
        "review",
        "rating",
    ]
    list_display_links = ["pkid", "user"]
    search_fields = ["user"]


admin.site.register(Food, FoodAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(FoodGallery, FoodGalleryAdmin)
admin.site.register(ReviewRating, ReviewRatingAdmin)
