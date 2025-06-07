"""
CP1404/CP5632 - Practical
Exercises to practice file handling: writing a name to a file, reading it back,
and summing numbers from a file using different reading techniques.
"""

#Write name to name.txt using open and close
name = input("Enter your name: ")
out_file = open("name.txt", "w")
out_file.write(name)
out_file.close()

#Read name from name.txt and print greeting using read, open and close
in_file = open("name.txt", "r")
name = in_file.read().strip()  # Use read() to get entire content, strip to remove newline
print(f"Hi {name}!")
in_file.close()

#Read first two numbers from numbers.txt, sum them, using readline and with
with open("numbers.txt", "r") as in_file:
    first_number = int(in_file.readline().strip())  # Read first line
    second_number = int(in_file.readline().strip())  # Read second line
    total = first_number + second_number
    print(total)

#Read all numbers from numbers.txt, sum them, using for line in file and with
total = 0
with open("numbers.txt", "r") as in_file:
    for line in in_file:
        total += int(line.strip())  # Convert each line to int, strip newline
print(total)