"""
CP1404/CP5632 Practical - Client code to use the Car class.
Note that the import has a folder (module) in it.
This is why we name our folders with no spaces or capitals, as valid module names.
Estimated time: 15 minutes
Actual start time: 05:18 PM, July 05, 2025
Actual end time: [To be recorded]
"""

from prac_06.car import Car


def main():
    """Demo test code to show how to use car class with named car 'limo'."""
    # Create a new Car object called "limo" with 100 units of fuel
    limo = Car("Limo", 100)

    # Add 20 more units of fuel
    limo.add_fuel(20)

    # Print the amount of fuel
    print(f"Limo fuel: {limo.fuel}")

    # Attempt to drive 115 km
    limo.drive(115)

    # Print the car object to test __str__
    print(limo)


if __name__ == "__main__":
    main()