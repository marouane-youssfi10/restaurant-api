from rest_framework.pagination import PageNumberPagination


class ReviewRatingPagination(PageNumberPagination):
    page_size = 10
