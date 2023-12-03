from rest_framework import views
from rest_framework.response import Response
from .models import FoodTruck
from .serializers import FoodTruckSerializer
from .utils import get_nearest_food_trucks

class FoodTruckList(views.APIView):
    """
    API view to list the nearest food trucks based on latitude and longitude.
    """
    
    def get(self, request):
        # Retrieve latitude and longitude from the request's query parameters.
        latitude = request.query_params.get('latitude')
        longitude = request.query_params.get('longitude')

        # Attempt to convert latitude and longitude to float values.
        # If conversion fails, return an error response.
        try:
            latitude = float(latitude)
            longitude = float(longitude)
        except (TypeError, ValueError):
            return Response({'error': 'Invalid latitude or longitude parameters'}, status=400)

        # Define the search radius (in kilometers).
        radius = 5

        # Retrieve all food trucks from the database and filter them by proximity
        # to the provided latitude and longitude, within the specified radius.
        nearby_trucks = [
            truck for truck in FoodTruck.objects.all()
            if get_nearest_food_trucks(longitude, latitude, truck.longitude, truck.latitude) <= radius
        ]

        # Sort the filtered food trucks by their distance from the provided location
        # and limit the results to the nearest 5 trucks.
        nearby_trucks = sorted(
            nearby_trucks,
            key=lambda t: get_nearest_food_trucks(longitude, latitude, t.longitude, t.latitude)
        )[:5]

        # Serialize the list of nearby food trucks to JSON.
        serializer = FoodTruckSerializer(nearby_trucks, many=True)

        # Return the serialized data in the response.
        return Response({'food_trucks': serializer.data})
