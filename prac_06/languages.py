"""
Program to demonstrate ProgrammingLanguage class.
Estimated time: 30 minutes
Actual start time: 05:00 PM, July 05, 2025
Actual end time: 05:40 PM
"""

from programming_language import ProgrammingLanguage

# Create language objects
python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

# Print python to test __str__
print(python)

# Create a list of languages
languages = [python, ruby, visual_basic]

# Print dynamically typed languages
print("The dynamically typed languages are:")
for language in languages:
    if language.is_dynamic():
        print(language.name)