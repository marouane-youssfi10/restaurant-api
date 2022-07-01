from rest_framework.exceptions import APIException


class OrdersNotFound(APIException):
    status_code = 404
    default_detail = "Orders not Found"


class OrderNumberDoesNotExist(APIException):
    status_code = 404
    default_detail = "This Order Does Not exists"
