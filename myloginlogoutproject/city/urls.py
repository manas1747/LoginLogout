from django.contrib import admin
from django.urls import path, include

from .views import city_list, create_city

urlpatterns = [
    path('list', city_list, name="city_list"),
    path('create/', create_city, name="create_city"),
]
