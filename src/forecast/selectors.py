from dataclasses import dataclass

from src.common.interfaces import ICityClient, ICoordinatesClient


@dataclass
class ForecastCityGetter:
    city: str
    coordinates: ICoordinatesClient
    cities: ICityClient

    def execute(self):
        cities = self.coordinates.execute()
        forecast_cities = self.cities(cities).execute()
        return forecast_cities
