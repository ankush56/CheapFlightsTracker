import requests
from dotenv import load_dotenv
import os

load_dotenv()


class FlightCodeFinder:
    URL = "https://iata-and-icao-codes.p.rapidapi.com/airline"

    headers = {
        "X-RapidAPI-Key": os.environ.get('X-RapidAPI-Key'),
        "X-RapidAPI-Host": os.environ.get('X-RapidAPI-Host')
    }

    def __init__(self):
        pass

    def find_flight_code(self, parameters):
        response = requests.get(self.URL, parameters, headers=self.headers)
        response.raise_for_status()
        data = response.json()
        return data[0]['name']

