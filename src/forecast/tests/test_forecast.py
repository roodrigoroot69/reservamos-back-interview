from unittest.mock import Mock, patch
from django.test import TestCase

from rest_framework.test import APIClient
from rest_framework import status
from src.forecast.tests.fixtures import CITY_FOUNDED, COORDINATES_CITY


class ForecastTestCase(TestCase):

    @patch('src.forecast.domain.use_cases.CoordinatesReservamosGetter.execute')
    @patch('src.forecast.domain.use_cases.CityOpenWeatherGetter.execute')
    def test_get_forecast_with_city_name(
        self,
        city_weather_mock,
        coordinates_mock,
    ):
        coordinates_mock.return_value = COORDINATES_CITY
        city_weather_mock.return_value = CITY_FOUNDED
        client = APIClient()
        city = 'monterrey'

        response = client.get(f'/destiny/?city={city}')
        result = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsNotNone(result)
        self.assertIsInstance(result['results'], list)
        self.assertEqual(result['results'][0]['city'], 'Monterrey')
        self.assertEqual(result['results'][0]['weather']['main'], 'Rain')

    @patch('src.forecast.domain.use_cases.CoordinatesReservamosGetter.execute')
    @patch('src.forecast.domain.use_cases.CityOpenWeatherGetter.execute')
    def test_get_forecast_with_partial_city_name(
        self,
        city_weather_mock,
        coordinates_mock,
    ):
        coordinates_mock.return_value = COORDINATES_CITY
        city_weather_mock.return_value = CITY_FOUNDED
        client = APIClient()
        city = 'mont'

        response = client.get(f'/destiny/?city={city}')
        result = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsNotNone(result)
        self.assertIsInstance(result['results'], list)
        self.assertEqual(result['results'][0]['city'], 'Monterrey')
        self.assertEqual(result['results'][0]['weather']['main'], 'Rain')

    @patch('src.forecast.domain.use_cases.requests.get')
    def test_city_does_not_found(self, city_weather_mock):
        city_weather_mock.return_value = Mock(status_code=200,
                                              json=lambda:
                                                  [])

        client = APIClient()
        city = 'yautepec'

        response = client.get(f'/destiny/?city={city}')
        result = response.json()

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertIsNotNone(
            result,
            {'message': 'The city: yautepec does not found!'},
        )
