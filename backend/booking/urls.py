from django.urls import path
from .views import ApartmentList, BookingCreate

urlpatterns = [
    path('apartments/', ApartmentList.as_view(), name='apartment-list'),
    path('book/', BookingCreate.as_view(), name='booking-create'),
]