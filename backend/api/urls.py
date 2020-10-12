from django.urls import path, include
from .views import PlaceViewSet

from rest_framework import routers

router = routers.DefaultRouter()
router.register('properties', PlaceViewSet, basename="properties")

urlpatterns = [
    path('api/', include(router.urls)),
]