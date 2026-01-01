users = []

def show_menu():
    print("\nMENU")
    print("1 - Add user")
    print("2 - List users")
    print("3 - Remove user")
    print("4 - Exit")

while True:
    show_menu()
    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Enter the user name: ")
        users.append(name)
        print("User added!")

    elif choice == "2":
        if not users:
            print("No users registered.")
        else:
            for i, user in enumerate(users, start=1):
                print(f"{i} - {user}")

    elif choice == "3":
        if not users:
            print("No users to remove.")
        else:
            for i, user in enumerate(users, start=1):
                print(f"{i} - {user}")
            try:
                number = int(input("Choose user number to remove: "))
                if 1 <= number <= len(users):
                    removed = users.pop(number - 1)
                    print(f"{removed} removed!")
                else:
                    print("Invalid number.")
            except ValueError:
                print("Please enter a valid number.")

    elif choice == "4":
        print("Exiting program...")
        break

    else:
        print("Invalid option. Try again.")
