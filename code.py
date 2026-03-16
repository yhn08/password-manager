import json

def load_passwords():
    try:
        with open ("passwords.json", "r") as r: 
            passwords = json.load(r)
            return passwords
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        return {}

passwords = load_passwords()


def save_passwords(passwords):
    with open("passwords.json", "w") as w:
        #data = json.dumps(passwords)
        #w.write(data)
        json.dump(passwords, w)




while True:
    print("=== Password Manager ===")
    print("1. Add password")
    print("2. Get password")
    print("3. List all services")
    print("4. Delete password")
    print("5. Exit")

    choice = input("\nInput the chosen number:")

    if choice == "1":
        print("You chose to add the password")
        service = input("Enter the service name: ")
        password = input("Enter the password: ")
        passwords[service] = password
        save_passwords(passwords)
        print(f"Password saved for {service}!")
    elif choice == "2":
        print("You chose to get the password")
        service = input("Enter the service name: ")
        if service in passwords:
            print(f"The password for {service} is {passwords[service]}")
        else:
            print("No password for that service found")
    elif choice == "3":
        print("You chose list all services")
        if passwords:
            print("\nYour saved services")
            for service in passwords:
                print(f"- {service}")
        else:
            print("No passwords saved yet!")
    elif choice == "4":
        print("You chose to delete the password")
        service = input("Enter the service name: ")
        password = input("Enter the password: ")
        if service in passwords and passwords[service] == password:
            del passwords[service]
            save_passwords(passwords)
            print(f"Deleted service and password for {service}")
        else:
            print("No service service found or password does not match the password inside the password manager")
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice!")