#Cheap, Financial Flights

#1) data processing component that pulls data from API
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



#Potential use case for using Pandas `DataFrame` to store and analyze flight data, including prices, airlines, and departure times


#2) data processing component to clean up the data
#Potential use case for using Pandas `DataFrame` to clean and preprocess the flight data, such as handling missing values, converting data types, and filtering out irrelevant information

#3) pricing component to get the prices for flights
#Allows for easy sorting and querying of price data, the primary function of our app is to expeditiously find flights which match the users criteria for the cheapest possible price.

#4) logic component for the flights

#We would be using filters for flight options based on user preference, such as price, duration, and airline. Additionally, by implementing a sorting algorithm, we can rank flight options based on affordability and time spent in air

# Plan unit test 1: Making sure that the data was correcetly pulled from the API and gives us our desirable data
# Plan unit test 2: ensure that the 10 reported flights are the cheapest possible
# Plan unit test 3: Raise value error if user inputs a destination or airport which does not exist
# Plan unit test 4: return nothing if the flight criteria is not possible
