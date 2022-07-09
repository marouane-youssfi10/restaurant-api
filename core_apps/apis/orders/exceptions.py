from rest_framework.exceptions import APIException


class CartItemIsEmpty(APIException):
    status_code = 400
    default_detail = "You must have one food in your cartitem at least"


class HaveMoreOrders(APIException):
    status_code = 400
    default_detail = "you have already order not completed"
