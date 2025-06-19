"""
Module: wimbledon_analysis
Description: Reads Wimbledon gentlemen's singles champions data, counts champions' wins, and lists countries.
Estimate: 30 minutes
Actual Time: 28 minutes
"""


def read_wimbledon_data(filename):
    """Reads CSV file and returns list of lists containing Wimbledon data."""
    data = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        next(in_file)  # Skip header
        for line in in_file:
            year, country, champion, _, _, _ = line.strip().split(',')
            data.append([year, country, champion])
    return data


def count_champions(data):
    """Counts number of wins per champion using a dictionary."""
    champion_to_wins = {}
    for _, _, champion in data:
        champion_to_wins[champion] = champion_to_wins.get(champion, 0) + 1
    return champion_to_wins


def get_countries(data):
    """Extracts unique countries in alphabetical order using a set."""
    countries = set(row[1] for row in data)
    return sorted(countries)


def main():
    """Processes Wimbledon data and displays champions' wins and countries."""
    filename = "wimbledon.csv"
    data = read_wimbledon_data(filename)

    # Count champions
    champion_to_wins = count_champions(data)
    print("Wimbledon Champions:")
    for champion, wins in sorted(champion_to_wins.items()):
        print(f"{champion} {wins}")

    # Get countries
    countries = get_countries(data)
    print("\nThese", len(countries), "countries have won Wimbledon:")
    print(', '.join(countries))

main()