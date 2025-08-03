"""
Testing exercises for CP1404 Practical 10.
Name: Yang Zijing
ID: 14817731
Description: Implements functions with assert and doctest for string repetition, word length check,
sentence formatting, and Car fuel validation.
"""
import doctest

# Named constants
DEFAULT_WORD_LENGTH = 5
REPEAT_TEST_STRING = "hi"
REPEAT_TEST_COUNT = 3
REPEAT_TEST_EXPECTED = "hi hi hi"
CAR_TEST_FUEL_1 = 100
CAR_TEST_FUEL_2 = 0


def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between.

    Args:
        s (str): The string to repeat.
        n (int): Number of times to repeat the string.

    Returns:
        str: The string repeated n times with spaces between each repetition.
    """
    return " ".join([s] * n)


def is_long_word(word, length=DEFAULT_WORD_LENGTH):
    """Check if word is longer than or equal to length.

    Args:
        word (str): The word to check.
        length (int, optional): Minimum length. Defaults to 5.

    Returns:
        bool: True if word length is >= length, False otherwise.

    >>> is_long_word("cat")
    False
    >>> is_long_word("python")
    True
    >>> is_long_word("supercalifragilistic", 10)
    True
    """
    return len(word) >= length


def format_sentence(phrase):
    """Format a phrase as a sentence with capital letter and full stop.

    Args:
        phrase (str): The phrase to format.

    Returns:
        str: The formatted sentence.

    >>> format_sentence("hello")
    'Hello.'
    >>> format_sentence("python programming")
    'Python programming.'
    >>> format_sentence("")
    '.'
    """
    if not phrase:
        return "."
    return phrase.capitalize() + "."


class Car:
    """Represent a Car object with fuel attribute."""

    def __init__(self, fuel=0):
        """Initialize a Car instance with fuel.

        Args:
            fuel (float): Amount of fuel in the car.
        """
        self.fuel = fuel


# Assert tests
assert repeat_string(REPEAT_TEST_STRING, REPEAT_TEST_COUNT) == REPEAT_TEST_EXPECTED, "repeat_string test failed"
car = Car(CAR_TEST_FUEL_1)
assert car.fuel == CAR_TEST_FUEL_1, f"Car fuel initialization failed for {CAR_TEST_FUEL_1}"
assert Car(CAR_TEST_FUEL_2).fuel == CAR_TEST_FUEL_2, f"Car fuel initialization failed for {CAR_TEST_FUEL_2}"

if __name__ == "__main__":
    doctest.testmod()