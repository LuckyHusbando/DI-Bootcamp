#W1D4EX

#Exercise 1: Favorite Numbers

my_fav_numbers = {7, 42, 25, 38, 54, 99}
my_fav_numbers.add(8)
my_fav_numbers.add(32)
my_fav_numbers.remove(32)
friend_fav_numbers = {33, 88, 43, 95, 23, 11}
our_fav_numbers = my_fav_numbers | friend_fav_numbers
print(our_fav_numbers)

#Exercise 2: Tuple

Tuple1 = (5, 2, 3, 8, 6)
#Tuple1.add(4) Result: Error - Tuples cannot be modified.

#Exercise 3: List Manipulation

basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana")
basket.remove("Blueberries")
basket.append("Kiwi")
basket.insert(1, "Apples")
basket.count("Apples")
basket.clear()
print(basket)

#Exercise 4: Floats

# A Float is a number with a demical. An integer is a number that is rounded and has no decimel, while a float does have a decimal.
MyList = [1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]
print(MyList)

#Exercise 5: For Loop

for i in range(1, 21):
    print(i)

for b in range(2, 21, 2):
    print(b)

#Exercise 6: While Loop

while True:
    user_input = (input("Please enter your name: "))

    if user_input.isdigit() or len(user_input) < 3:
        print("Invalid input. A name cannot be numbers and must be at least 3 letters. Please try again.")
    else:
        print("Thank you!")
    break

#Exercise 7: Favorite Fruits

fruit_input = (input("Please enter your favorite fruit, separated by spaces: "))
favorite_fruits = fruit_input.split()
chosen_fruit = (input("Please name any type of fruit: "))

if chosen_fruit.lower() in [fruit.lower() for fruit in favorite_fruits]:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you like it!")

#Exercise 8: Pizza Toppings

base_price = 10.00
topping_cost = 2.50
toppings_list = []

print("Welcome to the Pizza Builder! Enter 'quit' when you are finished adding toppings.\n")

while True:
    topping = input("Enter a pizza topping: ").strip()
    if topping.lower() == "quit":
        break

    toppings_list.append(topping)
    print(f"Adding {topping} to your pizza.\n")

    if not topping:
        print("Please type a valid topping name.\n")
        continue

    formatted_topping = topping.title()

    if formatted_topping in toppings_list:
        print(f"You already added {formatted_topping}! Double toppings aren't allowed.\n")
        continue

total_cost = base_price + (len(toppings_list) * topping_cost)

print("--- Your Order Summary ---")
if toppings_list: 
    print("Toppings added:")
    for t in toppings_list:
        print(f" - {t}")
else:
    print("Toppings added: None (Plain Cheese)")

print(f"Total Cost: ${total_cost:.2f}")

#Exercise 9: Cinemax Tickets

# Initialize the total cost counter and a ticket counter
total_cost = 0
ticket_count = 0

print("Welcome to the Movie Theater Ticket Calculator!")
print("Enter the age of each person. Type 'done' when you are finished.\n")

while True:
    # 1. Ask for input
    user_input = input("Enter age: ").strip()
    
    # 2. Check if the user is finished entering ages
    if user_input.lower() == 'done':
        break
        
    # 3. Validate that the input is a valid positive number
    if not user_input.isdigit():
        print("Invalid input. Please enter a valid number for age, or 'done' to finish.\n")
        continue
        
    # Convert string input to an integer
    age = int(user_input)
    ticket_count += 1
    
    # 4. Determine ticket price based on age rules
    if age < 3:
        price = 0
        print(f"Ticket {ticket_count}: Age {age} -> Free!")
    elif 3 <= age <= 12:
        price = 10
        print(f"Ticket {ticket_count}: Age {age} -> $10")
    else:
        price = 15
        print(f"Ticket {ticket_count}: Age {age} -> $15")
        
    # Add the ticket price to the running total
    total_cost += price
    print(f"Current Total: ${total_cost}\n")

# 5. Print final receipt summary
print("--- Final Ticket Summary ---")
print(f"Total Tickets Issued: {ticket_count}")
print(f"Total Amount Due:     ${total_cost}")

#Bonus

# Initialize lists to track our attendees
allowed_ages = []
denied_count = 0

print("Welcome to the Cinema Check-In!")
print("This movie is strictly restricted to ages 16 to 21 inclusive.")
print("Enter the ages of your group. Type 'done' when finished.\n")

while True:
    user_input = input("Enter age of teenager: ").strip()
    
    # 1. Check if finished entering ages
    if user_input.lower() == 'done':
        break
        
    # 2. Validate input is a number
    if not user_input.isdigit():
        print("Invalid entry. Please type a number or 'done'.\n")
        continue
        
    age = int(user_input)
    
    # 3. Filter based on strict bounds (16-21 inclusive)
    if 16 <= age <= 21:
        allowed_ages.append(age)
        print(f"Age {age} added to the group list. ✅\n")
    else:
        denied_count += 1
        print(f"Age {age} is outside the 16-21 restriction. Removed. ❌\n")

# 4. Print the final results

print("--- Final Theater Entry List ---")
if allowed_ages:
    # Sorting the list makes it clean and easy for a ticket taker to read
    allowed_ages.sort()
    print(f"Approved group ages: {allowed_ages}")
    print(f"Total tickets to issue: {len(allowed_ages)}")
else:
    print("No one in the group met the age requirements.")

if denied_count > 0:
    print(f"Note: {denied_count} person(s) were removed from the group.")