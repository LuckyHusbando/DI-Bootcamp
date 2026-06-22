#W2D2XP

#Exercise 1 - What are you learning?

def display_message():
    print("I am learning about functions in Python.")

display_message()

#Exercise 2  - What is your favorite book?

def favorite_book(title="Sherlock Holmes"):
    print(f"One of my favorite books is {title}.")

favorite_book("War & Peace")

#Exercise 3 - Some Geography

def describe_city(city="Unknown", country="Unknown"):
    print(f"{city} is in {country}.")

describe_city("Madrid", "Spain")
describe_city("Tel Aviv")

#Exercise 4 - Random

import random

def randomizer(number):
    #Check if number within valid range
    random_number = random.randint(1, 100)

    if number == random_number:
        print(f"You picked {number} and the random number {random_number} matched it!")
    else:
        print(f"Sorry, your {number} does not match {random_number}. Try again!")

randomizer(42)

#Exercise 5 - Let's Create Some Personalized Shirts

def make_shirt(size="large", text="I love Python!"):
    print(f"The shirt's size is {size} and the text reads {text}")

make_shirt()
make_shirt("Medium")
make_shirt("Any", "Uh oh, spaghettios!")
make_shirt(size="small", text="Hello!")

#Exercise 6 - Magicians

magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

def show_magicians(magician_names):
    for magician in magician_names:
        print(magician)

def make_great(magician_names):
    for i in range(len(magician_names)):
        magician_names[i] = f"the Great {magician_names[i]}"

magicians_list = ["Harry Houdini", "David Copperfield", "Penn & Teller", "Dynamo"]

print("Original Magicians:")
show_magicians(magicians_list)

print("\nModifying the list...")
make_great(magicians_list)

print("\nGreat Magicians:")
show_magicians(magicians_list)

#Exercise 7 - Temperature Advice

import random

def get_random_temp(season):
    if season == "winter":
        return random.uniform(-10.0, 5.0)
    elif season == "spring":
        return random.uniform(6.0, 20.0)
    elif season == "summer":
        return random.uniform(21.0, 40.0)
    elif season == "autumn":
        return random.uniform(5.0, 20.0)
    else:
        # Fallback range if something goes wrong
        return random.uniform(-10.0, 40.0)

current_temp = get_random_temp()

print(f"The current random temperature is: {current_temp}°C")

def main():
    current_temp = get_random_temp()
    print(f"The temperature right now is {current_temp} degrees Celcius.")
    if current_temp <= 0:
        print("Brrr, that is freezing! Wear some extra layers today.")
    elif current_temp >= 0 and current_temp <= 16:
        print("Quite chilly! Don’t forget your coat.")
    elif current_temp >= 16 and current_temp <= 23:
        print("Nice weather!")
    elif current_temp >= 24 and current_temp <= 32:
        print("A bit warm, stay hydrated!")
    elif current_temp >= 32 and current_temp <= 40:
        print("It's really hot, stay cool!")

main()
