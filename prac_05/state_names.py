"""CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

# Dictionary literals formatted with no space before, one space after colon
CODE_TO_NAME = {
    "QLD": "Queensland",
    "NSW": "New South Wales",
    "NT": "Northern Territory",
    "WA": "Western Australia",
    "ACT": "Australian Capital Territory",
    "VIC": "Victoria",
    "TAS": "Tasmania",
    "SA": "South Australia" }

# Added whitespace after ':' in print
print(CODE_TO_NAME)

state_code = input("Enter short state: ").lower()
while state_code != "":
    if state_code.upper() in CODE_TO_NAME:
        print(state_code, "is", CODE_TO_NAME[state_code.upper()])
    else:
        print("Invalid short state")
    state_code = input("Enter short state: ").lower()

# Loop to print all states and names neatly lined up
for code, name in CODE_TO_NAME.items():
    print(f"{code} is {name}")