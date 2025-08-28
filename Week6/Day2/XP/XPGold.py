def auth_cli_dictionary():
    users = {
        "admin": "password123",
        "user1": "pass_user1",
        "john.doe": "johnnyboy"
    }
    
    logged_in = None

    while True:
        command = input("Enter 'login', 'signup', or 'exit': ").lower()

        if command == "exit":
            print("Exiting...")
            break
        
        if command == "login":
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            
            if username in users and users[username] == password:
                logged_in = username
                print("You are now logged in.")
            else:
                print("Invalid username or password.")
                signup_option = input("Would you like to sign up? (yes/no): ").lower()
                if signup_option == "yes":
                    # Fall through to the signup logic below
                    pass
                else:
                    continue

        if command == "signup":
            while True:
                new_username = input("Choose a new username: ")
                if new_username in users:
                    print("This username already exists. Please choose a different one.")
                else:
                    break
            
            new_password = input("Choose a password: ")
            users[new_username] = new_password
            print("Signup successful! You can now log in.")
            logged_in = new_username
            
    print(f"Final user list: {users}")

# Uncomment the line below to run the dictionary-based CLI
# auth_cli_dictionary()