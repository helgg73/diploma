"""foodgram.api URL Configuration
"""
from django.urls import path, include
from djoser import views as djoser_views
from rest_framework import routers

from api.views import TagsViewSet

router = routers.DefaultRouter()
router.register('users', djoser_views.UserViewSet, basename='users')
router.register('tags', TagsViewSet, basename='tags')

urlpatterns = [
    path('auth/', include('djoser.urls.authtoken')),
    path('', include(router.urls)),
]
