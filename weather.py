import requests

class Weather():
    
    def __init__(self, api_key):
        self.api_key = api_key
        self.url = "http://api.openweathermap.org/data/2.5/weather"

    def get_weather(self, city):

        '''
        Returns the weather of a city

        Args:
            city (str): The city to get the weather of.

        Returns:
            json: The weather data of the city.
        '''

        url = f"{self.url}?q={city}&appid={self.api_key}"
        response = requests.get(url)
        return response.json()
