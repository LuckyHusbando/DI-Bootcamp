#Daily Challenge Day 4 - Gold

import datetime

def is_leap_year(year):
    """Determines if a year is a leap year."""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def display_birthday_cake():
    """Asks for a birthdate, calculates age, and displays a customized cake."""
    
    while True:
        birthdate_str = input("Please enter your birthdate (DD/MM/YYYY): ")
        try:
            birthdate = datetime.datetime.strptime(birthdate_str, "%d/%m/%Y").date()
            break
        except ValueError:
            print("Invalid date format. Please use DD/MM/YYYY.")
    
    today = datetime.date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    
    # Get the last digit of the age for the number of candles
    num_candles = age % 10
    candles_str = 'i' * num_candles
    
    # The cake template
    cake = f"""
       ___{candles_str}___
      |:H:a:p:p:y:|
    __|___________|__
   |^^^^^^^^^^^^^^^^^|
   |:B:i:r:t:h:d:a:y:|
   |                 |
   ~~~~~~~~~~~~~~~~~~~
"""
    
    # Check for the leap year bonus
    birth_year = birthdate.year
    if is_leap_year(birth_year):
        print("\nBecause you were born in a leap year, here are two cakes!")
        print(cake)
        print(cake)
    else:
        print(cake)

# Run the program
if __name__ == "__main__":
    display_birthday_cake()