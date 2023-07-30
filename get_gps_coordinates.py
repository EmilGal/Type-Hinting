from typing import NamedTuple 
from geopy.geocoders import Nominatim
from exceptions import CantGetCoordinates
from config import USE_ROUNDED_COORDINATES


class Coordinates(NamedTuple):
    longitude: float
    latitude: float

class Location(NamedTuple):
    address: str
    latitude: float
    longitude: float
    

def get_coordinates() -> Coordinates:
    geolocator = Nominatim(user_agent='My App')
    location = geolocator.geocode({'street': 'Долгоозёрная', 'city': 'Санкт-Петербург', 'country': 'Россия'}, language='ru')
    if location is not None:
        """Returns selected coordinates"""
        if USE_ROUNDED_COORDINATES == True:
            longitude, latitude = map(lambda x: round(x,2), [location.longitude, location.latitude])
            return Coordinates(longitude=longitude, latitude=latitude) 
    else: 
        raise CantGetCoordinates  ## Создаём свой класс исключений в файле Exceptions.py

def _get_location_by_street_city_country() -> Location:
    geolocator = Nominatim(user_agent='My App')
    location = geolocator.geocode({'street': 'Долгоозёрная', 'city': 'Санкт-Петербург', 'country': 'Россия'}, language='ru')
    return Location(address=location.address, latitude=location.latitude, longitude=location.longitude)


print(_get_location_by_street_city_country().longitude, _get_location_by_street_city_country().latitude)