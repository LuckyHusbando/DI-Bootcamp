#DC Air Management

from datetime import date, datetime, timedelta

class Airline:
    """
    Represents an airline company.
    """
    def __init__(self, id_code: str, name: str):
        self.id = id_code
        self.name = name
        self.planes = []

class Airplane:
    """
    Represents a single airplane.
    """
    def __init__(self, id_num: int, company: Airline, current_location):
        self.id = id_num
        self.company = company
        self.current_location = current_location
        self.next_flights = []

    def fly(self, destination):
        """
        Makes the airplane take off and land if a flight is scheduled for the destination.
        """
        for flight in self.next_flights:
            if flight.destination == destination:
                flight.take_off()
                flight.land()
                return True
        return False

    def location_on_date(self, flight_date: date):
        """
        Returns where the plane will be on a specific date.
        """
        current_location = self.current_location
        for flight in self.next_flights:
            if flight.date <= flight_date:
                current_location = flight.destination
            else:
                break
        return current_location

    def available_on_date(self, flight_date: date, location):
        """
        Checks if the plane can fly from a specific location on a given date.
        """
        # A plane can only fly once per day
        for flight in self.next_flights:
            if flight.date == flight_date:
                return False
        
        # Check if the plane is at the specified location on that date
        if self.location_on_date(flight_date) == location:
            return True
        return False

class Flight:
    """
    Represents a single flight.
    """
    def __init__(self, origin, destination, flight_date: date, plane: Airplane):
        self.origin = origin
        self.destination = destination
        self.date = flight_date
        self.plane = plane
        # ID is encoded as "DESTINATION-AIRLINE_CODE-YYYY-MM-DD"
        self.id = f"{self.destination.city}-{self.plane.company.id}-{self.date.strftime('%Y-%m-%d')}"

    def take_off(self):
        """
        Updates the system when the flight takes off.
        """
        print(f"Flight {self.id} taking off from {self.origin.city}.")
        self.origin.scheduled_departures.remove(self)

    def land(self):
        """
        Updates the system when the flight lands.
        """
        print(f"Flight {self.id} has landed at {self.destination.city}.")
        self.plane.current_location = self.destination
        self.destination.scheduled_arrivals.remove(self)
        
        # Remove the flight from the plane's list after completion
        if self in self.plane.next_flights:
            self.plane.next_flights.remove(self)

class Airport:
    """
    Represents an airport.
    """
    def __init__(self, city: str):
        self.city = city
        self.planes = []
        self.scheduled_departures = []
        self.scheduled_arrivals = []

    def schedule_flight(self, destination, flight_datetime: datetime, airlines: list):
        """
        Finds an available airplane, schedules the flight, and updates all relevant objects.
        """
        flight_date = flight_datetime.date()
        
        # Look for an available plane
        available_plane = None
        for airline in airlines:
            for plane in airline.planes:
                if plane.available_on_date(flight_date, self) and plane.company == airline:
                    available_plane = plane
                    break
            if available_plane:
                break

        if not available_plane:
            print(f"No available plane to schedule a flight from {self.city} to {destination.city} on {flight_date}.")
            return None
        
        # Create the flight
        new_flight = Flight(self, destination, flight_date, available_plane)
        
        # Update lists
        self.scheduled_departures.append(new_flight)
        self.scheduled_departures.sort(key=lambda f: f.date)

        destination.scheduled_arrivals.append(new_flight)
        destination.scheduled_arrivals.sort(key=lambda f: f.date)

        available_plane.next_flights.append(new_flight)
        available_plane.next_flights.sort(key=lambda f: f.date)
        
        print(f"Flight {new_flight.id} scheduled from {self.city} to {destination.city}.")
        return new_flight

    def info(self, start_date: date, end_date: date):
        """
        Displays every scheduled departure from the airport within a date range.
        """
        print(f"\n--- Scheduled Departures from {self.city} ({start_date} to {end_date}) ---")
        found_flights = False
        for flight in self.scheduled_departures:
            if start_date <= flight.date <= end_date:
                print(f"  - Flight {flight.id} to {flight.destination.city} on {flight.date} with plane {flight.plane.id}")
                found_flights = True
        if not found_flights:
            print("  No flights scheduled in this period.")
        print("---------------------------------------------------\n")

# --- Test Program ---
if __name__ == "__main__":
    # 1. Create Airlines and Airports
    emirates = Airline("EK", "Emirates")
    qatar_airways = Airline("QR", "Qatar Airways")

    dubai_airport = Airport("DXB")
    doha_airport = Airport("DOH")
    london_airport = Airport("LHR")

    # 2. Create Airplanes and assign them to airlines and airports
    plane1_ek = Airplane(101, emirates, dubai_airport)
    plane2_ek = Airplane(102, emirates, dubai_airport)
    plane3_qr = Airplane(201, qatar_airways, doha_airport)

    emirates.planes.append(plane1_ek)
    emirates.planes.append(plane2_ek)
    qatar_airways.planes.append(plane3_qr)

    dubai_airport.planes.extend([plane1_ek, plane2_ek])
    doha_airport.planes.append(plane3_qr)

    all_airlines = [emirates, qatar_airways]
    
    today = date.today()
    tomorrow = today + timedelta(days=1)
    day_after_tomorrow = today + timedelta(days=2)

    # 3. Schedule some flights
    dubai_airport.schedule_flight(london_airport, datetime.now() + timedelta(days=1), all_airlines)
    doha_airport.schedule_flight(dubai_airport, datetime.now() + timedelta(days=2), all_airlines)
    london_airport.schedule_flight(doha_airport, datetime.now() + timedelta(days=3), all_airlines)

    # 4. Display airport info for a date range
    dubai_airport.info(today, day_after_tomorrow + timedelta(days=5))

    # 5. Simulate a flight and check updates
    print("\n--- Simulating a flight ---")
    first_flight = dubai_airport.scheduled_departures[0]
    
    # Check plane's location before flight
    print(f"Plane {first_flight.plane.id} location before flight: {first_flight.plane.current_location.city}")
    first_flight.plane.fly(first_flight.destination)

    # Check plane's location after flight
    print(f"Plane {first_flight.plane.id} location after flight: {first_flight.plane.current_location.city}")

    # 6. Display updated info
    dubai_airport.info(today, day_after_tomorrow + timedelta(days=5))
    london_airport.info(today, day_after_tomorrow + timedelta(days=5))