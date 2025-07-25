"""Module to test the UnreliableCar class."""

from unreliable_car import UnreliableCar


def main():
    """Test the UnreliableCar class by driving multiple times."""
    car = UnreliableCar("Unreliable", 100, 50)

    # Test driving 100 times, 1 km each
    drives = 0
    for _ in range(100):
        if car.drive(1) > 0:
            drives += 1

    print(f"Drove {drives} times out of 100 attempts")
    print(f"Car details: {car}")

    # Assert drives are within expected range for 50% reliability
    assert 30 <= drives <= 70, f"Expected 30-70 drives, got {drives}"

main()