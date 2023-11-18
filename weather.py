import requests

class Weather():
    
    def __init__(self, api_key):
        self.api_key = api_key
        self.url = "http://api.openweathermap.org/data/2.5/weather"

    def get_weather(self, city):
        url = f"{self.url}?q={city}&appid={self.api_key}"
        response = requests.get(url)
        return response.json() 
