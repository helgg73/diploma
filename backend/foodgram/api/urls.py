"""foodgram.api URL Configuration
"""
from django.urls import path, include
from djoser import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('users', views.UserViewSet, basename='users')

urlpatterns = [
    path('auth/', include('djoser.urls.authtoken')),
    path('', include(router.urls)),
]
