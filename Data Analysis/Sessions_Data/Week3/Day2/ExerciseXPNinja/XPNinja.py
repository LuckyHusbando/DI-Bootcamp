import time
import os

class BankAccount:
    """A standard bank account with authentication."""

    def __init__(self, username, password):
        self.balance = 0
        self.username = username
        self.password = password
        self.authenticated = False

    def authenticate(self, username, password):
        """Authenticates the user with a username and password."""
        if self.username == username and self.password == password:
            self.authenticated = True
            return True
        return False

    def deposit(self, amount):
        """Adds a positive amount to the balance."""
        if not self.authenticated:
            raise Exception("Authentication required to make a deposit.")
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise Exception("Deposit amount must be a positive number.")
        self.balance += amount
        print(f"Deposited {amount:.2f}. New balance is {self.balance:.2f}")

    def withdraw(self, amount):
        """Deducts a positive amount from the balance."""
        if not self.authenticated:
            raise Exception("Authentication required to make a withdrawal.")
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise Exception("Withdrawal amount must be a positive number.")
        if amount > self.balance:
            raise Exception("Insufficient funds.")
        self.balance -= amount
        print(f"Withdrew {amount:.2f}. New balance is {self.balance:.2f}")


class MinimumBalanceAccount(BankAccount):
    """A bank account with a minimum balance requirement."""

    def __init__(self, username, password, minimum_balance=0):
        super().__init__(username, password)
        self.minimum_balance = minimum_balance

    def withdraw(self, amount):
        """
        Overrides the withdrawal method to enforce a minimum balance.
        """
        if not self.authenticated:
            raise Exception("Authentication required to make a withdrawal.")
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise Exception("Withdrawal amount must be a positive number.")

        if self.balance - amount < self.minimum_balance:
            raise Exception(f"Cannot withdraw. Minimum balance of {self.minimum_balance:.2f} must be maintained.")

        self.balance -= amount
        print(f"Withdrew {amount:.2f}. New balance is {self.balance:.2f}")


# Example of Part I, II & III usage
if __name__ == '__main__':
    account1 = BankAccount("user1", "pass1")
    account2 = MinimumBalanceAccount("user2", "pass2", minimum_balance=50)

    print("--- Testing BankAccount ---")
    account1.authenticate("user1", "pass1")
    account1.deposit(100)
    account1.withdraw(30)
    try:
        account1.withdraw(200)  # This should raise an exception
    except Exception as e:
        print(f"Error: {e}")

    print("\n--- Testing MinimumBalanceAccount ---")
    account2.authenticate("user2", "pass2")
    account2.deposit(100)
    account2.withdraw(40)  # New balance 60, which is > 50
    try:
        account2.withdraw(15)  # New balance 45, which is < 50. This should raise an exception
    except Exception as e:
        print(f"Error: {e}")
        