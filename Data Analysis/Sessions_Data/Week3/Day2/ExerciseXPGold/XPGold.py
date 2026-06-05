# Part I: BankAccount
class BankAccount:
    def __init__(self, username, password):
        self.balance = 0
        self.username = username
        self.password = password
        self.authenticated = False

    def authenticate(self, username, password):
        if self.username == username and self.password == password:
            self.authenticated = True
            return True
        return False

    def deposit(self, amount):
        if not self.authenticated:
            raise Exception("Authentication required to make a deposit.")
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise Exception("Deposit amount must be a positive number.")
        self.balance += amount
        print(f"Deposited {amount}. New balance is {self.balance}")

    def withdraw(self, amount):
        if not self.authenticated:
            raise Exception("Authentication required to make a withdrawal.")
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise Exception("Withdrawal amount must be a positive number.")
        if amount > self.balance:
            raise Exception("Insufficient funds.")
        self.balance -= amount
        print(f"Withdrew {amount}. New balance is {self.balance}")


# Part II: MinimumBalanceAccount
class MinimumBalanceAccount(BankAccount):
    def __init__(self, username, password, minimum_balance=0):
        super().__init__(username, password)
        self.minimum_balance = minimum_balance

    def withdraw(self, amount):
        if not self.authenticated:
            raise Exception("Authentication required to make a withdrawal.")
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise Exception("Withdrawal amount must be a positive number.")
        
        if self.balance - amount < self.minimum_balance:
            raise Exception(f"Cannot withdraw. Minimum balance of {self.minimum_balance} must be maintained.")
        
        self.balance -= amount
        print(f"Withdrew {amount}. New balance is {self.balance}")


# Part IV: BONUS ATM class
class ATM:
    def __init__(self, account_list, try_limit):
        if not isinstance(account_list, list):
            raise Exception("account_list must be a list.")
        for account in account_list:
            if not isinstance(account, (BankAccount, MinimumBalanceAccount)):
                raise Exception("All items in account_list must be instances of BankAccount or MinimumBalanceAccount.")
        self.account_list = account_list

        try:
            if not isinstance(try_limit, int) or try_limit <= 0:
                raise ValueError
            self.try_limit = try_limit
        except (ValueError, TypeError):
            print("Invalid try_limit input. Setting to default of 2.")
            self.try_limit = 2
            
        self.current_tries = 0
        self.show_main_menu()

    def show_main_menu(self):
        while True:
            print("\n--- Main Menu ---")
            print("1. Log in")
            print("2. Exit")
            choice = input("Enter your choice: ")
            
            if choice == '1':
                username = input("Enter username: ")
                password = input("Enter password: ")
                self.log_in(username, password)
            elif choice == '2':
                print("Thank you for using the ATM. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

    def log_in(self, username, password):
        found_account = None
        for account in self.account_list:
            if account.authenticate(username, password):
                found_account = account
                break

        if found_account:
            print("Login successful.")
            self.current_tries = 0
            self.show_account_menu(found_account)
        else:
            self.current_tries += 1
            print("Invalid username or password.")
            if self.current_tries >= self.try_limit:
                print(f"Maximum login attempts ({self.try_limit}) reached. Shutting down.")
                exit()
            print(f"Attempts left: {self.try_limit - self.current_tries}")

    def show_account_menu(self, account):
        while True:
            print(f"\n--- Account Menu for {account.username} ---")
            print(f"Current balance: {account.balance}")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Exit to Main Menu")
            choice = input("Enter your choice: ")
            
            try:
                if choice == '1':
                    amount = float(input("Enter deposit amount: "))
                    account.deposit(amount)
                elif choice == '2':
                    amount = float(input("Enter withdrawal amount: "))
                    account.withdraw(amount)
                elif choice == '3':
                    account.authenticated = False
                    print("Logged out successfully.")
                    break
                else:
                    print("Invalid choice. Please try again.")
            except Exception as e:
                print(f"Error: {e}")


# Example usage:
if __name__ == '__main__':
    account1 = BankAccount("user1", "pass1")
    account2 = MinimumBalanceAccount("user2", "pass2", minimum_balance=50)

    # Creating a list of accounts for the ATM
    accounts = [account1, account2]
    
    # Instantiate the ATM
    my_atm = ATM(accounts, 3) 