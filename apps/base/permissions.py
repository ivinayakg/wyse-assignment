from rest_framework import permissions
from rest_framework.exceptions import AuthenticationFailed
from apps.base.utils import JWTUtils
from apps.user.models import UserCollection
from django.conf import settings
from rest_framework import authentication
import jwt

class TokenAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        # Get the Authorization header from the request
        auth_header = request.META.get("HTTP_AUTHORIZATION")

        if not auth_header:
            return (None, False)  # No Authorization header found

        token = auth_header

        try:
            user_info = JWTUtils.verify(token)
            if user_info is None:
                return (None, False)

            username = user_info["username"]
            if username is None:
                return (None, False)
            
            user = UserCollection.find_one({"username": username})
            if user is None:
                return (None, False)
            
            return (user, True)

        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed("Token has expired.")
        except jwt.DecodeError:
            raise AuthenticationFailed("Invalid token.")

class IsAuthenticated(permissions.BasePermission):
    def has_permission(self, request, view):
        # Check if the user is authenticated
        return request.user and request.user["_id"]