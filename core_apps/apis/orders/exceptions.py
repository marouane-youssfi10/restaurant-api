from rest_framework.exceptions import APIException


class CartItemEmpty(APIException):
    status_code = 400
    default_detail = "You must have one food in your cartitem at least"
