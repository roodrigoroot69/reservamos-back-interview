import concurrent.futures
from typing import Dict, List

from django.template.defaultfilters import slugify

from src.common.exceptions import CityDoesNotFoundException, WrongCoordinatesException
from src.common.interfaces import ICoordinatesClient, ICityClient

import requests


RESERVAMOS_URL = 'https://search.reservamos.mx/api/v2'
OPEN_WEATHER_URL = 'https://api.openweathermap.org/data/2.5/forecast?'
API_KEY = '58c41ce5675e936a6a1eac43faf102cb'


class CoordinatesReservamosGetter(ICoordinatesClient):
    city: str

    def execute(self):
        response = requests.get(f'{RESERVAMOS_URL}/places?q={self.city}&to={slugify(self.city)}')

        response.raise_for_status()

        if not response:
            raise CityDoesNotFoundException(f'The city: {self.city} does not found!')
        return response.json()


class CityOpenWeatherGetter(ICityClient):
    cities: List[Dict]

    def execute(self):
        forecast_cities = []
        with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
            future_to_city = {executor.submit(self._process_city_forecast, city): city for city in self.cities}
            for future in concurrent.futures.as_completed(future_to_city):
                city = future_to_city[future]
                try:
                    forecast_city = city
                    forecast_cities.append(forecast_city)
                except Exception as exc:
                    print(f"generate an excepcion: {exc}")
        return forecast_cities

    def _get_forecast_city(self, city):
        url = f'{OPEN_WEATHER_URL}lat={city['lat']}&lon={city['lon']}&appid={API_KEY}'
        response = requests.get(url)
        if not response:
            raise WrongCoordinatesException('Latitude or Longitude are wrong!')
        return response.json()

    def _process_city_forecast(self, city):
        forecast = self._get_forecast_city(city)
        return forecast['list']
