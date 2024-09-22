from dataclasses import dataclass
from datetime import datetime, timezone


@dataclass
class WeatherDTO:

    @classmethod
    def from_api_response(cls, forecast_item, city):
        new_date = datetime.fromtimestamp(forecast_item['dt'], tz=timezone.utc)
        return {
            'date': str(new_date.strftime('%Y-%m-%d')),
            'temp_min': forecast_item['main']['temp_min'],
            'temp_max': forecast_item['main']['temp_max'],
            'city': city['city']['name'],
            'country': city['city']['country'],
            'id_city': city['city']['id'],
            'weather': {
                'main': forecast_item['weather'][0]['main'],
                'description': forecast_item['weather'][0]['description']
            }
        }
