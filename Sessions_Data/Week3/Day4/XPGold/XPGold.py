#XP Gold - Week 3 Day 4

#Import Holidays function did not operate due to lack of US reference material.

# from datetime import date
# # import holidays

# def upcoming_holiday():
#     """
#     Displays today's date and the time until the next upcoming holiday.
#     """
#     today = date.today()
#     print(f"Today's date is: {today}")

#     # Initialize a holiday dictionary for the current country (e.g., US)
#     # us_holidays = holidays.US()

#     # Find the next holiday
#     # for holiday_date, name in sorted(us_holidays.items()):
#         # if holiday_date > today:
#             days_until = (holiday_date - today).days
#             print(f"The next holiday is {name} in {days_until} days.")
#             break

# # Example usage
# upcoming_holiday()

# The holidays module provides a dictionary-like object where keys are dates and values are holiday names. We iterate through the sorted list of holidays to find the first one that occurs after today's date.


# Exercise 2: How Old Are You On Jupiter?
# This function calculates a person's age on different planets based on a given age in seconds. The orbital periods for each planet are provided relative to Earth's year.

def age_on_planets(seconds):
    """
    Calculates age on different planets given an age in seconds.
    
    Args:
        seconds (int): The age in seconds.
    """
    earth_year_seconds = 31557600
    
    # Orbital periods in Earth years
    orbital_periods = {
        'Earth': 1.0,
        'Mercury': 0.2408467,
        'Venus': 0.61519726,
        'Mars': 1.8808158,
        'Jupiter': 11.862615,
        'Saturn': 29.447498,
        'Uranus': 84.016846,
        'Neptune': 164.79132
    }

    earth_years = seconds / earth_year_seconds
    
    print(f"Age in seconds: {seconds}")
    print(f"This is equivalent to {earth_years:.2f} Earth years.\n")
    
    for planet, period in orbital_periods.items():
        planet_age = earth_years / period
        print(f"On {planet}, you would be {planet_age:.2f} years old.")

# Example usage
age_on_planets(1000000000)

# The function first calculates the age in Earth years and then uses the provided orbital periods to find the equivalent age on each of the other planets. The f-string formatting with :.2f ensures the output is rounded to two decimal places.


# Exercise 3: Regular Expression #1
# This function uses Python's re module to extract all digits from a string and concatenate them into a single string.

import re

def return_numbers(text):
    """
    Extracts all digits from a string and returns them as a new string.
    
    Args:
        text (str): The input string.
        
    Returns:
        str: A string containing only the digits from the input.
    """
    # Find all sequences of one or more digits
    numbers_list = re.findall(r'\d', text)
    
    # Join the list of digits into a single string
    return "".join(numbers_list)

# Example usage
print(f"The extracted numbers are: {return_numbers('k5k3q2g5z6x9bn')}")

# The regular expression \d matches any digit (0-9). The re.findall() function returns a list of all non-overlapping matches, and "".join() concatenates them.


# Exercise 4: Regular Expression #2
# This code asks the user for their full name and uses regular expressions to validate it against a set of rules.

import re

def validate_name():
    """
    Asks the user for their full name and validates it using regex.
    """
    while True:
        full_name = input("Please enter your full name (e.g., 'John Doe'): ")

        # Regex pattern for validation
        # ^[A-Z]:   Starts with an uppercase letter
        # [a-z]*:   Followed by zero or more lowercase letters
        # \s:       Followed by exactly one space
        # [A-Z]:   Followed by another uppercase letter
        # [a-z]*$:  Followed by zero or more lowercase letters until the end of the string
        pattern = r'^[A-Z][a-z]*\s[A-Z][a-z]*$'

        if re.match(pattern, full_name):
            print("Name is valid.")
            break
        else:
            print("Invalid name. Please follow the rules:")
            print("- Only letters allowed.")
            print("- Exactly one space between names.")
            print("- First letter of each name must be capitalized.")

# Example usage
validate_name()
# The regular expression ^[A-Z][a-z]*\s[A-Z][a-z]*$ is designed to match a string that starts with an uppercase letter, followed by lowercase letters, a single space, another uppercase letter, and then more lowercase letters. This pattern enforces all the rules in a single check.

# Exercise 5: Python Password Generator
# This program generates and validates passwords based on a user-specified length and a set of rules. The code includes a test function to verify that the generated passwords meet the criteria.

import random
import string

def get_valid_length():
    """
    Prompts the user for a password length and validates the input.
    Returns:
        int: A valid password length between 6 and 30.
    """
    while True:
        try:
            length = int(input("Enter password length (6-30 characters): "))
            if 6 <= length <= 30:
                return length
            else:
                print("Password length must be between 6 and 30.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def generate_password(length):
    """
    Generates a password of a specified length with required character types.
    
    Args:
        length (int): The desired length of the password.
        
    Returns:
        str: The generated password.
    """
    digits = string.digits
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    special_chars = "!@#$%^&*"
    all_chars = digits + lowercase + uppercase + special_chars

    # Ensure at least one of each required character type is included
    password = [
        random.choice(digits),
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(special_chars)
    ]
    
    # Fill the rest of the password length with random characters
    if length > 4:
        remaining_length = length - 4
        password.extend(random.choices(all_chars, k=remaining_length))
    
    # Shuffle the list to ensure the required characters aren't always at the start
    random.shuffle(password)
    
    return "".join(password)

def test_password(password, length):
    """
    Tests if a generated password meets all requirements.
    
    Args:
        password (str): The password to test.
        length (int): The expected length of the password.
        
    Returns:
        bool: True if the password is valid, False otherwise.
    """
    if len(password) != length:
        print(f"❌ Length mismatch: Expected {length}, got {len(password)}")
        return False
        
    has_digit = any(char.isdigit() for char in password)
    has_lower = any(char.islower() for char in password)
    has_upper = any(char.isupper() for char in password)
    has_special = any(char in "!@#$%^&*" for char in password)

    if not all([has_digit, has_lower, has_upper, has_special]):
        print("❌ Missing required character type.")
        return False
        
    return True

# Main program flow
if __name__ == '__main__':
    # ------------------ Test function ------------------
    print("--- Running 100 password tests ---")
    for _ in range(100):
        test_length = random.randint(6, 30)
        test_password_str = generate_password(test_length)
        if test_password(test_password_str, test_length):
            print(f"✅ Test passed for password '{test_password_str}' of length {test_length}.")
        else:
            print(f"❌ Test failed for password '{test_password_str}' of length {test_length}.")

    # ------------------ User interaction ------------------
    print("\n--- Password Generator for You ---")
    password_length = get_valid_length()
    new_password = generate_password(password_length)
    
    print(f"\nYour new password is: {new_password}")
    print("Remember to keep your password in a safe place! 🤫")