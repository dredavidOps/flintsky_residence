from rest_framework import generics
from .models import Apartment, Booking
from .serializers import ApartmentSerializer, BookingSerializer
from backend.metrics import bookings_created_total

class ApartmentList(generics.ListAPIView):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer

class BookingCreate(generics.CreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def perform_create(self, serializer):
        instance = serializer.save()
        bookings_created_total.inc()
        return instance

