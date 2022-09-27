# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.


import requests
import os
from twilio.rest import Client
from dotenv import load_dotenv
from data_manager import DataManager

load_dotenv()

SHEET_URL = "https://api.sheety.co/fba4dfbb939ba81e50bb949091994b8f/flightDeals/prices"
SHEET_USERNAME = os.environ.get('SHEET_USERNAME')
SHEET_PASSWORD = os.environ.get('SHEET_PASSWORD')
auth = (SHEET_USERNAME, SHEET_PASSWORD)

sheet1 = DataManager(SHEET_URL)
# Get sheet data
#


sheet_input = {
    'price': {
        'city': "Test",
        'iataCode': 1234,
        'lowestPrice': 12
    }
}
# Add destination to sheet data
# Check if entry there if not there then only add
data = sheet1.sheet_action('GET')
print(f"data is {data}")
print(f"sheet input is {sheet_input['price']['city']}")

sheet1.sheet_action('POST', json=sheet_input, auth=auth )
#
### url = "https://api.tequila.kiwi.com/v2/search"
#
##API_KEY = os.environ.get('API_KEY') parameters = {
#     'fly_from':'YYZ',
#     'fly_to': 'YVR',
#     'dateFrom': '01/11/2022',
#     'dateTo': '04/11/2022',
#     'curr': 'CAD'
# }
#
# headers = {
#     "apikey": API_KEY,
#     "Content-Type": "application/json"
# }
#
# response = requests.get(url, parameters, headers=headers)
# response.raise_for_status()
# data = response.json()
# print(data)
