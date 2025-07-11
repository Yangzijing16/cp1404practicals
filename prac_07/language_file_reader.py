"""
CP1404/CP5632 Practical
File and class example - opens/reads a file, stores in objects of custom class
(contains multiple versions for demonstration: using csv and namedtuple)
"""

from programming_language import ProgrammingLanguage

def main():
    """Load and display programming languages from a CSV file."""
    languages = load_languages("languages.csv")
    print("Programming Languages:")
    for language in languages:
        print(language)

def load_languages(filename):
    """Load programming languages from a CSV file.

    Args:
        filename (str): Path to the CSV file.

    Returns:
        list: List of ProgrammingLanguage objects.
    """
    languages = []
    with open(filename, 'r') as file:
        file.readline()  # Skip header
        for line in file:
            parts = line.strip().split(',')
            name = parts[0]
            typing = parts[1]
            reflection = parts[2].lower() == 'true'
            year = int(parts[3])
            pointer_arithmetic = parts[4].lower() == 'true'
            language = ProgrammingLanguage(name, typing, reflection, year, pointer_arithmetic)
            languages.append(language)
    return languages

main()
