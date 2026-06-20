#W1D6EX

#Exercise 1: Converting Lists into Dictionaries

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

NewDict = dict(zip(keys, values))
print(NewDict)

#Exercise 2: Cinemax #2

family = {"rick": 43, "beth": 13, "morty": 5, "summer": 2}
total_cost = 0

print("---Individual Ticket Prices---")

for name, age in family.items():
    if age < 3:
        price = 0
    elif age <= 12:
        price = 10
    else:
        price = 15

print(f"{name.capitalize()}'s ticket is ${price}.")
total_cost += price

print("\n---Final Bill---")
print(f"Total Family Cost: #{total_cost}")

#Bonus

user_family = {}

print("Let's calculate your movie tickets!")
print("Type 'quit' when you are done adding family members.\n")

while True:
    name = input("Enter family member's name: ")
    if name.lower() == 'quit':
        break

    age = int(input(f"Enter {name}'s age: "))
    user_family[name] = age

total_cost = 0

print("\n ---Individual Ticket Prices---")
for name, age in user_family.items():
    if age <3:
        price = 0
    elif age <= 12:
        price = 10
    else:
        price = 15

    print(f"{name.capitalize()}: ${price}")
    total_cost += price

print("\n---Final Bill---")
print(f"Total Family Cost: ${total_cost}")

#Exercise 3: Zara

# name: Zara
# creation_date: 1975
# creator_name: Amancio Ortega Gaona
# type_of_clothes: men, women, children, home
# international_competitors: Gap, H&M, Benetton
# number_stores: 7000
# major_color: 
#     France: blue, 
#     Spain: red, 
#     US: pink, green

brand = {
    "name": "Zara", 
    "creation_date": 1975, 
    "creator_name": "Amancio Ortega Gaona", 
    "type_of_clothes": ["Men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000, 

    "major_color": {
        "France": "blue",
        "Spain": "red",
        "USA": ["pink", "green"]
        }
    }

brand["number_stores"] = 2
clients = brand["type_of_clothes"]
print(f"Zara's clients include {clients[0]}, {clients[1]}, {clients[2]}, and they also offer items for the {clients[3]}.")
brand["country_creation"] = "Spain"
if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual")
del brand["creation_date"]
competitors = brand["international_competitors"]
print(f"Zara's newest competitor is {competitors[3]}.")
print(brand["major_color"]["USA"])
number_of_keys = len(brand)
print(number_of_keys)
print(brand.keys())

#Bonus

more_on_zara = {
    "creation_date": 1975, 
    "number_stores": 7000 
    }

#Merging

Zara_Complete = brand | more_on_zara
print(Zara_Complete)

#Exercise 4: Disney Characters

users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]

char_to_index = {name: index for index, name in enumerate(users)}
print(char_to_index)

# 2. Create a dictionary that maps indices to characters:

index_to_char = dict(enumerate(users))
print(index_to_char)

# 3. Create a dictionary where characters are sorted alphabetically and mapped to their indices:

sorted_char_to_index = {name: index for index, name in enumerate(sorted(users))}
print(sorted_char_to_index)