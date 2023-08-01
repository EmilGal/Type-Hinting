import urllib.request
from typing import NamedTuple
from datetime import datetime
from exceptions import *
from get_gps_coordinates import Coordinates
import config


Celcius = int

class Weather(NamedTuple):
    temperature: Celcius ## ввели алиас выше Celcius = int    
    feels_like: int
    wind_speed: float
    sunrise: datetime
    sunset: datetime

def get_weather(coordinates: Coordinates) -> Weather:
    ninja_response = _get_ninja_api_response(longitude=coordinates.longitude, latitude=coordinates.latitude) 
    weather = _parse_ninja_response(ninja_response)
    return weather

    
def _get_ninja_api_response(latitude: float = 30.02, longitude: float = 60.01) -> str:
    headers = {'X-Api-Key': 'CGdF1pnHbl+maAeXF/poHg==dwCogwvp4W5zGxAV'} 
    url = config.API_NINJAS_URL.format(latitude=latitude, longitude=longitude)
    try:
        request = urllib.request.Request(url, headers=headers)
        response = urllib.request.urlopen(request)
        result = response.read()
        if result is not None:
            return result
        else:
            raise API_response_error
    except urllib.error.URLError:     
        raise API_error

# def _decode_from_bytes(response: bytes) -> str:
#     return bytes.decode('utf-8')


# def _parse_ninja_response(ninja_response: str) -> Weather:
#     try: 
#         ninja_dict = {}
    

if __name__ == '__main__':
    print(_get_ninja_api_response())
    