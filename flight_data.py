import requests

LOCATION_URL = "https://api.tequila.kiwi.com/locations/query"


class FlightData:
    def __init__(self):
        self.location_url = LOCATION_URL

    # This class is responsible for structuring the flight data.
    def get_iata_code(self, location_parameters, headers):
        response = requests.get(LOCATION_URL, location_parameters, headers=headers)
        response.raise_for_status()
        data = response.json()
        return data['locations'][0]['code']
