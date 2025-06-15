"""
CP1404/CP5632 Practical
Data file -> lists program
"""

def load_data():
    """Read data from file and return as a list of lists."""
    data = []
    with open('subject_data.txt', 'r') as file:
        for line in file:
            line = line.strip()  # Remove trailing newline
            parts = line.split(',')  # Split line into parts
            parts[2] = int(parts[2])  # Convert student number to integer
            data.append(parts)  # Add parts to data list
    return data

def display_subject_details(data):
    """Display subject details in a formatted way."""
    for subject, lecturer, students in data:
        print(f"{subject} is taught by {lecturer} and has {students} students")

def main():
    """Main function to load and display subject data."""
    data = load_data()
    display_subject_details(data)

main()