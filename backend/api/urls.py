from django.urls import path, include
from .views import PlaceViewSet, BookingViewSet

from rest_framework import routers

router = routers.DefaultRouter()
router.register('properties', PlaceViewSet, basename="properties")
router.register('bookings', BookingViewSet, basename="bookings")

urlpatterns = [
    path('api/', include(router.urls)),
]