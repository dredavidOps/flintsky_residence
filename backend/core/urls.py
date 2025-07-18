from django.contrib import admin
from django_prometheus import exports
from django.urls import path, include
from django.http import JsonResponse

urlpatterns = [
    path('', lambda request: JsonResponse({"message":"Flintsky Backend is running"})),
    path('metrics/', exports.ExportToDjangoView),
    path("admin/", admin.site.urls),
    path('api/', include('booking.urls')),
]