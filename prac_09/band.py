"""Module for Band class, managing a group of musicians."""

from musician import Musician


class Band:
    """A band with a name and list of musicians."""

    def __init__(self, name: str, musicians: list):
        """Initialise a Band with a name and list of musicians.

        Args:
            name (str): The name of the band.
            musicians (list): List of Musician objects.
        """
        self.name = name
        self.musicians = musicians

    def __str__(self) -> str:
        """Return a string representation of the band.

        Returns:
            str: Band name and musician details.
        """
        return f"{self.name} ({', '.join(str(musician) for musician in self.musicians)})"

    def play(self) -> None:
        """Have each musician play their instrument."""
        for musician in self.musicians:
            print(musician.play())