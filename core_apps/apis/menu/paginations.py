from rest_framework.pagination import PageNumberPagination


class ReviewRatingPagination(PageNumberPagination):
    page_size = 10


class FoodsPagination(PageNumberPagination):
    page_size = 10
