#Exercise XP - Week 2 Day 6

# Exercise 4 : Afternoon at the Zoo

# Step 1: Define the Zoo Class
class Zoo:
    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.animals = []
        self.grouped_animals = {}

    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)
            print(f"{new_animal} has been added to the zoo.")
        else:
            print(f"{new_animal} is already in the zoo.")

    def get_animals(self):
        if not self.animals:
            print("The zoo is empty.")
        else:
            print("Animals in the zoo:")
            for animal in self.animals:
                print(f"- {animal}")

    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
            print(f"{animal_sold} has been sold.")
        else:
            print(f"Sorry, {animal_sold} is not in the zoo.")

    def sort_animals(self):
        # Sort the animals list alphabetically
        self.animals.sort()
        
        # Group the animals into a dictionary
        self.grouped_animals = {}
        for animal in self.animals:
            first_letter = animal[0].upper()
            if first_letter not in self.grouped_animals:
                self.grouped_animals[first_letter] = []
            self.grouped_animals[first_letter].append(animal)
        
        print("Animals have been sorted and grouped.")

    def get_groups(self):
        if not self.grouped_animals:
            print("Please run sort_animals() first to group the animals.")
            return

        print("\n--- Animal Groups ---")
        for letter, animal_list in self.grouped_animals.items():
            print(f"{letter}: {animal_list}")

# Step 2: Create a Zoo instance
brooklyn_safari = Zoo("Brooklyn Safari")

# Step 3: Call the Zoo methods
print("--- Adding Animals ---")
brooklyn_safari.add_animal("Giraffe")
brooklyn_safari.add_animal("Bear")
brooklyn_safari.add_animal("Baboon")
brooklyn_safari.add_animal("Lion")
brooklyn_safari.add_animal("Zebra")
brooklyn_safari.add_animal("Cougar")
brooklyn_safari.add_animal("Cat")
brooklyn_safari.add_animal("Baboon") # Test for duplicate

print("\n--- Current Animals ---")
brooklyn_safari.get_animals()

print("\n--- Selling an Animal ---")
brooklyn_safari.sell_animal("Bear")

print("\n--- Animals After Selling ---")
brooklyn_safari.get_animals()

print("\n--- Sorting and Grouping Animals ---")
brooklyn_safari.sort_animals()

print("\n--- Displaying Groups ---")
brooklyn_safari.get_groups()

#end