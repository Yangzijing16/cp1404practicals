# myguitars.py
from guitar import Guitar


def main():
    guitars = load_guitars("guitars.csv")
    print("Guitars:")
    for guitar in guitars:
        print(guitar)

    # Sort by year
    guitars.sort()
    print("\nGuitars sorted by year:")
    for guitar in guitars:
        print(guitar)

    # Add new guitars
    print("\nAdd a new guitar:")
    name = input("Name: ")
    while name:
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitars.append(Guitar(name, year, cost))
        name = input("Name: ")

    # Save to file
    save_guitars("guitars.csv", guitars)
    print("Guitars saved to guitars.csv")


def load_guitars(filename):
    guitars = []
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            name = parts[0]
            year = int(parts[1])
            cost = float(parts[2])
            guitars.append(Guitar(name, year, cost))
    return guitars


def save_guitars(filename, guitars):
    with open(filename, 'w') as file:
        for guitar in guitars:
            file.write(f"{guitar.name},{guitar.year},{guitar.cost}\n")


if __name__ == "__main__":
    main()