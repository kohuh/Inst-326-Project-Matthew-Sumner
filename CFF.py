#Cheap, Financial Flights
from serpapi import GoogleSearch
import pandas as pd
import json

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
            "api_key": "65aadbc33f7564338658dd6568a7b3e2dcc100ebe47fa43f51dbcf03beda75b6", "sort_by":2, "max_price":self.max_price, "type": 2
        }
        search = GoogleSearch(param)
        self.convertToList(search)
    def convertToList(self, dictionary):
        temp=json.loads(dictionary)
        flightList=[]
        for i in temp:
            


            
            
#Potential use case for using Pandas `DataFrame` to store and analyze flight data, including prices, airlines, and departure times.