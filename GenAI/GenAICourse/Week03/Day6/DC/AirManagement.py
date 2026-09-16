#AirManagement

import datetime
from typing import List, Optional

class Airline:
    """Represents an airline company."""
    def __init__(self, code: str, name: str):
        self.id = code
        self.name = name
        self.planes: List['Airplane'] = []

class Airplane:
    """Represents an individual airplane."""
    all_airplanes = []

    def __init__(self, plane_id: int, company: Airline, current_location: 'Airport'):
        self.id = plane_id
        self.company = company
        self.current_location = current_location
        self.next_flights: List['Flight'] = []

        #Register the airplane with its company, current airport, and the global registry
        self.company.planes.append(self)
        self.current_location.planes.append(self)
        Airplane.all_airplanes.append(self)

    def location_on_date(self, target_date: datetime.date) -> 'Airport':
        """Calculates where the plane will be at the start of the given date."""
        expected_location = self.current_location
        #Iterate through scheduled flights to track its movements before the target date.
        for flight in self.next_flights:
            if flight.date < target_date:
                expected_location = flight.destination
        return expected_location
    
    def available_on_date(self, target_date: datetime.date, location: 'Airport') ->bool:
        """Returns True if the plane can fly from 'location' on 'target_date'."""
        #Constraint 1: A plane can only fly once per day.
        for flight in self.next_flights:
            if flight.date == target_date:
                return False
            
        #Constraint 2: The plane must actually be at the requested location on that date.
        expected_location = self.location_on_date(target_date)
        return expected_location == location
    
    def fly(self, destination: 'Airport'):
        """Executes the next flight to the given destination."""
        flight_to_execute = None

        #Find the next scheduled flight to this destination.
        for flight in self.next_flights:
            if flight.destination == destination:
                flight_to_execute = flight
                break

        if flight_to_execute:
            flight_to_execute.take_off()
            flight_to_execute.land()

            #Remove the completed flight from the airplane's schedule
            self.next_flights.remove(flight_to_execute)

            #Optionally clean up the airport schedules
            if flight_to_execute in flight_to_execute.origin.scheduled_departures:
                flight_to_execute.origin.scheduled_departures.remove(flight_to_execute)
            if flight_to_execute in flight_to_execute.destination.scheduled_arrivals:
                flight_to_execute.destination.scheduled_arrivals.remove(flight_to_execute)
            print(f"Plane {self.id} successfully flew to {destination.city}.")
        else:
            print(f"Plane {self.id} has no scheduled flight to {destination.city}.")

class Flight:
    """Represents a scheduled flight."""
    def __init__(self, flight_date: datetime.date, origin: 'Airport', destination: 'Airport', plane: Airplane):
        self.date = flight_date
        self.origin = origin
        self.destination = destination
        self.plane = plane

        #ID Format: Destination City + Airline Code = YYYYMMDD
        date_str = self.date.strftime("%Y%m%d")
        self.id = f"{self.destination.city}-{self.plane.company.id}-{date_str}"

    def take_off(self):
        """Removes the plane from the origin airport's grounded list."""
        if self.plane in self.origin.planes:
            self.origin.planes.remove(self.plane)

    def land(self):
        """Updates the plane's location and adds it to the destination airport."""
        self.plane.current_location = self.destination
        self.destination.planes.append(self.plane)

class Airport:
    """Represents an airport."""
    def __init__(self, city_code: str):
        self.city = city_code
        self.planes: List[Airplane] = []
        self.scheduled_departures: List[Flight] = []
        self.scheduled_arrivals: List[Flight] = []

    def scheduled_flight(self, destination: 'Airport', flight_date: datetime.date) -> Optional[Flight]:
        #Finds an available plane and schedules a flight to the destination.
        available_plane = None

        #Search global registry for an available plane
        for plane in Airplane.all_airplanes:
            if plane.available_on_date(flight_date, self):
                available_plane = plane
                break

        if not available_plane:
            print(f"Error: No airplanes available from {self.city} to {destination.city} on {flight_date}.")
            return None
        
        #Create the Flight
        new_flight = Flight(flight_date, self, destination, available_plane)

        #Update and sort Airplane schedule
        available_plane.next_flights.append(new_flight)
        available_plane.next_flights.sort(key=lambda f: f.date)

        #Update and sort Airport schedules
        self.scheduled_departures.append(new_flight)
        self.scheduled_departures.sort(key=lambda f: f.date)

        destination.scheduled_arrivals.append(new_flight)
        destination.scheduled_arrivals.sort(key=lambda f: f.date)

        print(f"Scheduled: Flight {new_flight.id} from {self.city} to {destination.city} on {flight_date}")
        return new_flight
    
    def info(self, start_date: datetime.date, end_date: datetime.date):
        """Displays all scheduled deparatures and arrivals between two dates."""
        print(f"\n--- Flight Info for {self.city} ({start_date} to {end_date}) ---")

        print("Departures:")
        for f in self.scheduled_departures:
            if start_date <= f.date <= end_date:
                print(f" {f.date} | ID: {f.id} | To: {f.destination.city} | Plane: {f.plane.id}")

        print("Arrivals:")
        for f in self.scheduled_arrivals:
            if start_date <= f.date <= end_date:
                print(f" {f.date} | ID: {f.id} | To: {f.destination.city} | Plane: {f.plane.id}")
                
        print("Arrivals:")
        for f in self.scheduled_arrivals:
            if start_date <= f.date <= end_date:
                print(f"  {f.date} | ID: {f.id} | From: {f.origin.city} | Plane: {f.plane.id}")
        print("--------------------------------------------------\n")

##Test The Program##

if __name__ == "__main__":
    # 1. Setup Dates
    today = datetime.date(2026, 7, 20)
    tomorrow = datetime.date(2026, 7, 21)
    day_after = datetime.date(2026, 7, 22)

    # 2. Setup Airports
    jfk = Airport("JFK")
    lhr = Airport("LHR")
    cdg = Airport("CDG")

    # 3. Setup Airline and Airplane
    delta = Airline("DL", "Delta Airlines")
    
    # Plane 101 starts at JFK
    plane_101 = Airplane(101, delta, jfk)

    print("--- Scheduling Flights ---")
    # Schedule flight from JFK to LHR today
    f1 = jfk.scheduled_flight(lhr, today)
    
    # Try scheduling another flight for the same plane today (Should fail: only 1 flight per day)
    f2_fail = jfk.scheduled_flight(cdg, today)

    # Schedule flight from LHR to CDG tomorrow (Plane will be at LHR tomorrow, so it works)
    f3 = lhr.scheduled_flight(cdg, tomorrow)

    # 4. Display Airport Info
    jfk.info(today, day_after)
    lhr.info(today, day_after)

    # 5. Execute the flight
    print("--- Executing Flights ---")
    print(f"Before take-off, planes at JFK: {[p.id for p in jfk.planes]}")
    print(f"Before take-off, planes at LHR: {[p.id for p in lhr.planes]}")
    
    plane_101.fly(lhr)
    
    print(f"After landing, planes at JFK: {[p.id for p in jfk.planes]}")
    print(f"After landing, planes at LHR: {[p.id for p in lhr.planes]}")