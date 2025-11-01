# alx_backend_caching_property_listings/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Route /properties/ to the properties application's urls.py
    path('properties/', include('properties.urls')),
]
