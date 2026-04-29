#Cheap, Financial Flights

#1) data processing component that pulls data from API
#Make sure you download the following before running the code:
#pip install google-search-results



import pandas as pd
import serpapi 


Class CheapFinancialFlights:
    def __init__(self):
        self.api_key = "65aadbc33f7564338658dd6568a7b3e2dcc100ebe47fa43f51dbcf03beda75b6"

    def get_flight_data(self):
            """
            This function retrieves flight records from user input and returns a list of the 10 cheapest flights that match the criteria. It uses the SerpAPI to access flight data and processes it to find the best options for the user.
            """
            "api_key": self.api_key
            departure = input("Enter departure airport code (e.g., PQC): ")
            arrival = input("Enter arrival airport code (e.g., AUS): ")
            airline = input("Enter preferred airline (optional): ")
            outbound_date = input("Enter outbound date (YYYY-MM-DD): ")
            return_date = input("Enter return date (YYYY-MM-DD): ")

        params = {
            "api_key": self.api_key,
            "engine": "google_flights",
            "departure_id": "PQC",
            "arrival_id": "AUS",
            "outbound_date": "2025-10-08",
            "return_date": "2025-10-22",
            "deep_search": "true"}

#Need to include price filter for user to filter out flights that are above a certain price point. Also, potential for a filter for flight duration to ensure that the user is not presented with flights that are too long or too short for their preferences. This can be if we don't meet enough of the requirments for code patterns.

results = serpapi.search(params)



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
