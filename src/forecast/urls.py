from django.urls import path

from src.forecast.views import ForecastDestinyAPIView


urlpatterns = [
    path('destiny/', ForecastDestinyAPIView.as_view()),
]
