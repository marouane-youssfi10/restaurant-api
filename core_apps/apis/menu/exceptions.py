from rest_framework.exceptions import APIException


class ReviewUserDoesNotExists(APIException):
    status_code = 400
    default_detail = "the review of this user does not exist"


class AlreadyRated(APIException):
    status_code = 400
    default_detail = "You have already Rated this food"
