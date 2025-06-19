"""
Module: email_name_storage
Description: Stores user emails and names in a dictionary, extracting names from emails.
Estimate: 20 minutes
Actual Time: 18 minutes
"""

def extract_name_from_email(email):
    """Extracts a name from an email address."""
    local_part = email.split('@')[0]
    name_parts = local_part.split('.')
    name = ' '.join(part.title() for part in name_parts)
    return name

def main():
    email_to_name = {}

    email = input("Email: ").strip()
    while email:
        name = extract_name_from_email(email)
        response = input(f"Is your name {name}? (Y/n) ").strip().lower()

        if response in ['', 'y']:
            email_to_name[email] = name
        else:
            name = input("Name: ").strip()
            email_to_name[email] = name

        email = input("Email: ").strip()

    print()
    for email, name in email_to_name.items():
        print(f"{name} ({email})")
main()