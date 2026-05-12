#Cheap, Financial Flights
import serpapi 
import os

class FlightSearch:
    """
    Class to search for flights using SerpAPI. Objective is to create a list of flight objects,
    filter by price, sort by price, and print the list of flights.
    """
    def __init__(self, departure, arrival, outbound_date):
        """
        Initalizes the parameters for flight search and creates a list of the flight objects, which can later be sorted by price or 
        filtered by price range.
        Arguments:
        departure (str): The departure airport code
        arrival (str): The arrival airport code 
        outbound_date (str): The date of departure in the format "YYYY-MM-DD"
        """
        self.departure=departure
        self.arrival=arrival
        self.outbound_date=outbound_date
        #self.api_key = os.getenv("api_key")
        self.api_key = "3d39eb189e17e631e1448aaa9fe368fc52344f30a2a3ad937f26f066ceec1b52"
        param = {
            "engine": "google_flights", "departure_id": self.departure, "arrival_id": self.arrival, "outbound_date": self.outbound_date, "currency": "USD", "hl": "en",
            "sort_by":2, "type": 2
        }
        #This creates a list of flight objects, from which we can sort by price/filter by price range.
        client = serpapi.Client(api_key=self.api_key)
        search = client.search(param)
        all_itineraries = search.get("best_flights", []) + search.get("other_flights", [])
        self.flightList=self.createList(all_itineraries) #creates list of flight objects

    #Unit test for __init__ function
    #fs = FlightSearch("CDG", "AUS", "2026-09-12")
    # assert fs.departure == "CDG", "Departure airport code not set correctly"
    # assert fs.arrival == "AUS", "Arrival airport code not set correctly"
    # assert fs.outbound_date == "2026-09-12", "Outbound date not set correctly"
    # assert isinstance(fs.flightList, list), "Flight list not created correctly"

    def sortByPrice(self):
        """
        Sorts list of flight objects by price from lowest to highest.
        return: (var) sorted list of flight onbjects in ascending order by price
        """
        return sorted(self.flightList)
    
    #Unit test for sortByPrice function
    #fs = FlightSearch("CDG", "AUS", "2026-09-12")
    # sorted_flights = fs.sortByPrice()
    # assert sorted_flights == sorted(fs.flightList), "Flights not sorted correctly by price"

    def setPriceRange(self, max_price, min_price=0):
        """
        Filters list of flight objects by price range between min_price and max_price. 
        Default min_price is set to 0. If min_price is 0, then the function will return all
        flights with a price less than max_price. if min_price is greater than 0,
        the function will return all flights with a price between min_price and max_price.
        Arguments:
        max_price (float): The maximum price for the flight.
        min_price (float): The minimum price for the flight.
        return: (var) list of flight objects with price between min_price and max_price
        """
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
    
    #Unit test for setPriceRange function
    fs = FlightSearch("CDG", "AUS", "2026-09-12")
    assert len(fs.setPriceRange(500))==len(fs.flightList), "When price range with min_price=0, return all flights with price less than max_price."

    
    def printList(self):
        """
        Prints the list of flight objects in a readable format.
        """
        for i in self.flightList:
            print(i) 
            print("\n")

    #unit test for printList function
    #fs = FlightSearch("CDG", "AUS", "2026-09-12")
    # fs.printList(), "prints list of flight objects in readable format"

    def createList(self, input):
        """
        Creates a list of flight objects based on input data from SerpAPI. Using the flight number,
        airline, price, departure time, arrival time, duration, and layover information to create the flight objects.
        Arguments:
        input (list): A list of flight data from SerpAPI, which contains information about the flights (flight number, airline,
        price, departure time, arrival time, duration, and layover information).
        return: (var) list of flight objects created from the input data.
        """
        flight_list=[]
        for t in input:
            first_leg=t["flights"][0]
            last_leg=t["flights"][-1]
            has_layover = len(t.get("layovers", [])) > 0
            flight_list.append(Flight(first_leg["flight_number"], first_leg["airline"], t["price"], first_leg["departure_airport"]["time"], last_leg["arrival_airport"]["time"], duration=t["total_duration"], layover=has_layover))
        return flight_list

    # Unit test for createList function
    # This will be a explained through a written test procedure, since the alternative requires many lines of code to 
    # create a mock input for the function. To test the createList function, we can begin by building mock input data and 
    # paramaters that are similar to what we would get from SerpAPI. This would be a dictionary which would include the following
    # keys: "flight_number, "airline", "price", "departure_airport", "arrival_airport", "total_duration", and "layovers". 
    # The value for the "departure_airport" and "arrival_airport" keys would be another dictionary with the key "time" and a
    # value of a string representing the departure and arrival time. The value for the "layovers" key would be a list, which would 
    # be empty if there are no layovers and would contain information about the layover if there is one. Once we have this 
    # mock input data, we can call the createList function with this data and check whether the output recieved is a list of
    # flight objects with the correct attributes based on the input data. 
    
    
class Flight():
    """
    Creates a flight object with the following attributes: flight number, airline, price, departure time,
    arrival time, duration, and layover info, which can be used to sort by price/filter by price range.
    """
    def __init__(self, flight_number, airline, price, departure_time, arrival_time, duration=0, layover=False,):
        """
        Initalized flight objects with the following attributes: flight number, airline, price, departure time,
        arrival time, duration, and layover info.
        Arguments:
        flight_number (str): The flight number.
        airline (str): The airline of the flight
        price (float): The price of the flight.
        departure_time (str): The departure time of the flight.
        arrival_time (str): The arrival time of the flight.
        duration (str): The duration of the flight.
        layover (bool): A boolean value indicating whether the flight has a layover or not. Default is set to False.
        """
        self.flight_number=flight_number
        self.airline=airline 
        self.price=price 
        self.departure_time=departure_time
        self.arrival_time=arrival_time
        self.duration=duration
        self.layover=layover

    #Unit test for __init__ function
    #flight = Flight("AA755", "American Airlines", 781.0, "2026-09-12 13:55:00", "2026-09-12 20:27:00", 812, True)
    # assert flight.flight_number == "AA755", "Flight number not set correctly"
    # assert flight.airline == "American Airlines", "Airline not set correctly"
    # assert flight.price == 781.0, "Price not set correctly"
    # assert flight.departure_time == "2026-09-12 13:55:00", "Departure time not set correctly"
    # assert flight.arrival_time == "2026-09-12 20:27:00", "Arrival time not set correctly"
    # assert flight.duration == 812, "Duration not set correctly"
    # assert flight.layover == True, "Layover info not set correctly"

    def __lt__(self, other):
        """
        Compares price of two flight objects and returns True if the price of the current flight is less than the price of the other flight,
        otherwise returning false. If the object is not an instance of the Flight class, raise ValueError.
        Arguments:
        other (var): The object to compare the current flight object to.
        return: (bool) If the price of the current flight is less than the price, return True, otherwise return False. 
        If the object is not an instance of the Flight class, raise ValueError.
        """
        if isinstance(other, Flight):
            if other.price>=self.price:
                return True
            else:
                return False
        else:
            raise ValueError("Object Other is not Instance of Flight object")
    
    #Unit test for __lt__ function
    #flight1 = Flight("AA755", "American Airlines", 781.0, "2026-09-12 13:55:00", "2026-09-12 20:27:00", 812, True)
    #flight2 = Flight("BA305", "British Airways", 801.0, "2026-09-12 14:15:00", "2026-09-12 20:35:00", 800, False)
    # assert flight1.__lt__(flight2) == True, "Flight 1 should be less than Flight 2 based on price"
    # assert flight2.__lt__(flight1) == False, "Flight 2 should not be less than Flight 1 based on price"
        
    def __eq__(self, other):
        """
        Compares prices of two flight objects and returns True. If the price of the current flight is equal to that of the other flight,
        return true, otherwise, return false. If the object is not an instance of the Flight class, raise ValueError.
        Arguments:
        other (var): The object to compare the current flight object to.
        return: (bool) If the price of the current flight is equal to the other price, return True, otherwise return False. 
        If the object is not an instance of the Flight class, raise ValueError.
        """
        if isinstance(other, Flight):
            if other.price==self.price:
                return True
            else:
                return False
        else:
            raise ValueError("Object Other is not Instance of Flight object")
    #Unit test for __eq__ function
    #flight1 = Flight("AA755", "American Airlines", 781.0, "2026-09-12 13:55:00", "2026-09-12 20:27:00", 812, True)
    #flight2 = Flight("BA305", "British Airways", 801.0, "2026-09-12 14:15:00", "2026-09-12 20:35:00", 800, False)
    #assert flight1.__eq__(flight2) == False, "Flight 1 should not be equal to Flight 2 based on price"
        
    def __str__(self):
        """
        Return a string of the flight object in a readable format, including flight number, airline, price, departure time,
        arrival time, duration.
        return: (str) A string of the flight object in a readable format including afformentioned attributes.
        """
        return f"airline flight number {self.flight_number} on {self.airline}, for ${self.price} dollars, leaving at {self.departure_time}, and arriving at {self.arrival_time}, for a total of {self.duration} minutes."
    #Unit test for __str__ function
    #flight = Flight("AA755", "American Airlines", 781.0, "2026-09-12 13:55:00", "2026-09-12 20:27:00", 812, True)
    #assert flight.__str__() == "airline flight number AA755 on American Airlines, for $781.0 dollars, leaving at 2026-09-12 13:55:00, and arriving at 2026-09-12 20:27:00, for a total of 812 minutes.", "String representation of flight object not correct"
    
    def __repr__(self):
        """
        Returns a string of the flight objects in the __repr__ format for understanding the attributes of the flight object.
        These elements include: flight number, airline, price, departure time, arrival time, and duration.
        return: (str) A string of the flight object including the afformentioned attributes.
        """
        return f"({self.flight_number}, {self.airline}, {self.price}, {self.departure_time}, {self.arrival_time}, {self.duration}, {self.layover}.)"
    
    #Unit test for __repr__ function
    #flight = Flight("AA755", "American Airlines", 781.0, "2026-09-12 13:55:00", "2026-09-12 20:27:00", 812, True)
    #assert flight.__repr__() == "(AA755, American Airlines, 781.0, 2026-09-12 13:55:00, 2026-09-12 20:27:00, 812, True.)", "Repr representation of flight object not correct"

if __name__ == "__main__":
    """
    The main function to create a flight search object with the following paramters:
    departure code, arrival code, and outbound date.
    """
    fs = FlightSearch("CDG", "AUS", "2026-09-12")
    fs.printList()