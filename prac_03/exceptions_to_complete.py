"""
CP1404/CP5632 - Practical3
Program to safely get a valid integer from the user, handling non-numeric input
without crashing by catching ValueError exceptions.
"""

is_finished = False
while not is_finished:
    try:
        result = int(input("Enter a valid integer: "))
        is_finished = True  # Exit loop on valid integer
    except ValueError:  # Catch invalid integer input
        print("Please enter a valid integer.")
print("Valid result is:", result)