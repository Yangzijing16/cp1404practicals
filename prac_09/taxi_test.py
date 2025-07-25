"""Module to test the Taxi class."""

from taxi import Taxi


def main():
    """Test the Taxi class by creating, driving, and checking fares."""
    # Create a new taxi
    my_taxi = Taxi("Prius 1", 100)

    # Drive 40 km
    my_taxi.drive(40)
    print(f"Taxi details: {my_taxi}")
    print(f"Current fare: ${my_taxi.get_fare():.2f}")

    # Restart the meter and drive 100 km
    my_taxi.start_fare()
    my_taxi.drive(100)
    print(f"Taxi details: {my_taxi}")
    print(f"Current fare: ${my_taxi.get_fare():.2f}")

main()