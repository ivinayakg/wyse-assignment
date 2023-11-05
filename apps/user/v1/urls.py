from django.urls import include, path
from rest_framework import routers
from django.urls import path
from apps.user.v1.views import UserViewSet, ProfileViewSet

router = routers.DefaultRouter()
router.register(r'accounts', UserViewSet, basename="user_v1")
router.register(r'accounts/profile', ProfileViewSet, basename="profile_v1")

urlpatterns = [
    path("", include(router.urls)),
]
