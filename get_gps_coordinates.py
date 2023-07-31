from typing import NamedTuple
from geopy.geocoders import Nominatim
from exceptions import CantGetCoordinates
from config import USE_ROUNDED_COORDINATES


class Coordinates(NamedTuple):
    longitude: float
    latitude: float

class _Location(NamedTuple):
    address: str
    latitude: float
    longitude: float
    
    
def get_coordinates() -> Coordinates:
    adress, latitude, longitude = _get_location_by_street_city_country()
    """Returns rounded coordinates"""
    if USE_ROUNDED_COORDINATES == True:
        latitude, longitude = map(lambda x: round(x, 2), [latitude, longitude])
        return Coordinates(longitude=longitude, latitude=latitude)

def _get_location_by_street_city_country() -> _Location:
    geolocator = Nominatim(user_agent='My App')
    location = geolocator.geocode({'street': 'Долгоозёрная', 'city': 'Санкт-Петербург', 'country': 'Россия'}, language='ru')
    if location is not None: 
        return _Location(address=location.address, latitude=location.latitude, longitude=location.longitude)
    else:
        raise CantGetCoordinates
        
