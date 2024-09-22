from dataclasses import dataclass, field
from typing import List, Type

from src.common.exceptions import CityDoesNotFoundException
from src.common.interfaces import ICityClient, ICoordinatesClient
from src.forecast.domain.weather_dto import WeatherDTO


@dataclass
class ForecastCityGetter:
    city: str
    coordinates: ICoordinatesClient
    cities_class: Type[ICityClient]
    cities: List = field(default_factory=list)

    def execute(self):
        try:
            coordinates_cities = self.coordinates.execute()
        except CityDoesNotFoundException as cdnfe:
            return {'message': str(cdnfe)}

        city_openweather_getter = self.cities_class(
            coordinates_cities=coordinates_cities
        )
        forecast_cities = city_openweather_getter.execute()

        self._transform_forecast_dto(forecast_cities)

        unique_cities = {}
        self._delete_extras_forecasts(unique_cities)

        filtered_cities_list = list(unique_cities.values())

        return filtered_cities_list

    def _delete_extras_forecasts(self, unique_cities) -> None:
        for city in self.cities:
            key = (city['date'], city['id_city'])
            if key not in unique_cities:
                unique_cities[key] = city

    def _transform_forecast_dto(self, forecast_cities) -> None:
        for forecast in forecast_cities:
            for fori in forecast['list']:
                data = WeatherDTO.from_api_response(fori, forecast)
                self.cities.append(data)
