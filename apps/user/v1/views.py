from rest_framework import serializers
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status as http_status
from django.shortcuts import redirect
from django.conf import settings
from urllib.parse import urlencode
import http.client
import json
import datetime
import requests

from apps.base.base_views import ModelBaseViewSet
from apps.base.exceptions import BadRequestExcpetion, PermissionDeniedExcpetion
from apps.user.exceptions import AuthenticationFailedException
from apps.user.models import User, UserCollection
from apps.user.utils import generate_random_username
from apps.base.utils import JWTUtils
from apps.base.permissions import TokenAuthentication, IsAuthenticated

class DummySerializer(serializers.Serializer):
    pass

class ProfileViewSet(ModelBaseViewSet):
    queryset = []
    permission_classes = [IsAuthenticated]
    serializer_class = DummySerializer
    authentication_classes = [TokenAuthentication]

    @action(methods=["GET"], detail=False)
    def view(self, request, *args, **kwargs):
        username = request.query_params.get("username", None)
        if username is None:
            return Response("Username is required in query params", 400)
        
        return Response({"username": request.user["username"], "email": request.user["email"], "fullName": request.user["fullName"]})
    
    @action(methods=["POST"], detail=False)
    def edit(self, request, *args, **kwargs):
        username = request.data.get("username", None)
        firstName = request.data.get("firstName", None)
        lastName = request.data.get("lastName", None)

        user = UserCollection.find_one({"_id": request.user["_id"]})
        if user is None:
            raise BadRequestExcpetion()
        
        if username is not None:
            user_with_new_username = UserCollection.find_one({"username": username})
            if user_with_new_username is not None:
                return Response(f"User already exists with the username ${username}")

        if firstName is None:
            firstName = user["firstName"]
        if lastName is None:
            lastName = user["lastName"]
        if username is None:
            username = user["username"]

        fullName = firstName + "-" + lastName

        new_values = {"$set": {"username": username, "lastName": lastName, "firstName": firstName, "fullName": fullName}}

        UserCollection.update_one({"_id": request.user["_id"]}, new_values)
        
        return Response({"username": username, "email": request.user["email"], "fullName": fullName})

class UserViewSet(ModelBaseViewSet):
    queryset = []
    permission_classes = []
    serializer_class = DummySerializer

    @action(methods=["POST"], detail=False)
    def register(self, request, *args, **kwargs):
        username = request.data.get("username", None)
        firstName = request.data.get("firstName", None)
        lastName = request.data.get("lastName", None)
        email = request.data.get("email", None)
        password = request.data.get("password", None)
        
        if email is None or password is None:
            return Response("An email and password is required", 400)

        if firstName is None or firstName is None:
            raise BadRequestExcpetion()
        
        if len(password) > 100 or len(email) > 100 or len(firstName) > 100 or len(lastName) > 100:
            return Response("Only 100 characters are allowed for a field", 400)

        if username is None:
            username = generate_random_username()

        user_with_username = UserCollection.find_one({"username":username})
        if user_with_username is not None:
            return Response("A user with that username already exists", 400)

        user_with_email = UserCollection.find_one({"email":email})
        if user_with_email is not None:
            return Response("A user with that email already exists", 400)
        
        
        if len(password) < 8:
            return Response("This password is too short. It must contain atleast 8 characters", 400)
        
        firebase_register_request = requests.post(f"https://identitytoolkit.googleapis.com/v1/accounts:signUp?key={settings.GOOGLE_API_KEY}", {"email": email, "password": password, "returnSecureToken": True})

        if firebase_register_request.status_code != 200:
            raise BadRequestExcpetion()

        registration_data = firebase_register_request.json()

        user = User(username, email, firstName, lastName, registration_data["localId"])

        if user.is_valid():
            user_doc = user.doc()
            user_id = UserCollection.insert_one(user_doc).inserted_id
            return Response({"username": user.username, "email": user.email})
        else:
            return Response("Something went wrong", 400)
        
    @action(methods=["GET", "POST"], detail=False)
    def login(self, request, *args, **kwargs):
        username = request.data.get("username", None)
        password = request.data.get("password", None)

        if username is None or password is None:
            raise BadRequestExcpetion()
        
        user = UserCollection.find_one({"username": username})
        if user is None:
            return Response(f"User with {username} not found")
        
        email = user["email"]

        firebase_login_request = requests.post(f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={settings.GOOGLE_API_KEY}", {"email": email, "password": password, "returnSecureToken": True})

        registration_data = firebase_login_request.json()

        if firebase_login_request.status_code != 200:
            raise BadRequestExcpetion()
        
        token = JWTUtils.create_token({"_id": str(user["_id"]), "username": user["username"],"email": user["email"],"firstName": user["firstName"],"lastName": user["lastName"],"fullName": user["fullName"], "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=36)})

        return Response({"email": email, "username": user["username"], "fullName": user["fullName"], "token": token})


        
