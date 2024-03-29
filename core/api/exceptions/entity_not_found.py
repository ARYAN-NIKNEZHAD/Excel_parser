from rest_framework import status
from rest_framework.exceptions import APIException
from django.utils.encoding import force_str


class EntityNotFoundError(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = 'Entity not found!'

    def __init__(self, detail, field, status_code):
        if status_code is not None:self.status_code = status_code
        if detail is not None:
            self.detail = {field: {"Error": force_str(detail)}}
        else: self.detail = {'detail': force_str(self.default_detail)}
