"""
Program to manage guitars.
Estimated time: 15 minutes
Actual start time: 03:20 PM, July 06, 2025
Actual end time: 3:40 PM
"""

from guitar import Guitar

guitars = []

# For testing, add guitars directly
guitars.append(Guitar("Fender Stratocaster", 2014, 765.40))
guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.90))

# Uncomment for user input
# print("My guitars!")
# while True:
#     name = input("Name: ")
#     if not name:
#         break
#     year = int(input("Year: "))
#     cost = float(input("Cost: "))
#     guitars.append(Guitar(name, year, cost))
#     print(f"{name} ({year}) : ${cost:,.2f} added.\n")

print("\nThese are my guitars:")
for i, guitar in enumerate(guitars, 1):
    vintage_string = " (vintage)" if guitar.is_vintage() else ""
    print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")