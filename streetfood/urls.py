from django.urls import path
from .views import FoodTruckList

urlpatterns = [
    path('api/foodtrucks', FoodTruckList.as_view(), name='foodtruck-list'),
]