from django.urls import include, path
from rest_framework import routers
from django.contrib import admin
from django.urls import path

router = routers.DefaultRouter()

urlpatterns = [
    path("admin/", admin.site.urls)
]

# apps urls
urlpatterns += [
    path("api/v1/", include(("apps.user.v1.urls", "user"), namespace="user"))
]
