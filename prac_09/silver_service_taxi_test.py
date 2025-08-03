"""Module to test the SilverServiceTaxi class."""

from silver_service_taxi import SilverServiceTaxi
from taxi import PRICE_PER_KM
from silver_service_taxi import FLAGFALL


def main():
    """Test the SilverServiceTaxi class with a sample trip."""
    taxi = SilverServiceTaxi("Hummer", 200, 2)

    # Drive 18 km
    taxi.drive(18)
    fare = taxi.get_fare()
    print(f"Taxi details: {taxi}")
    print(f"Fare for 18 km: ${fare:.2f}")

    # Test fare: 18 km * 1.23 * 2 + 4.50 = 48.78, rounded to 48.80
    expected_fare = round((18 * PRICE_PER_KM * 2 + FLAGFALL), 1)
    assert fare == expected_fare, f"Expected fare ${expected_fare}, got ${fare}"

main()