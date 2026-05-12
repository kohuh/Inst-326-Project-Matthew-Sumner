from CFF import FlightSearch, Flight


# Unit test for __init__ function
# This is meant to test whether the paramaters for the FlightSearch class are set up correctly.
fs = FlightSearch("CDG", "AUS", "2026-09-12")
assert fs.departure == "CDG", "Departure airport code not set correctly"
assert fs.arrival == "AUS", "Arrival airport code not set correctly"
assert fs.outbound_date == "2026-09-12", "Outbound date not set correctly"
assert isinstance(fs.flightList, list), "Flight list not created correctly"

## class FlightSearch

# Unit test for sortByPrice function
# This is meant to test whether the sortByPrice function is correctly sorting the flight objects 
# in price order.
sorted_flights = fs.sortByPrice()
assert sorted_flights == sorted(fs.flightList), "Flights not sorted correctly by price"

# Unit test for setPriceRange function
# This is meant to test whether the setPriceRange function is filtering the flight objects by a 
# specific price range.
expensive_flight = fs.setPriceRange(1000, 500)
for flight in expensive_flight:
    assert flight.price >= 500 and flight.price <= 1000, "Flight price is not within the specified price range"

#unit test for printList function
fs.printList(), "prints list of flight objects in readable format"

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

## class Flight

#Unit test for __init__ function
# This is meant to test whether the pramaters for Flight class return the correct attributes for the
# flight object.
flight = Flight("AA755", "American Airlines", 781.0, "2026-09-12 13:55:00", "2026-09-12 20:27:00", 812, True)
assert flight.flight_number == "AA755", "Flight number not set correctly"
assert flight.airline == "American Airlines", "Airline not set correctly"
assert flight.price == 781.0, "Price not set correctly"
assert flight.departure_time == "2026-09-12 13:55:00", "Departure time not set correctly"
assert flight.arrival_time == "2026-09-12 20:27:00", "Arrival time not set correctly"
assert flight.duration == 812, "Duration not set correctly"
assert flight.layover == True, "Layover not True when there is a layover"

#Unit test for __lt__ function
# This is meant to test whether the __lt__ function is actually comparing the price the two flight objects
# and returning the associated boolean value
flight1 = Flight("AA755", "American Airlines", 781.0, "2026-09-12 13:55:00", "2026-09-12 20:27:00", 812, True)
flight2 = Flight("BA305", "British Airways", 801.0, "2026-09-12 14:15:00", "2026-09-12 20:35:00", 800, False)
assert flight1.__lt__(flight2) == True, "Flight 1 should be less than Flight 2 based on price"
assert flight2.__lt__(flight1) == False, "Flight 2 should not be less than Flight 1 based on price"

#Unit test for __eq__ function
# This is meant to test if the __eq__ function is comparing the price of two flight objects and returning
# the correct boolean value whether the condition is met.
assert flight1.__eq__(flight2) == False, "Flight 1 should not be equal to Flight 2 based on price"

#Unit test for __str__ function
# This is mean to test whether the __str__ function is returning a correct string representaion of the flight
# object.
assert flight.__str__() == "airline flight number AA755 on American Airlines, for $781.0 dollars, leaving at 2026-09-12 13:55:00, and arriving at 2026-09-12 20:27:00, for a total of 812 minutes.", "String representation of flight object not correct"

#Unit test for __repr__ function
# This is meant to test whether the __repr__ function is returning the correct __repr__ represenation of the
# flight object.
assert flight.__repr__() == "(AA755, American Airlines, 781.0, 2026-09-12 13:55:00, 2026-09-12 20:27:00, 812, True.)", "Repr representation of flight object not correct"
