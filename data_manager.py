import requests
from config import SHEETY_AUTH, SHEETY_USERS_ENDPOINT, SHEETY_PRICES_ENDPOINT
SHEETY_AUTH = SHEETY_AUTH
SHEETY_PRICES_ENDPOINT = SHEETY_PRICES_ENDPOINT
SHEETY_USERS_ENDPOINT = SHEETY_USERS_ENDPOINT

SHEETY_HEADERS = {
    "Authorization": SHEETY_AUTH,
    "Content-Type": "application/json"
}


class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers=SHEETY_HEADERS)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data,
                headers=SHEETY_HEADERS
            )
            print(response.text)

    def update_prices(self, lowestprice, destination):
        for city in self.destination_data:
            if city["iataCode"] == destination:
                new_data = {
                    "price": {
                        "lowestPrice": lowestprice
                    }
                }
                response = requests.put(
                    url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                    json=new_data,
                    headers=SHEETY_HEADERS
                )

    def get_customer_emails(self):
        customers_endpoint = SHEETY_USERS_ENDPOINT
        response = requests.get(url=customers_endpoint, headers=SHEETY_HEADERS)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data
