from rest_framework.exceptions import APIException
from rest_framework import status as httpStatus


class AuthenticationFailedException(APIException):
    status_code = 400
    default_detail = 'Authentication with google failed, try again later.'
    default_code = 'Authentication with google failed'


class BadRequestExcpetion(APIException):
    status_code = 400
    default_detail = 'Something went wrong, try again later.'
    default_code = 'Something went wrong'


class InvalidRequestDataExcpetion(APIException):
    status_code = 400
    default_detail = 'Invalid request data'
    default_code = 'Invalid request data'


class PermissionDeniedExcpetion(APIException):
    status_code = 400
    default_detail = 'You do not have permission for this'
    default_code = 'You do not have permission for this'


class OrganizationCodeMissingException(APIException):
    status_code = httpStatus.HTTP_400_BAD_REQUEST
    default_detail = 'Organization Code is required in query params.'
    default_code = 'Organization Code is missing'


class OrganizationCodeInvalidException(APIException):
    status_code = httpStatus.HTTP_400_BAD_REQUEST
    default_detail = 'Organization Code is invalid.'
    default_code = 'Organization Code is invalid'


class OrganizationSubscriptionException(APIException):
    status_code = httpStatus.HTTP_400_BAD_REQUEST
    default_detail = 'You are not a part of this organization.'
    default_code = 'You are not a part of this organization'
