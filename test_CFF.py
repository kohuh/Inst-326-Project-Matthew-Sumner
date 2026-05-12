from CFF import FlightSearch
from CFF import Flight
import CFF

fs = CFF.FlightSearch("CDG", "AUS", "2026-09-12")
assert fs.departure == "CDG", "Departure airport code not set correctly"
assert fs.arrival == "AUS", "Arrival airport code not set correctly"
assert fs.outbound_date == "2026-09-12", "Outbound date not set correctly"
assert isinstance(fs.flightList, list), "Flight list not created correctly"