#Cheap, Financial Flights
from serpapi import GoogleSearch
import pandas as pd

param = {
    "engine": "google_flights",
    "departure_id": "JFK",          
    "arrival_id": "LAX",         
    "outbound_date": "2026-06-15",  
    "currency": "USD",
    "hl": "en",
    "api_key": "65aadbc33f7564338658dd6568a7b3e2dcc100ebe47fa43f51dbcf03beda75b6"
}

search = GoogleSearch(param)

#Potential use case for using Pandas `DataFrame` to store and analyze flight data, including prices, airlines, and departure times.