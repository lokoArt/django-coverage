# Create your views here.
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.generics import GenericAPIView
from rest_framework.request import Request
from rest_framework.response import Response

from app_airplanes import services
from app_airplanes.serializers import FuelConsumptionOutputSerializer, FuelConsumptionInputSerializer


class EstimateFuelConsumptionView(GenericAPIView):
    """
    post:
       Estimates fuel consumption by airplane
    """

    serializer_class = FuelConsumptionInputSerializer
    output_serializer = FuelConsumptionOutputSerializer

    def post(self, request: Request) -> Response:
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        result = services.estimate_consumption_for_airplanes(serializer.validated_data['airplanes'])

        output_serializer = self.output_serializer(result, many=True)
        return Response(output_serializer.data, status=status.HTTP_200_OK)
