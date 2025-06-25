from flight_search import FlightSearch
from data_manager import DataManager
from flight_data import FlightData
from notification_manager import NotificationManager
from pprint import pprint
#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

flight_search = FlightSearch()
sheet= DataManager()
notification = NotificationManager()

sheet_data = sheet.get_data()
pprint(sheet_data)

for i in sheet_data:
    if i["iataCode"] == "":
        # updated_sheet_data = flight_search.update_sheet(sheet_data)
        updated_sheet_data = sheet_data
        break
    else:
        updated_sheet_data = sheet_data

sheet.update_sheet(updated_sheet_data)
# pprint(sheet_data)
search_data = flight_search.search_flight(updated_sheet_data)
# pprint(search_data)

flight_data = FlightData(search_data)
flight_data.display_prices(updated_sheet_data)

cheap_prices = flight_data.find_cheapest_flight()

print(cheap_prices)

for city in updated_sheet_data:
    for flight in cheap_prices[city["city"]]:
        print(flight)
        notification.send_message(flight)