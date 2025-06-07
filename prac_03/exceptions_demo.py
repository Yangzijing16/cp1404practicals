"""
CP1404/CP5632 - Practical3
A simple division calculator that safely handles user input.
Ensures valid numeric inputs and prevents division by zero by checking the denominator,
with results formatted to two decimal places.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))

    if denominator == 0:
        print("Cannot divide by zero!")
    else:
        fraction = numerator / denominator
        print(f"{fraction:.2f}")  # Format to 2 decimal places for clarity
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")