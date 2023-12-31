import os
from dotenv import load_dotenv
import pycountry
import requests

load_dotenv()
API_KEY = os.getenv('API_KEY')

class Weather:
    def __init__(self, city: str = 'Buenos Aires', units: str = 'Metric'):
        self.key = API_KEY
        self.city = city
        self.units = units
    
    #---- MAIN FUNCTIONS ----
    def req_info_api(self):
        # GEOCODING API
        call_link = f'http://api.openweathermap.org/geo/1.0/direct?q={self.city}&limit=&appid={self.key}'
        response = requests.get(call_link)
        if response.status_code != 200: raise Exception("Connection Error with Geocoding API")
        json = response.json()
        
        # Get full country name by its shortening
        country_shortening = json[0]['country']
        country_full_name = pycountry.countries.get(alpha_2 = country_shortening).name
        
        # CURRENT WEATHER API
        LAT, LON = json[0]['lat'], json[0]['lon']
        call_link = f'https://api.openweathermap.org/data/2.5/weather?lat={LAT}&lon={LON}&units={self.units}&appid={self.key}'
        response = requests.get(call_link)
        if response.status_code != 200: raise Exception("Connection Error with Current Weather API")
        json = response.json()
        
        temperature, condition = json['main']['temp'], json['weather'][0]['main']
        
        return country_full_name, temperature, condition
    
    # SETTERS
    def set_city(self, city: str): 
        self.city = city
    
    def get_weather_value(self):
        data = self.req_info_api()
        return {
            "city": self.city,
            "country": data[0],
            "temperature": f'{round(data[1])}°C',
            "condition": data[2]
        }

if __name__ == '__main__':
    weather = Weather()
    print(weather.get_weather_value())