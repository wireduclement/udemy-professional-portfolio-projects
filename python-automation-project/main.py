import requests
import datetime
from dotenv import load_dotenv
import os


class WeatherChecker:
    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv('API_KEY')
        self.base_url = "https://api.openweathermap.org/data/2.5/weather"

    def get_weather(self, city):
        request_url = f"{self.base_url}?appid={self.api_key}&q={city}"
        response = requests.get(request_url)
        if response.status_code == 200:
            return response.json()
        else:
            return None
        
    def display_weather(self, city):
        data = self.get_weather(city)
        if data:
            weather = data["weather"][0]["description"]
            temperature = round(data["main"]["temp"])
            sunrise = datetime.datetime.utcfromtimestamp(data["sys"]["sunrise"] + data["timezone"])
            sunset = datetime.datetime.utcfromtimestamp(data["sys"]["sunset"] + data["timezone"])
            country = data["sys"]["country"]
            print(f"Weather summary: {weather}")
            print(f"Temperture: {temperature}°C")
            print(f"Sunrise: {sunrise}")
            print(f"Sunset: {sunset}")
            print(f"Location: {city}, {country}")
        else:
            print(":)Oops, something's not right...")


def main():
    city = input("Welcome! here's an automated program to check the weather, enter city: ").title()
    weather_checker = WeatherChecker()
    weather_checker.display_weather(city)

if __name__ == "__main__":
    main()
