"""Module for SilverServiceTaxi class, a fancy Taxi with flagfall."""

from taxi import Taxi

# Constants
FLAGFALL = 4.50


class SilverServiceTaxi(Taxi):
    """A Taxi with a fanciness multiplier and flagfall charge."""

    def __init__(self, name: str, fuel: float, fanciness: float):
        """Initialise a SilverServiceTaxi with name, fuel, and fanciness.

        Args:
            name (str): The name of the taxi.
            fuel (float): The amount of fuel.
            fanciness (float): Multiplier for price per km.
        """
        super().__init__(name, fuel)
        self.price_per_km = Taxi.price_per_km * fanciness

    def __str__(self) -> str:
        """Return a string representation including flagfall.

        Returns:
            str: Description including parent details and flagfall.
        """
        return f"{super().__str__()} plus flagfall of ${FLAGFALL:.2f}"

    def get_fare(self) -> float:
        """Calculate the fare including flagfall, rounded to nearest 10c.

        Returns:
            float: The total fare for the trip.
        """
        return round(super().get_fare() + FLAGFALL, 1)