from rest_framework.exceptions import APIException


class OrderNumberDoesNotExist(APIException):
    status_code = 404
    default_detail = "This Order Does Not exists"
