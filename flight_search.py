import os
import requests

# This class is responsible for talking to the Flight Search API.
URL = "https://api.tequila.kiwi.com/v2/search"

class FlightSearch:
    def __init__(self):
        self.flight_api_url = URL

    def search_flight_data(self, parameters, headers):
        response = requests.get(self.flight_api_url, parameters, headers=headers)
        response.raise_for_status()
        data = response.json()
        return data
