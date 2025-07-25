"""
CP1404/CP5632 Practical - Suggested Solution
Programming Language class with tests.
"""


class ProgrammingLanguage:
    def __init__(self, name, typing, reflection, year, pointer_arithmetic):
        """Initialize a ProgrammingLanguage instance.

        Args:
            name (str): Name of the programming language.
            typing (str): Typing discipline (e.g., Dynamic, Static).
            reflection (bool): Whether the language supports reflection.
            year (int): Year the language first appeared.
            pointer_arithmetic (bool): Whether the language supports pointer arithmetic.
        """
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year
        self.pointer_arithmetic = pointer_arithmetic

    def __str__(self):
        """Return a string representation of the ProgrammingLanguage."""
        return (f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, "
                f"Pointer Arithmetic={self.pointer_arithmetic}, First appeared in {self.year}")

    def is_dynamic(self):
        """Return True if the language is dynamically typed."""
        return self.typing == "Dynamic"
