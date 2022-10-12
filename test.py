a1 = ['WS', 'AC']
flight_code_search_params = {
    "iata_code" : '',
}


for x in a1:
    flight_code_search_params["iata_code"] = x
    print(flight_code_search_params)
    flight_code_search_params["iata_code"] = ''


# for city in data['prices']:
#     flight_search_parameters['fly_to'] = city['iataCode']
#     # Check minimum price
#     response_data = flight_search.search_flight_data(flight_search_parameters, headers)
#     current_min_price = 0
#     counter = 0
#     flight_response_list = []
#     flight_data = None
#     airlines = []
#     flight_code_search_params = {
#         "iata_code": ""
#     }
#     for x in response_data['data']:
#         if counter == 0:
#             current_min_price = x['price']
#         if current_min_price > x['price']:
#             current_min_price = x['price']
#         counter = counter + 1
#         for items in x['airlines']:
#             flight_code_search_params["iata_code"] = items
#             print(flight_code_search_params)
#             airline_name = flight_code_finder.find_flight_code(flight_code_search_params)
#             airlines.append(airline_name)
#
#         flight_data = (x['cityTo'], current_min_price, {'Flights': airlines})
#     flight_response_list.append(flight_data)
#     print(f"{flight_response_list}")
#     flight_code_search_params["iata_code"] = ''