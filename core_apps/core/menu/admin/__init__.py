from django.contrib import admin
from django.utils.html import format_html
from dal_admin_filters import AutocompleteFilter

from core_apps.core.menu.models import Category, Food, FoodGallery, ReviewRating
from core_apps.utils.admin import ReadOnlyWithDetailAdmin


class UserFilter(AutocompleteFilter):
    title = "By user name"
    field_name = "user"
    autocomplete_url = "user-autocomplete"
    is_placeholder_title = True


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
        "created_at",
        "updated_at",
    ]
    list_display_links = ["pkid", "food_name"]
    search_fields = ["food_name"]


class FoodGalleryAdmin(admin.ModelAdmin):
    def thumbnail(self, obj):
        if obj.food_images:
            return format_html('<img src="{}" width="150">'.format(obj.food_images.url))
        return "-"

    list_display = [
        "pkid",
        "food",
        "thumbnail",
        "created_at",
        "updated_at",
    ]
    list_display_links = ["pkid", "food"]
    thumbnail.short_description = "Food picture"


class ReviewRatingAdmin(ReadOnlyWithDetailAdmin):
    list_display = [
        "pkid",
        "user_name",
        "food_name",
        "review",
        "rating",
        "created_at",
        "updated_at",
    ]
    list_display_links = ["pkid"]
    search_fields = (UserFilter, "user__username", "user__email")

    def user_name(self, obj: ReviewRating):
        return format_html(
            '<a href="/admin/users/user/?q={}">{} {}</a>',
            obj.user.username,
            obj.user.first_name,
            obj.user.last_name,
        )

    def food_name(self, obj: ReviewRating):
        return format_html(
            '<a href="/admin/menu/food/{}/change">{}</a>',
            obj.food.pkid,
            obj.food.food_name,
        )


admin.site.register(Food, FoodAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(FoodGallery, FoodGalleryAdmin)
admin.site.register(ReviewRating, ReviewRatingAdmin)
