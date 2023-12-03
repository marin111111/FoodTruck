from rest_framework import views
from rest_framework.response import Response
from .models import FoodTruck
from .serializers import FoodTruckSerializer
from .utils import get_nearest_food_trucks

class FoodTruckList(views.APIView):
    def get(self, request):
        latitude = request.query_params.get('latitude')
        longitude = request.query_params.get('longitude')

        try:
            latitude = float(latitude)
            longitude = float(longitude)
        except (TypeError, ValueError):
            return Response({'error': 'Invalid latitude or longitude parameters'}, status=400)

        radius = 5

        nearby_trucks = [
            truck for truck in FoodTruck.objects.all()
            if get_nearest_food_trucks(longitude, latitude, truck.longitude, truck.latitude) <= radius
        ]

        nearby_trucks = sorted(
            nearby_trucks,
            key=lambda t: get_nearest_food_trucks(longitude, latitude, t.longitude, t.latitude)
        )[:5]

        serializer = FoodTruckSerializer(nearby_trucks, many=True)

        return Response({'food_trucks': serializer.data})