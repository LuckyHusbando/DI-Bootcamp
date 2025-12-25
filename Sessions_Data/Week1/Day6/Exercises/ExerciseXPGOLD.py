#Exercise XP Gold

# Create a dictionary of birthdays
birthdays = {
    "John": "1990/05/15",
    "Jane": "1988/11/22",
    "Peter": "1995/03/10",
    "Sarah": "1992/08/30",
    "David": "1985/07/01"
}

# Print a welcome message and instructions
print("Welcome to the birthday lookup program!")
print("You can look up the birthdays of the following people:")
print(", ".join(birthdays.keys()))

# Ask the user for a person's name
person_name = input("\nPlease enter a person's name: ")

# Check if the name is in the dictionary and print the birthday
if person_name in birthdays:
    birthday = birthdays[person_name]
    print(f"\n{person_name}'s birthday is on {birthday}.")
else:
    print(f"\nSorry, I don't have the birthday for {person_name}.")

#Exercise 2 - Birthdays

# Create a dictionary of birthdays
birthdays = {
    "John": "1990/05/15",
    "Jane": "1988/11/22",
    "Peter": "1995/03/10",
    "Sarah": "1992/08/30",
    "David": "1985/07/01"
}

# Print a welcome message and list all the names
print("Welcome to the birthday lookup program!")
print("Here are the people whose birthdays we have:")
print(", ".join(birthdays.keys()))

# Ask the user for a person's name
person_name = input("\nPlease enter a person's name: ")

# Check if the name is in the dictionary and print the appropriate message
if person_name in birthdays:
    birthday = birthdays[person_name]
    print(f"\n{person_name}'s birthday is on {birthday}.")
else:
    print(f"\nSorry, we don’t have the birthday information for {person_name}.")

#Exercise 3 - Add Your Own Birthday

# Create a dictionary of birthdays
birthdays = {
    "John": "1990/05/15",
    "Jane": "1988/11/22",
    "Peter": "1995/03/10",
    "Sarah": "1992/08/30",
    "David": "1985/07/01"
}

# --- Add a new birthday to the dictionary ---
print("Would you like to add a new birthday to our list?")
new_name = input("Enter the person's name: ")
new_birthday = input(f"Enter {new_name}'s birthday (YYYY/MM/DD): ")

# Add the new data to the dictionary
birthdays[new_name] = new_birthday
print(f"\nThank you! The birthday for {new_name} has been added.")

# --- Look up a birthday in the updated dictionary ---
print("\n--- Birthday Lookup ---")
print("Here are the people whose birthdays we have:")
print(", ".join(birthdays.keys()))

# Ask the user for a person's name to look up
person_name = input("\nPlease enter a person's name to look up: ")

# Check if the name is in the dictionary and print the appropriate message
if person_name in birthdays:
    birthday = birthdays[person_name]
    print(f"\n{person_name}'s birthday is on {birthday}.")
else:
    print(f"\nSorry, we don’t have the birthday information for {person_name}.")

#Exercise 4 - Fruit Shop

# Task 1: Print items and prices from a simple dictionary

items = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

print("--- Task 1: Items and Prices ---")
for item, price in items.items():
    print(f"The price of a {item} is ${price}.")

print("\n") # Add a blank line for separation

# Task 2: Calculate total cost from a nested dictionary

items_with_stock = {
    "banana": {"price": 4 , "stock":10},
    "apple": {"price": 2, "stock":5},
    "orange": {"price": 1.5 , "stock":24},
    "pear": {"price": 3 , "stock":1}
}

total_cost = 0

print("--- Task 2: Total Cost of All Stock ---")
# Loop through the values of the outer dictionary, which are the inner dictionaries
for item_data in items_with_stock.values():
    price = item_data["price"]
    stock = item_data["stock"]
    
    # Calculate the cost for the current item and add it to the total
    item_total = price * stock
    total_cost += item_total
    
print(f"The total cost to buy everything in stock is: ${total_cost}")