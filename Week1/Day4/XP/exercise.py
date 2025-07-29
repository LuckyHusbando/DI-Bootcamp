#Exercise 1 - Favorite Numbers

my_fav_numbers = {8, 2, 48, 23, 48, 42, 31, 20}
my_fav_numbers.add(34)
my_fav_numbers.add(84)
my_fav_numbers.remove(84)

friend_fav_numbers = {82, 53, 72, 91, 24, 62, 3}
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
print(our_fav_numbers)

#Exercise 2 - Tuples

my_tuple = (34, 56, 24, 43, 59)
#Tuples cannot be edited by commands under normal circumstances.

#Exercise 3 - List Manipulation

basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana")
basket.remove("Blueberries")
basket.append("Kiwi")
basket.insert(1, "Apples")
basket.count("Apples")
basket.clear
print(basket)

#Exercise 4 - Floats

#A float is a real number that contains a fractional park, like including a decimal point.
#This is different from an integer which is simply a whole number.

My_Floats = [1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]
print(My_Floats)

#Exercise 5 - For Loop

Test_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
for num in Test_numbers:
    print(num)

for index, element in enumerate(Test_numbers):
    if index % 2 == 0:
        print(f'Index: {index}, Element: {element}')

#Exercise 6 - While Loop

my_name = "Derek"
user_name = ""

while user_name != my_name:
    user_name = input("Please enter your real name: ")

print(f"Hello, {my_name}! You have entered the correct name!")

#Exercise 7 - Favorite Fruits

# Ask the user for their favorite fruits
favorite_fruits_input = input("What are your favorite fruits? Please separate them with spaces: ")

# Store these fruits in a list
favorite_fruits = favorite_fruits_input.lower().split()

# Ask the user to input the name of any fruit
chosen_fruit = input("Enter the name of any fruit: ").lower()

# Check if the chosen fruit is in their list of favorite fruits
if chosen_fruit in favorite_fruits:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy it!")

#Exercise 8 - Pizza Toppings

toppings = []
base_price = 10.00
topping_cost = 2.50

print("Let's build your pizza! Enter toppings one-by-one. Type 'quit' when you are finished.")

while True:
    topping = input("Enter a topping: ").lower()
    if topping == 'quit':
        break
    else:
        toppings.append(topping)
        print(f"Adding {topping} to your pizza.")

print("\n---") #Horizontal line for better readability. 

print("\nYour pizza will have the following toppings:")
for topping in toppings:
    print(f"- {topping.title()}")

total_cost = base_price + (len(toppings) * topping_cost)
print(f"\nTotal cost of your pizza: ${total_cost:.2f}")

#Exercise 9 - Cinemax Tickets

total_cost = 0

print("Enter the age of each family member. Type 'done' when finished.")

while True:
    age_input = input("Enter age (or 'done'): ")
    if age_input.lower() == 'done':
        break

    try:
        age = int(age_input)
        if age < 0: 
            print("Age cannot be negative. Please enter a valid age.")
            continue

        if age < 3:
            print("Ticket: Free.")
        elif 3 <= age <= 12:
            total_cost += 10
            print("Ticket: $10")
        else:
            total_cost += 15
            print("Ticket: $15")
    except ValueError:
        print("Invalid input. Please enter a number for age or 'done'.")

print(f"\nTotal ticket cost for the family: ${total_cost}")

#Bonus

attendees = []
print("Enter the age of each person. Type 'done' when finished.")

while True:
    age_input = input("Enter age (or 'done'): ")
    if age_input.lower() == 'done':
        break

    try:
        age = int(age_input)
        if age < 0:
            print("Age cannot be negative. Please enter a valid age.")
            continue
        attendees.append(age)
    except Valueerror:
        print("Invalid input. Please enter a number for age or 'done'.")

#This is for filtering out people who are not allowed to watch. Viewers must be 16-21.

allowed_attendees = []
for age in attendees:
    if 16 <= age <= 21:
        allowed_attendees.append(age)

if allowed_attendees:
    print("\nThe following people are allowed to watch the movie.")
    for age in allowed_attendees:
        print(f"- Age: {age}")
else:
    print("\nNo one in the group is allowed to watch the movie.")

#Exercise 10 - Sandwich Orders

sandwich_orders = ["Tuna", "Pastrami", "Avocado", "Pastrami", "Egg", "Chicken", "Pastrami"]
finished_sandwiches = []

print("We're sorry, but the deli has run out of Pastrami.")

#Remove all instances of "Pastrami":
while "Pastrami" in sandwich_orders:
    sandwich_orders.remove("Pastrami")

#Prepare sandwiches
while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0) #Get the first sandwich in the list
    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\n---")

print("\nHere are all the sandwiches that were made: ")
for sandwich in finished_sandwiches:
    print(f"- {sandwich}")

    