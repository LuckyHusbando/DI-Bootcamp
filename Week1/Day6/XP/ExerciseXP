#Exercise XP (Mandatory)

#Exercise 1

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

# Use the zip() function to pair the keys and values,
# then convert the result to a dictionary using dict()
result_dict = dict(zip(keys, values))

print(result_dict)

#Exercise 2

def calculate_and_print_costs(family_data):
    """
    Calculates and prints the ticket price for each family member
    and the total cost.
    """
    total_cost = 0

    print("\n--- Calculating Ticket Costs ---")
    for name, age in family_data.items():
        if age < 3:
            price = 0
            print(f"{name.capitalize()} ({age} years old): Free")
        elif 3 <= age <= 12:
            price = 10
            print(f"{name.capitalize()} ({age} years old): ${price}")
        else: # age > 12
            price = 15
            print(f"{name.capitalize()} ({age} years old): ${price}")
        
        total_cost += price

    print(f"\nTotal cost for the family: ${total_cost}")
    print("-" * 30)
    return total_cost

# --- Main Program ---

# Part 1: Calculate cost for the predefined family data
family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
calculate_and_print_costs(family)

# Part 2: Allow user to input family members
user_family = {}
print("\n--- Bonus: Enter family members and ages ---")
print("Enter 'done' for the name when finished.")

while True:
    name = input("Enter a family member's name: ").strip()
    if name.lower() == 'done' or name == '':
        break
    
    try:
        age_str = input(f"Enter {name}'s age: ")
        age = int(age_str)
        user_family[name] = age
    except ValueError:
        print("Invalid age. Please enter a number.")
        continue

if user_family:
    calculate_and_print_costs(user_family)
else:
    print("\nNo family members entered. Exiting bonus section.")

#Exercise 3

# Create the dictionary with the provided data
brand = {
    'name': 'Zara',
    'creation_date': 1975,
    'creator_name': 'Amancio Ortega Gaona',
    'type_of_clothes': ['men', 'women', 'children', 'home'],
    'international_competitors': ['Gap', 'H&M', 'Benetton'],
    'number_stores': 7000,
    'major_color': {
        'France': 'blue',
        'Spain': 'red',
        'US': ['pink', 'green']
    }
}

print("Original Dictionary:")
print(brand)
print("-" * 30)

# 1. Change the value of number_stores to 2
brand['number_stores'] = 2
print(f"1. New number_stores value: {brand['number_stores']}")

# 2. Print a sentence describing Zara’s clients
clients = ", ".join(brand['type_of_clothes'])
print(f"2. Zara's clients include clothes for: {clients}.")

# 3. Add a new key country_creation with the value Spain
brand['country_creation'] = 'Spain'
print(f"3. Dictionary after adding 'country_creation': {brand}")

# 4. Check if international_competitors exists and, if so, add "Desigual"
if 'international_competitors' in brand:
    brand['international_competitors'].append('Desigual')
    print(f"4. 'Desigual' added to competitors: {brand['international_competitors']}")

# 5. Delete the creation_date key
del brand['creation_date']
print(f"5. Dictionary after deleting 'creation_date': {brand}")

# 6. Print the last item in international_competitors
last_competitor = brand['international_competitors'][-1]
print(f"6. The last item in international_competitors is: {last_competitor}")

# 7. Print the major colors in the US
us_colors = brand['major_color']['US']
print(f"7. The major colors in the US are: {us_colors}")

# 8. Print the number of keys in the dictionary
num_keys = len(brand)
print(f"8. The number of keys in the dictionary is: {num_keys}")

# 9. Print all keys of the dictionary
all_keys = list(brand.keys())
print(f"9. All keys of the dictionary are: {all_keys}")

# --- Extra ---
print("\n" + "=" * 15 + " Bonus Section " + "=" * 15)

# Create another dictionary
more_on_zara = {
    'creation_date': 1975,
    'number_stores': 7000
}

# Merge the two dictionaries
brand.update(more_on_zara)

print("Merged dictionary after bonus update:")
print(brand)

#Exercise 4

# The given list of characters
users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]

# 1. Create a dictionary that maps characters to their indices
dict1 = {character: index for index, character in enumerate(users)}
print(f"1. Characters mapped to indices:\n{dict1}\n")

# 2. Create a dictionary that maps indices to characters
dict2 = {index: character for index, character in enumerate(users)}
print(f"2. Indices mapped to characters:\n{dict2}\n")

# 3. Create a dictionary where characters are sorted alphabetically and mapped to their indices
sorted_users = sorted(users)

# Then, use a dictionary comprehension with enumerate() on the sorted list.
dict3 = {character: index for index, character in enumerate(sorted_users)}
print(f"3. Sorted characters mapped to indices:\n{dict3}")

