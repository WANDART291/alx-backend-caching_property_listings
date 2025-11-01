# properties/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Map the root of the properties app (which is /properties/) to the view
    path('', views.property_list, name='property_list'),
]