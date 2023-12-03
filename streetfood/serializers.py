from rest_framework import serializers
from .models import FoodTruck


class FoodTruckSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodTruck
        fields = (
            "applicant",
            "address",
            "fooditems",
            "latitude",
            "longitude",
            "locationid",
            "facility_type",
            "cnn",
            "location_description",
            "permit",
            "status",
            "dayshours",
            "approved",
            "expiration_date",
            "zip_codes",
            "neighborhoods_old",
        )
