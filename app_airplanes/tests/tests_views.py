# Create your tests here.
import json
import os

from rest_framework import status
from rest_framework.test import APIClient, APITestCase


class TestApi(APITestCase):
    valid_input: list = []

    def test_estimate_fuel_consumption_no_data(self) -> None:
        invalid_payoad_1 = [{}]
        response = APIClient().post('/airplanes/estimate-fuel-consumption/', invalid_payoad_1, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_estimate_fuel_consumption_not_enough_data(self) -> None:
        invalid_payload_2 = [{'id': 5,
                              'fuel_tank': 200,
                              'passengers_number': 100}]
        response = APIClient().post('/airplanes/estimate-fuel-consumption/', invalid_payload_2, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_estimate_fuel_consumption_with_negative_id(self) -> None:
        api_client = APIClient()
        dir_path = os.path.dirname(os.path.realpath(__file__))

        with open('{}/resources/airplane_payload_1.json'.format(dir_path), encoding='utf-8') as data_file:
            data = json.loads(data_file.read())
            data['airplanes'][0]['id'] = -1
            response = api_client.post('/airplanes/estimate-fuel-consumption/', data, format='json')
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_estimate_fuel_consumption_with_negative_passengers(self) -> None:
        api_client = APIClient()
        dir_path = os.path.dirname(os.path.realpath(__file__))

        with open('{}/resources/airplane_payload_1.json'.format(dir_path), encoding='utf-8') as data_file:
            data = json.loads(data_file.read())
            data['airplanes'][0]['passengers_number'] = -1
            response = api_client.post('/airplanes/estimate-fuel-consumption/', data, format='json')
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_estimate_fuel_consumption(self) -> None:
        api_client = APIClient()
        dir_path = os.path.dirname(os.path.realpath(__file__))

        with open('{}/resources/airplane_payload_1.json'.format(dir_path), encoding='utf-8') as data_file:
            data = json.loads(data_file.read())

            response = api_client.post('/airplanes/estimate-fuel-consumption/', data, format='json')
            self.__validate_response(response, '{}/resources/airplane_payload_1_expected.json'.format(dir_path))

    def __validate_response(self, response, resource):
        with open(resource, encoding='utf-8') as data_file:
            expected_response = json.loads(data_file.read())
            actual_response = list(dict(d) for d in response.data)
            self.assertTrue(expected_response == actual_response, 'Received unexpected response')
