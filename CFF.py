#Cheap, Financial Flights
from serpapi import GoogleSearch
import pandas as pd
import json
import os

class FlightSearch:
    def __init__(self, departure, arrival, min_price, max_price, outbound_date):
        if min_price<=0 or max_price<=0:
            raise ValueError("Prices must exceed 0")
        elif min_price>max_price:
            raise ValueError("Minimum price must be less than or equal to max price")
        self.departure=departure
        self.arrival=arrival
        self.min_price=min_price
        self.max_price=max_price
        self.outbound_date=outbound_date
        param = {
            "engine": "google_flights", "departure_id": self.departure, "arrival_id": self.arrival, "outbound_date": self.outbound_date, "currency": "USD", "hl": "en",
            "api_key": "2fa1e48f28a2949f47a62f717b2b70e051afb251b0abf77717c5c9462b155c7f", "sort_by":2, "max_price":self.max_price, "type": 2
        }
        search = GoogleSearch(param)
        self.convertToList(search)

    def convertToList(self, dictionary):
        temp=json.loads(dictionary)
        flightList=[]
        # for i in temp:

    def storeData(self, flightList):
        """
        Stores flight data in a CSV file using Pandas DataFrame.
        """
        df = pd.DataFrame(flightList, columns=['Airline', 'Price', 'Departure Time', 'Arrival Time'])
        df.to_csv('flights.csv', index=False)



if __name__ == "__main__":
    departure = input("Enter departure location: (i.e., JFK) ")
    arrival = input("Enter arrival location: (i.e., LAX) ")
    min_price = float(input("Enter minimum price: $"))
    max_price = float(input("Enter maximum price: $"))
    outbound_date = input("Enter outbound date (YYYY-MM-DD): ")

    flight_search = FlightSearch(departure, arrival, min_price, max_price, outbound_date)


            
            
#Potential use case for using Pandas `DataFrame` to store and analyze flight data, including prices, airlines, and departure times.