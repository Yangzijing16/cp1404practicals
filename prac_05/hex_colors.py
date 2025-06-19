# Colour code lookup program

# Constant dictionary of colour names and their hex codes
COLOUR_CODES = {
    "aliceblue": "#f0f8ff",
    "amethyst": "#9966cc",
    "amber": "#ffbf00",
    "azure": "#f0ffff",
    "beige": "#f5f5dc",
    "bisque": "#ffe4c4",
    "black": "#000000",
    "blond": "#faf0be",
    "cerise": "#de3163",
    "fawn": "#e5aa70"
}

colour_name = input("Enter colour name (or press Enter to quit): ").lower()
while colour_name != "":
    if colour_name in COLOUR_CODES:
        print(f"{colour_name} is {COLOUR_CODES[colour_name]}")
    else:
        print("Invalid colour name")
    colour_name = input("Enter colour name (or press Enter to quit): ").lower()
