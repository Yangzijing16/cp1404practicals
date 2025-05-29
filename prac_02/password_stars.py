def get_password():
    password = input("Enter password: ")
    while len(password) < 6:
        print("Password too short")
        password = input("Enter password: ")
    return password

def main():
    password = get_password()
    print("*" * len(password))

main()