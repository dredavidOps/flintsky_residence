from django.contrib import admin
from django.http import JsonResponse
from django.urls import path, include

urlpatterns = [
    path('', lambda request: JsonResponse({"message":"Flintsky Backend is running"})),
    path('', include('django_prometheus.urls')),
    path("admin/", admin.site.urls),
    path('api/', include('booking.urls')),
]
