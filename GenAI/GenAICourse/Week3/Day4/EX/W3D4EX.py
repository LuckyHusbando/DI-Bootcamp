# #W3D4EX

# 🌟 Exercise 1: Currencies

class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    # String representation for print() and str()
    def __str__(self):
        # Adding an 's' to pluralize the currency name for the output
        return f"{self.amount} {self.currency}s"

    # String representation for debugging and repr()
    def __repr__(self):
        return f"'{self.amount} {self.currency}s'"

    # Conversion to integer
    def __int__(self):
        return self.amount

    # Handles addition (c1 + c2) or (c1 + 5)
    def __add__(self, other):
        if isinstance(other, int):
            return self.amount + other
        elif isinstance(other, Currency):
            if self.currency != other.currency:
                raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
            return self.amount + other.amount
        else:
            raise TypeError("Unsupported operand type")

    # Handles in-place addition (c1 += 5) or (c1 += c2)
    def __iadd__(self, other):
        if isinstance(other, int):
            self.amount += other
        elif isinstance(other, Currency):
            if self.currency != other.currency:
                raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
            self.amount += other.amount
        return self


# --- Testing the code ---
c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)

print(c1)          # 5 dollars
print(int(c1))     # 5
print(repr(c1))    # '5 dollars'
print(c1 + 5)      # 10
print(c1 + c2)     # 15
print(c1)          # 5 dollars

c1 += 5
print(c1)          # 10 dollars

c1 += c2
print(c1)          # 20 dollars

# print(c1 + c3) 
# Uncommenting the above will raise: 
# TypeError: Cannot add between Currency type <dollar> and <shekel>

# 🌟 Exercise 2: Import
# Goal: Create a module with a function and import it into another file.

# func.py
def sum_and_print(num1, num2):
    result = num1 + num2
    print(f"The sum of {num1} and {num2} is {result}")

# exercise_one.py
# from func import sum_and_print

# Calling the imported function
sum_and_print(15, 27)

# 🌟 Exercise 3: String module

import string
import random

def generate_random_string():
    # Step 2: Get a string of all letters
    all_letters = string.ascii_letters 
    
    random_chars = []
    
    # Step 3: Loop 5 times to select a random character
    for _ in range(5):
        random_chars.append(random.choice(all_letters))
        
    # Concatenate the characters into a single string
    random_string = "".join(random_chars)
    print(f"Random string: {random_string}")

generate_random_string()

# 🌟 Exercise 4: Current Date

import datetime

def display_current_date():
    # Get the current date
    today = datetime.date.today()
    
    # Display the date
    print(f"Today's date is: {today}")

display_current_date()

# 🌟 Exercise 5: Amount of time left until January 1st

import datetime

def time_until_new_year():
    # Step 2: Get current date and time
    now = datetime.datetime.now()
    
    # Step 3: Create datetime object for Jan 1st of next year
    next_year = now.year + 1
    new_year_date = datetime.datetime(next_year, 1, 1)
    
    # Step 4: Calculate the difference
    time_left = new_year_date - now
    
    # Step 5: Display the difference
    print(f"Time left until January 1st: {time_left}")

time_until_new_year()

# 🌟 Exercise 6: Birthday and minutes

time_until_new_year()

import datetime

def minutes_lived(birthdate_str):
    # Defining the format we expect: YYYY-MM-DD
    date_format = "%Y-%m-%d"
    
    try:
        # Convert string to a datetime object
        birthdate = datetime.datetime.strptime(birthdate_str, date_format)
        
        # Get the current time
        now = datetime.datetime.now()
        
        # Get the time difference
        time_difference = now - birthdate
        
        # Calculate total minutes lived
        # .total_seconds() gets the entire difference in seconds, then we divide by 60
        minutes = int(time_difference.total_seconds() / 60)
        
        print(f"Since your birthdate on {birthdate_str}, you have lived approximately {minutes:,} minutes!")
        
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")

# Example usage:
minutes_lived("1995-08-25")

# 🌟 Exercise 7: Faker Module
# Goal: Use the faker module to generate fake user data and store it in a list of dictionaries.

# Step 2: Import the faker module
from faker import Faker

# Initialize the Faker instance
faker = Faker()

# Step 3: Create an empty list of users
users = []

# Step 4: Create a function to add users
def generate_fake_users(number_of_users):
    for _ in range(number_of_users):
        user_dict = {
            "name": faker.name(),
            "address": faker.address(),
            "language_code": faker.language_code()
        }
        users.append(user_dict)

# Step 5: Call the function and print the users list
generate_fake_users(5)

# Printing nicely using a loop
for idx, user in enumerate(users, 1):
    print(f"User {idx}:")
    print(f"  Name: {user['name']}")
    print(f"  Address: {user['address'].replace(chr(10), ', ')}") # replaces newline with comma for cleaner output
    print(f"  Language Code: {user['language_code']}")
    print("-" * 30)