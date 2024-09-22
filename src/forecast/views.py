from typing import Dict
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from src.forecast.domain.use_cases import (
    CityOpenWeatherGetter,
    CoordinatesReservamosGetter
)
from src.forecast.selectors import ForecastCityGetter
from rest_framework.pagination import PageNumberPagination


class ForecastDestinyAPIView(APIView):

    def get(self, request):
        city = request.GET.get('city')
        if not city:
            return Response(
                {"error": "City parameter is required"},
                status=status.HTTP_400_BAD_REQUEST
            )
        coordinates_reservamos = CoordinatesReservamosGetter(
           city=request.GET['city'],
        )

        response = ForecastCityGetter(
            city=request.GET['city'],
            coordinates=coordinates_reservamos,
            cities_class=CityOpenWeatherGetter,
        ).execute()

        if isinstance(response, Dict):
            return Response(response, status=status.HTTP_404_NOT_FOUND)

        paginator = PageNumberPagination()
        paginator.page_size = 10
        paginated_response = paginator.paginate_queryset(response, request)

        return paginator.get_paginated_response(paginated_response)
