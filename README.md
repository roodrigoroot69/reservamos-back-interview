# Tecnical Interview for Reservamos

## Challenge description:

`In Reservamos we're always looking for ways to help our users have the best
experience when looking for travel options so that they can make the best decision
when reserving a bus or flight ticket. To accomplish this, we have to make a REST API
which can be consumed by a client app to check the weather forecast for the
destinations available in Reservamos. The API's functionality is to be able to compare
the weather forecast for the next 7 days, by day, of different destinations offered by
Reservamos. The client app must be able to send the name of a city and fetch the
maximum and minimum temperature for these places.
For this challenge you will be using OpenWeather's API to look up the temperature
using geographic coordinates, and show the results in metric units.`

## Objective:

An endpoint that return a list of all cities that match the given param including the maximum and
minimum temperature for the next 7 days (include only cities into results)
**Note:** Curently Open Weather Map does not longer offers data of the next 7 days, only offers for 5 days in a Free plan


## Stack
- Django
- Django Rest Framework
- Docker
- Docker Compose


## Instructions for Run Project

Note: For this project **Docker** is Required

#### To Run Project
```docker compose up --build -d	```

#### To Run Project With Logs
```docker compose up --build```

#### To Stop Project
```docker compose stop```

**Note:** For this project i preferred don't use a .env for save environment variables, because is for a tecnical interview,
in a real project i will use a .env file or maybe other service like SSM or AppConfig to save and get environment variables
for the project.

## Consume Endpoint


### Get All Cities that match the given param

Get All Cities that match the given param

**URL** : `http://localhost:8000/destiny/?city=acapulco`

**Method** : `GET`

**Auth required** : NO

**Data constraints**


## Success Response

**Code** : `200 OK`

**Content example**

```json

{
    "count": 6,
    "next": null,
    "previous": null,
    "results": [
        {
            "date": "2024-09-22",
            "temp_min": 15.66,
            "temp_max": 16.79,
            "city": "Polanco",
            "country": "MX",
            "id_city": 3521305,
            "weather": {
                "main": "Rain",
                "description": "light rain"
            }
        },
        {
            "date": "2024-09-23",
            "temp_min": 21.44,
            "temp_max": 21.44,
            "city": "Polanco",
            "country": "MX",
            "id_city": 3521305,
            "weather": {
                "main": "Clouds",
                "description": "scattered clouds"
            }
        },
        {
            "date": "2024-09-24",
            "temp_min": 21.61,
            "temp_max": 21.61,
            "city": "Polanco",
            "country": "MX",
            "id_city": 3521305,
            "weather": {
                "main": "Clouds",
                "description": "scattered clouds"
            }
        },
        {
            "date": "2024-09-25",
            "temp_min": 21.29,
            "temp_max": 21.29,
            "city": "Polanco",
            "country": "MX",
            "id_city": 3521305,
            "weather": {
                "main": "Clouds",
                "description": "broken clouds"
            }
        },
        {
            "date": "2024-09-26",
            "temp_min": 20.29,
            "temp_max": 20.29,
            "city": "Polanco",
            "country": "MX",
            "id_city": 3521305,
            "weather": {
                "main": "Clouds",
                "description": "broken clouds"
            }
        },
        {
            "date": "2024-09-27",
            "temp_min": 18.34,
            "temp_max": 18.34,
            "city": "Polanco",
            "country": "MX",
            "id_city": 3521305,
            "weather": {
                "main": "Clouds",
                "description": "overcast clouds"
            }
        }
    ]
}
```
## Not Found Response

**Code** : `404 NOT FOUND`
The citye entered does not found

**Content example**

```json
{
    "message": "The city: yautepec does not found!"
}

```

## Tests
I'm using unittest(From Python) and TestCase(Django) for tests.
Maybe this could cause confusion because only have tests in app for the service Forecast

Taking as reference the book "Architecture Pattern with Python" the tests for domain should live in service layer why?
Because we don't use the Bussines Rules outside Service (for this case ForecastCityGetter), if we create more tests for live in domain we could be a lot of test repeated and unncesaries.

For this reazon all test are for ForecastCityGetter class, because only in this point i call other class or function (Bussines Rules)

If we modify the Domain (Bussines Rules) also service can be failed, because the App module(Forecast) or proccess depende of the Domain.

#### Run Test

```docker compose run back python manage.py test```

