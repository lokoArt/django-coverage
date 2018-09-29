from rest_framework import serializers


class AirplaneSerializer(serializers.Serializer):
    id = serializers.IntegerField(min_value=1)
    passengers_number = serializers.IntegerField(min_value=0)


class FuelConsumptionInputSerializer(serializers.Serializer):
    airplanes = serializers.ListField(child=AirplaneSerializer(), min_length=10)


class FuelConsumptionOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    fuel_consumption = serializers.DecimalField(max_digits=18, decimal_places=3)
    maximum_duration = serializers.IntegerField()
