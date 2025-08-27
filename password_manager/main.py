from password_manager import auth, storage

def menu(user):
    while True:
        print("\n1. Add credential")
        print("2. View credentials")
        print("3. Logout")
        choice = input("Choose an option: ")

        if choice == '1':
            site = input("Site: ")
            uname = input("Username: ")
            pw = input("Password: ")
            storage.add_credential(user, site, uname, pw)
            print("Credential added!")

        elif choice == '2':
            creds = storage.list_credentials(user)
            if not creds:
                print("No credentials saved.")
            else:
                for c in creds:
                    print(f"Site: {c['site']}, Username: {c['username']}, Password: {c['password']}")

        elif choice == '3':
            print(f"Goodbye, {user.username}!")
            break

        else:
            print("Invalid option.")

def main():
    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            uname = input("New username: ")
            pw = input("Password: ")
            if auth.register(uname, pw):
                print("Registered successfully.")
            else:
                print("Username already exists.")

        elif choice == '2':
            uname = input("Username: ")
            pw = input("Password: ")
            user = auth.login(uname, pw)
            if user:
                print(f"Welcome, {uname}!")
                menu(user)
            else:
                print("Login failed.")

        elif choice == '3':
            print("Exiting program.")
            break

        else:
            print("Invalid option.")

if __name__ == '__main__':
    main()
