class CityDoesNotFoundException(Exception):
    def __init__(self, message):
        super().__init__(message)

class WrongCoordinatesException(Exception):
    ...
