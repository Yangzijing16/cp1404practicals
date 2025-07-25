"""Module for UnreliableCar class, a Car with random drive reliability."""

from car import Car
import random


class UnreliableCar(Car):
    """A Car that may not drive based on reliability percentage."""

    def __init__(self, name: str, fuel: float, reliability: float):
        """Initialise an UnreliableCar with name, fuel, and reliability.

        Args:
            name (str): The name of the car.
            fuel (float): The amount of fuel.
            reliability (float): Percentage chance (0-100) the car will drive.
        """
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance: float) -> float:
        """Drive the car if a random number is less than reliability.

        Args:
            distance (float): The distance to attempt to drive.

        Returns:
            float: The actual distance driven (0 if unreliable).
        """
        if random.uniform(0, 100) < self.reliability:
            return super().drive(distance)
        return 0