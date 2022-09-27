import requests


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    # Use sheety API

    def __init__(self, url):
        self.sheet_url = url

    def sheet_action(self, action_type, **kwargs):
        sheet_inputs = {}
        auth = ()
        data = None
        endpoint_url = None
        for key, value in kwargs.items():
            if key == 'json':
                sheet_inputs = value
            if key == 'auth':
                auth = value
            if key == 'endpoint':
                endpoint_url = self.sheet_url + "/" + str(value)
        if action_type == 'GET':
            # Get Sheet data
            response = requests.get(self.sheet_url)
            response.raise_for_status()
            data = response.json()
            return data
        elif action_type == 'POST':
            # Check if entry there already in spreadsheet
            response = requests.get(self.sheet_url)
            response.raise_for_status()
            data = response.json()
            dest_exist = False
            for x in data['prices']:
                if x['city'] == sheet_inputs['price']['city']:
                    print("Destination already there")
                    dest_exist = True

            if dest_exist == False:
                # Post sheet data
                sheet_response = requests.post(self.sheet_url, json=sheet_inputs, auth=auth)
                sheet_result = sheet_response.json()
                print(f"New destination added in google sheet{sheet_result}")
        elif action_type == 'PUT':
            print(f"endpoint url is {self.sheet_url}")
            sheet_response = requests.put(endpoint_url, json=sheet_inputs, auth=auth)
            sheet_result = sheet_response.json()
            print(f"Put request executed{sheet_result}")
            # Reset sheet url
            endpoint_url = self.sheet_url





