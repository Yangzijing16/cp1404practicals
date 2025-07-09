"""
Programming Language class for storing language details.
Estimated time: 30 minutes
Actual start time: 05:42 PM, July 05, 2025
Actual end time: 06:16 PM
"""

class ProgrammingLanguage:
    def __init__(self, name, typing, reflection, year):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        return self.typing == "Dynamic"

    def __str__(self):
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"