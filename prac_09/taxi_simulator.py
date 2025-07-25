"""Module for a taxi simulator with Taxi and SilverServiceTaxi classes."""

from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

class TaxiFleet:
    """A collection of taxis for the simulator."""

    def __init__(self, taxis: list):
        """Initialise a TaxiFleet with a list of taxis.

        Args:
            taxis (list): List of Taxi or SilverServiceTaxi objects.
        """
        self.taxis = taxis
        self.current_taxi = None
        self.total_bill = 0.0

    def display_taxis(self) -> None:
        """Display the list of available taxis."""
        print("Taxis available:")
        for i, taxi in enumerate(self.taxis):
            print(f"{i} - {taxi}")

    def choose_taxi(self, choice: str) -> bool:
        """Select a taxi based on user input.

        Args:
            choice (str): The index of the taxi to select.

        Returns:
            bool: True if a valid taxi was chosen, False otherwise.
        """
        try:
            index = int(choice)
            if 0 <= index < len(self.taxis):
                self.current_taxi = self.taxis[index]
                return True
            print("Invalid taxi choice")
            return False
        except ValueError:
            print("Invalid taxi choice")
            return False

    def drive_taxi(self, distance: str) -> bool:
        """Drive the current taxi and update the bill.

        Args:
            distance (str): The distance to drive.

        Returns:
            bool: True if the drive was successful, False otherwise.
        """
        if self.current_taxi is None:
            print("You need to choose a taxi before you can drive")
            return False
        try:
            distance = float(distance)
            distance_driven = self.current_taxi.drive(distance)
            if distance_driven > 0:
                fare = self.current_taxi.get_fare()
                print(f"Your {self.current_taxi.name} trip cost you ${fare:.2f}")
                self.total_bill += fare
                self.current_taxi.start_fare()
                return True
            print("Trip not possible (no fuel or no drive)")
            return False
        except ValueError:
            print("Invalid distance")
            return False

    def get_total_bill(self) -> float:
        """Return the total bill for all trips.

        Returns:
            float: The total bill.
        """
        return self.total_bill

def main():
    """Run the taxi simulator with a menu-driven interface."""
    # Constants for menu options
    QUIT = 'q'
    CHOOSE = 'c'
    DRIVE = 'd'
    VALID_OPTIONS = {QUIT, CHOOSE, DRIVE}

    taxis = [
        Taxi("Prius", 100),
        SilverServiceTaxi("Limo", 100, 2),
        SilverServiceTaxi("Hummer", 200, 4)
    ]
    fleet = TaxiFleet(taxis)
    done = False

    print("Let's drive!")
    while not done:
        choice = input(f"{QUIT})uit, {CHOOSE})hoose taxi, {DRIVE})rive\n>>> ").lower()

        if choice not in VALID_OPTIONS:
            print("Invalid option")
        elif choice == QUIT:
            print(f"Total trip cost: ${fleet.get_total_bill():.2f}")
            print("Taxis are now:")
            fleet.display_taxis()
            done = True
        elif choice == CHOOSE:
            fleet.display_taxis()
            fleet.choose_taxi(input("Choose taxi: "))
        elif choice == DRIVE:
            fleet.drive_taxi(input("Drive how far? "))

        if not done:
            print(f"Bill to date: ${fleet.get_total_bill():.2f}")

main()