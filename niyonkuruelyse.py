from collections import deque

class RideSharingApp:
    def __init__(self):
        self.available_drivers = {}
        self.scheduled_rides = deque()
        self.completed_rides = []
        self.undo_stack = []

    def add_driver(self, driver_name):
        """Add a driver to the available drivers list."""
        self.available_drivers[driver_name] = True
        print(f"Driver {driver_name} added.")

    def request_ride(self, passenger_name):
        """Request a ride and schedule it."""
        for driver in self.available_drivers:
            if self.available_drivers[driver]:  
                self.available_drivers[driver] = False  
                ride_request = (passenger_name, driver)
                self.scheduled_rides.append(ride_request)
                self.undo_stack.append(ride_request)
                print(f"Ride requested for {passenger_name} with driver {driver}.")
                return
        print("No available drivers.")

    def complete_ride(self):
        """Complete the ride and make the driver available again."""
        if self.scheduled_rides:
            passenger_name, driver = self.scheduled_rides.popleft()
            self.available_drivers[driver] = True  
            self.completed_rides.append((passenger_name, driver))  
            print(f"Ride completed for {passenger_name} with driver {driver}.")
        else:
            print("No scheduled rides.")

    def undo_request(self):
        """Undo the last ride request."""
        if self.undo_stack:
            last_request = self.undo_stack.pop()
            self.scheduled_rides.remove(last_request)
            passenger_name, driver = last_request
            self.available_drivers[driver] = True  
            print(f"Ride request for {passenger_name} undone. Driver {driver} is now available again.")
        else:
            print("No ride requests to undo.")

    def list_drivers(self):
        """List available drivers in a formatted way."""
        print("\nAvailable Drivers:")
        print("{:<20} {}".format("Driver Name", "Status"))
        print("-" * 30)
        for driver, available in self.available_drivers.items():
            status = "Available" if available else "Busy"
            print("{:<20} {}".format(driver, status))

    def list_scheduled_rides(self):
        """List currently scheduled rides in a formatted way."""
        print("\nScheduled Rides:")
        print("{:<20} {}".format("Passenger Name", "Driver Name"))
        print("-" * 30)
        for passenger_name, driver in self.scheduled_rides:
            print("{:<20} {}".format(passenger_name, driver))

    def list_completed_rides(self):
        """List completed rides in a formatted way."""
        print("\nCompleted Rides:")
        print("{:<20} {}".format("Passenger Name", "Driver Name"))
        print("-" * 30)
        for passenger_name, driver in self.completed_rides:
            print("{:<20} {}".format(passenger_name, driver))

    def run(self):
        
        while True:
            command = input("\n select option: \n\n 1: Add Driver \n 2: Request Ride  \n 3: Complete Ride \n 4: Undo Request \n 5: Show Available Drivers \n 6: Show Scheduled Rides \n 7: Show Completed Rides \n 8: Exit \n  nter your choice : ").strip()
            if command == "1":
                driver_name = input("Enter driver name: ")
                self.add_driver(driver_name)
            elif command == "2":
                passenger_name = input("Enter passenger name: ")
                self.request_ride(passenger_name)
            elif command == "3":
                self.complete_ride()
            elif command == "4":
                self.undo_request()
            elif command == "5":
                self.list_drivers()
            elif command == "6":
                self.list_scheduled_rides()
            elif command == "7":
                self.list_completed_rides()
            elif command == "8":
                print("Exiting the app.")
                break
            else:
                print("Invalid command. Please try again.")

# Run the app
if __name__ == "__main__":
    app = RideSharingApp()
    app.run()
