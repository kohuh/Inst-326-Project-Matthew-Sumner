#Cheap, Financial Flights
from re import search

from serpapi import GoogleSearch
import pandas as pd
import json
import os

class FlightSearch:
    def __init__(self, departure, arrival, min_price, max_price, outbound_date):
        self.departure=departure
        self.arrival=arrival
        self.min_price=min_price
        self.max_price=max_price
        self.outbound_date=outbound_date
        self.api_key = os.getenv("api_key")
        param = {
            "engine": "google_flights", "departure_id": self.departure, "arrival_id": self.arrival, "outbound_date": self.outbound_date, "currency": "USD", "hl": "en",
            "api_key": self.api_key, "sort_by":2, "max_price":self.max_price, "type": 2
        }
        search = GoogleSearch(param)
        self.convertToList(search)
    
    def sortByPrice(self):
        if self.min_price<=0 or self.max_price<=0:
            raise ValueError("Prices must exceed 0")
        elif self.min_price>self.max_price:
            raise ValueError("Minimum price must be less than or equal to max price")
        

    def convertToList(self, dictionary):
        flight_list=[]
        flights=dictionary.get_dict().get("flights", [])
        for flight in flights:
            # Extract relevant flight information
            airline = flight.get("airline", "N/A")
            #... (Extract other relevant flight information such as price, departure time, etc.)




    def storeData(self, flightList):
        """
        Stores flight data in a CSV file using Pandas DataFrame.
        """
        df = pd.DataFrame(flightList, columns=['Airline', 'Price', 'Departure Time', 'Arrival Time'])
        df.to_csv('flights.csv', index=False)
        print(df)

    

if __name__ == "__main__":
    departure = input("Enter departure location: (i.e., JFK) ")
    arrival = input("Enter arrival location: (i.e., LAX) ")
    min_price = float(input("Enter minimum price: $"))
    max_price = float(input("Enter maximum price: $"))
    outbound_date = input("Enter outbound date (YYYY-MM-DD): ")

    flight_search = FlightSearch(departure, arrival, min_price, max_price, outbound_date)
