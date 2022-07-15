from rest_framework.pagination import PageNumberPagination


class CustomersPagination(PageNumberPagination):
    page_size = 2
