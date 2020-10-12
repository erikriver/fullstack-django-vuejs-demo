from django.urls import path, include
from .views import PlaceViewSet, BookingViewSet, PlaceBookingViewSet

from rest_framework import routers

router = routers.DefaultRouter()
router.register('properties', PlaceViewSet, basename="properties")
router.register('bookings', BookingViewSet, basename="bookings")
router.register(r'properties/(?P<property_id>[0-9a-f-]+)/bookings',
                PlaceBookingViewSet, basename="properties-bookings")

urlpatterns = [
    path('api/', include(router.urls)),
]