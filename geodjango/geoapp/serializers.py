from rest_framework_gis.serializers import GeoFeatureModelSerializer
from rest_framework import serializers
from django.contrib.gis.geos import Point
from .models import Place

class PlaceSerializer(GeoFeatureModelSerializer):
    location = serializers.ListField(
        child=serializers.FloatField(), write_only=True
    )
    class Meta:
        model = Place
        geo_field = "location"
        fields = ("id", "name", "location")

    def create(self, validated_data):
        coordinates = validated_data.pop("location")
        validated_data["location"] = Point(coordinates[0], coordinates[1])
        return super().create(validated_data)

    def update(self, instance, validated_data):
        if "location" in validated_data:
            coordinates = validated_data.pop("location")
            instance.location = Point(coordinates[0], coordinates[1])
        return super().update(instance, validated_data)