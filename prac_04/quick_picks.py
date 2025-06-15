import random

MIN_NUMBER = 1
MAX_NUMBER = 45
NUMBERS_PER_PICK = 6

def generate_quick_pick():
    numbers = []
    while len(numbers) < NUMBERS_PER_PICK:
        num = random.randint(MIN_NUMBER, MAX_NUMBER)
        if num not in numbers:  # Ensure no duplicates
            numbers.append(num)
    numbers.sort()  # Sort in ascending order
    # Format each number to take 2 spaces, right-aligned
    return [f"{num:2}" for num in numbers]

def main():
    try:
        num_picks = int(input("How many quick picks? "))
        if num_picks < 0:
            print("Please enter a non-negative number.")
            return
        for _ in range(num_picks):
            quick_pick = generate_quick_pick()
            print(" ".join(quick_pick))
    except ValueError:
        print("Please enter a valid number.")

main()