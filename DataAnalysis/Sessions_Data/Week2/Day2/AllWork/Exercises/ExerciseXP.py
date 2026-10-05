#Exercise XP Week 2 Day 2

#Exercise 1

# Step 1: Define a function named display_message()
def display_message():
    """
    This function prints a simple message about the current topic.
    """
    # Step 2: Print a message inside the function
    print("I am learning about functions in Python.")

# Step 3: Call the function to execute the code
display_message()

#Exercise 2

# Step 1: Define a function named favorite_book() that accepts one parameter, title.
def favorite_book(title):
    """
    This function displays a message about a favorite book.
    """
    # Step 2: Print a message that includes the title.
    print(f"One of my favorite books is {title}.")

# Step 3: Call the favorite_book() function with a book title as an argument.
favorite_book("Alice in Wonderland")

# Example with a different book title
favorite_book("The Lord of the Rings")

#Exercise 3

# Step 1: Define a function named describe_city() with two parameters,
#         where 'country' has a default value.
def describe_city(city, country="Unknown"):
    """
    This function prints a message describing a city and its country.
    """
    # Step 2: Print a message that includes the city and country.
    print(f"{city} is in {country}.")

# Step 3: Call the function with different combinations of arguments.

# Call with both city and country arguments provided.
describe_city("Reykjavik", "Iceland")

# Call with only the city argument; the country will use the default value.
describe_city("Paris")

# Example with another city and country
describe_city("Tokyo", "Japan")

# Example with another city and default country
describe_city("Sydney")

#Exercise 4

# Step 1: Import the random module
import random

# Step 2: Define a function that accepts a number between 1 and 100 as a parameter
def compare_random_number(user_number):
    """
    Generates a random number and compares it to a number provided by the user.
    """
    # Step 3: Generate a random integer between 1 and 100
    random_number = random.randint(1, 100)

    # Step 4: Compare the two numbers using conditional statements
    if user_number == random_number:
        # If the numbers match, print a success message
        print("Success!")
    else:
        # Otherwise, print a fail message and display both numbers
        print(f"Fail! Your number: {user_number}, Random number: {random_number}")

# Step 5: Call the function with a number between 1 and 100
compare_random_number(50)

# You can call the function with different numbers to test the output
compare_random_number(1)
compare_random_number(99)

#Exercise 5

# Step 1 & 4: Define a function named make_shirt() with parameters and default values.
def make_shirt(size="large", text="I love Python"):
    """
    This function summarizes the size and message of a shirt.
    """
    # Step 2: Print a summary message inside the function.
    print(f"The size of the shirt is {size} and the text is {text}.")

# Step 3 & 5: Call the function in various ways.

# Call to make a large shirt with the default message.
# The function uses the default values for both size and text.
print("1. Calling with default values:")
make_shirt()

# Call to make a medium shirt with the default message.
# The 'medium' argument overrides the default size, but the text remains the default.
print("\n2. Calling with a custom size:")
make_shirt("medium")

# Call to make a shirt of any size with a different message.
# Both default values are overridden by the provided arguments.
print("\n3. Calling with a custom size and message:")
make_shirt("small", "Custom message")

# Step 6 (Bonus): Call the function using keyword arguments.
# This explicitly names the parameters, making the code clearer.
print("\n4. Calling with keyword arguments:")
make_shirt(text="I'm a keyword argument!", size="XL")

#Exercise 6

# Step 1: Create a list of magician names
magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

# Step 2: Create a function to display magicians
def show_magicians(magicians):
    """
    Prints each name from a list of magicians.
    """
    for magician in magicians:
        print(magician)

# Step 3: Create a function to modify the list
def make_great(magicians):
    """
    Adds " the Great" to each magician's name in the list.
    """
    # Loop through the list using the index to modify it in place
    for i in range(len(magicians)):
        magicians[i] = magicians[i] + " the Great"

# Step 4: Call the functions
print("Original magicians:")
show_magicians(magician_names)

# Call make_great() to modify the list
make_great(magician_names)

print("\nGreat magicians:")
# Call show_magicians() to display the modified list
show_magicians(magician_names)

#Exercise 7

import random

# Step 1: Create the get_random_temp() Function
def get_random_temp():
    """Returns a random integer temperature between -10 and 40 degrees Celsius."""
    return random.randint(-10, 40)

def main():
    """
    Generates a random temperature, prints it, and provides advice.
    This version uses the basic integer temperature function.
    """
    # Step 2: Call get_random_temp() and store the result
    temperature = get_random_temp()
    print(f"The temperature right now is {temperature} degrees Celsius.")

    # Step 3: Provide Temperature-Based Advice
    if temperature < 0:
        print("Brrr, that’s freezing! Wear some extra layers today.")
    elif 0 <= temperature < 16:
        print("Quite chilly! Don’t forget your coat.")
    elif 16 <= temperature < 24: # Changed 23 to 24 to align with the next range
        print("Nice weather.")
    elif 24 <= temperature < 32:
        print("A bit warm, stay hydrated.")
    else: # This covers temperatures from 32 to 40
        print("It’s really hot! Stay cool.")

# To run the initial version, uncomment the line below.
# main()

# -------------------------------------------------------------------------
# Step 4 (Bonus): Modify get_random_temp() to return floating-point numbers.
# -------------------------------------------------------------------------
def get_random_temp_float():
    """Returns a random floating-point temperature between -10 and 40 degrees Celsius."""
    return random.uniform(-10, 40)

def main_float():
    """
    Generates a random floating-point temperature, prints it, and provides advice.
    """
    temperature = get_random_temp_float()
    print(f"The temperature right now is {temperature:.1f} degrees Celsius.")

    if temperature < 0:
        print("Brrr, that’s freezing! Wear some extra layers today.")
    elif 0 <= temperature < 16:
        print("Quite chilly! Don’t forget your coat.")
    elif 16 <= temperature < 24:
        print("Nice weather.")
    elif 24 <= temperature < 32:
        print("A bit warm, stay hydrated.")
    else:
        print("It’s really hot! Stay cool.")

# To run the floating-point version, uncomment the line below.
# main_float()

# -------------------------------------------------------------------------
# Step 5 (Bonus): Month-Based Seasons
# -------------------------------------------------------------------------

def get_seasonal_temp_range(month):
    """
    Returns a temperature range (min, max) based on the month.
    Assuming Northern Hemisphere seasons.
    """
    if month in [12, 1, 2]:
        # Winter
        return (-5, 10)
    elif month in [3, 4, 5]:
        # Spring
        return (5, 20)
    elif month in [6, 7, 8]:
        # Summer
        return (25, 40)
    elif month in [9, 10, 11]:
        # Autumn
        return (10, 25)
    else:
        # Invalid month, return a default range
        print("Invalid month entered. Using a default range.")
        return (-10, 40)

def main_seasonal():
    """
    Asks for a month, generates a seasonal temperature, and provides advice.
    """
    try:
        month = int(input("Enter the current month (1-12): "))
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 12.")
        return

    min_temp, max_temp = get_seasonal_temp_range(month)
    temperature = random.uniform(min_temp, max_temp)
    print(f"\nThe temperature right now is {temperature:.1f} degrees Celsius.")

    if temperature < 0:
        print("Brrr, that’s freezing! Wear some extra layers today.")
    elif 0 <= temperature < 16:
        print("Quite chilly! Don’t forget your coat.")
    elif 16 <= temperature < 24:
        print("Nice weather.")
    elif 24 <= temperature < 32:
        print("A bit warm, stay hydrated.")
    else:
        print("It’s really hot! Stay cool.")

# To run the full bonus version, uncomment the line below.
main_seasonal()

#end