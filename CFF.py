#Cheap, Financial Flights
import serpapi 
import pandas as pd
import json
import os

class FlightSearch:
    def __init__(self, departure, arrival, outbound_date):
        self.departure=departure
        self.arrival=arrival
        self.outbound_date=outbound_date
        #self.api_key = os.getenv("api_key")
        self.api_key = "3d39eb189e17e631e1448aaa9fe368fc52344f30a2a3ad937f26f066ceec1b52"
        param = {
            "engine": "google_flights", "departure_id": self.departure, "arrival_id": self.arrival, "outbound_date": self.outbound_date, "currency": "USD", "hl": "en",
            "sort_by":2, "type": 2
        }
        client = serpapi.Client(api_key=self.api_key)
        search = client.search(param)
        all_itineraries = search.get("best_flights", []) + search.get("other_flights", [])
        self.flightList=self.createList(all_itineraries) #creates list of flight objects

    def sortByPrice(self):
        return sorted(self.flightList)
    def setPriceRange(self, max_price, min_price=0):
        priced_list=[]
        if min_price<=0 or max_price<=0:
            raise ValueError("Prices must exceed 0")
        elif min_price>max_price:
            raise ValueError("Minimum price must be less than or equal to max price")
        else:
            for flight in self.flightList:
                if flight.price>min_price and flight.price<max_price:
                    priced_list.append(flight)
        return priced_list
    
    def printList(self):
        for i in self.flightList:
            print(i) 
            print("\n")

    def createList(self, input):
        flight_list=[]
        for t in input:
            first_leg=t["flights"][0]
            last_leg=t["flights"][-1]
            has_layover = len(t.get("layovers", [])) > 0
            flight_list.append(Flight(first_leg["flight_number"], first_leg["airline"], t["price"], first_leg["departure_airport"]["time"], last_leg["arrival_airport"]["time"], duration=t["total_duration"], layover=has_layover))
        return flight_list

class Flight():
    def __init__(self, flight_number, airline, price, departure_time, arrival_time, duration=0, layover=False,):
        self.flight_number=flight_number
        self.airline=airline 
        self.price=price 
        self.departure_time=departure_time
        self.arrival_time=arrival_time
        self.duration=duration
        self.layover=layover
    def __lt__(self, other):
        if isinstance(other, Flight):
            if other.price>=self.price:
                return True
            else:
                return False
        else:
            raise ValueError("Object Other is not Instance of Flight object")
    def __eq__(self, other):
        if isinstance(other, Flight):
            if other.price==self.price:
                return True
            else:
                return False
        else:
            raise ValueError("Object Other is not Instance of Flight object")
    def __str__(self):
        return f"airline flight number {self.flight_number} on {self.airline}, for {self.price}, leaving at {self.departure_time}, and arriving at {self.arrival_time}, for a total of {self.duration}"
    def __repr__(self):
        return f"({self.flight_number}, {self.airline}, {self.price}, {self.departure_time}, {self.arrival_time}, {self.duration}, {self.layover}"
if __name__ == "__main__":
    #departure = input("Enter departure location: (i.e., JFK) ")
    #arrival = input("Enter arrival location: (i.e., LAX) ")
    #outbound_date = input("Enter outbound date (YYYY-MM-DD): ")
    fs = FlightSearch("CDG", "AUS", "2026-09-12")
    fs.printList()

