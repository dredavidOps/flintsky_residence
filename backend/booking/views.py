from rest_framework import generics
from .models import Apartment, Booking
from .serializers import ApartmentSerializer, BookingSerializer

class ApartmentList(generics.ListAPIView):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer

class BookingCreate(generics.CreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

