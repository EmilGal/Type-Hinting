import requests
from typing import NamedTuple
from datetime import datetime
from get_gps_coordinates import Coordinates


Celcius = int

class Weather(NamedTuple):
    temperature: Celcius ## ввели алиас выше Celcius = int    
    feels_like: int
    wind_speed: float
    sunrise: datetime
    sunset: datetime

def get_weather(coordinates: Coordinates) -> Weather:
    return Weather(
        temperature=20,
        feels_like=19,
        wind_speed=4.2,
        sunrise=datetime.fromisoformat('2023-07-28 04:00:00'),
        sunset=datetime.fromisoformat('2023-07-28 22:00:00')
    )
    
print(get_weather())