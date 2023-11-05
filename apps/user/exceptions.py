from rest_framework.exceptions import APIException


class AuthenticationFailedException(APIException):
    status_code = 400
    default_detail = 'Authentication with google failed, try again later.'
    default_code = 'Authentication with google failed'


class AlreadyMemberOrganizationException(APIException):
    status_code = 400
    default_detail = 'You are already a member of this organization'
    default_code = 'Already a Member'
