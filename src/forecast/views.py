from rest_framework.views import APIView
from rest_framework.response import Response
from src.forecast.domain.use_cases import CityOpenWeatherGetter, CoordinatesReservamosGetter
from src.forecast.selectors import ForecastCityGetter


class ForecastDestinyAPIView(APIView):

    def get(self, request, *args, **kwargs):
        print(request.GET)
        print("####33")
        coordinates_reservamos = CoordinatesReservamosGetter(
           city=request.GET['city']
        )

        response = ForecastCityGetter(
            city=request.GET['city'],
            coordinates=coordinates_reservamos,
            cities=CityOpenWeatherGetter
        ).execute()
        return Response(response)
