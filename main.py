# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.


import requests
import os
from twilio.rest import Client
from dotenv import load_dotenv
from data_manager import DataManager
from pprint import pprint
from flight_data import FlightData
from flight_search import FlightSearch

load_dotenv()

SHEET_URL = "https://api.sheety.co/fba4dfbb939ba81e50bb949091994b8f/flightDeals/prices"
SHEET_USERNAME = os.environ.get('SHEET_USERNAME')
SHEET_PASSWORD = os.environ.get('SHEET_PASSWORD')
auth = (SHEET_USERNAME, SHEET_PASSWORD)


sheet1 = DataManager(SHEET_URL)
#flight_search = DataManager(url)
flight_data = FlightData()
flight_search = FlightSearch()

URL = "https://api.tequila.kiwi.com/v2/search"
API_KEY = os.environ.get('API_KEY')

headers = {
    "apikey": API_KEY,
    "Content-Type": "application/json"
}



sheet_input = {
    'price': {
        'city': "Test",
        'iataCode': 1234,
        'lowestPrice': 12
    }
}


# Add destination to sheet data
# Check if entry there if not there then only add
# data = sheet1.sheet_action('GET')
# print(f"data is {data}")
# print(f"sheet input is {sheet_input['price']['city']}")
#
# sheet1.sheet_action('POST', json=sheet_input, auth=auth)

#Update all IATA code to testing
# data = sheet1.sheet_action('GET')
# for x in data['prices']:
#     print(f"id is {x['id']}")
#     sheet1.sheet_action('PUT', json=new_data, auth=auth, endpoint=x['id'])



location_parameters = {
    'term': '',
}

new_data = {
    'price': {
        'iataCode': 1234,
    }
}

# Get all locations in sheet
data = sheet1.sheet_action('GET')

#Loop through each destination check if IATA code is there
#If IATA code is missing add them from flight data API
for x in data['prices']:
    if x['iataCode'] == '':
        location_parameters['term'] = x['city']
        code = flight_data.get_iata_code(location_parameters, headers)
        new_data['price']['iataCode'] = code
        sheet1.sheet_action('PUT', json=new_data, auth=auth, endpoint=x['id'])
        # Reset params
        location_parameters['term'] = ''
        new_data['price']['iataCode'] = 1234
        print("All Destinations Flight Data IATA codes are updated")


# Get Flights Data
flight_search_parameters = {
    'fly_from':'YYZ',
    'fly_to': 'YVR',
    'dateFrom': '01/11/2022',
    'dateTo': '04/11/2022',
    'curr': 'CAD'
}


for city in data['prices']:
    flight_search_parameters['fly_to'] = city['iataCode']
    # Check minimum price
    response_data = flight_search.search_flight_data(flight_search_parameters, headers)
    current_min_price = None
    counter = 0
    flight_response_list = {}
    destination_city = None
    for x in response_data['data']:
        if counter == 0:
            current_min_price = x['price']
        if current_min_price > x['price']:
            current_min_price = x['price']
        counter = counter + 1
        destination_city = x['cityTo']

    flight_response_list[destination_city] = current_min_price
    print(f"{flight_response_list}")
###########




