#Exercise XP - Week 2 Day 6

#Exercise 1 - Cats

class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

# Step 1: Create cat objects
cat1 = Cat("Whiskers", 5)
cat2 = Cat("Shadow", 8)
cat3 = Cat("Mittens", 3)

# Step 2: Create a function to find the oldest cat
def find_oldest_cat(*cats):
    """
    Takes multiple cat objects and returns the oldest one.
    """
    oldest_cat = None
    max_age = -1
    for cat in cats:
        if cat.age > max_age:
            max_age = cat.age
            oldest_cat = cat
    return oldest_cat

# An alternative, more Pythonic way using the max() function
def find_oldest_cat_pythonic(*cats):
    """
    Finds the oldest cat using Python's max() function with a lambda key.
    """
    return max(cats, key=lambda cat: cat.age)

# Step 3: Print the oldest cat's details
oldest = find_oldest_cat_pythonic(cat1, cat2, cat3)
print(f"The oldest cat is {oldest.name}, and is {oldest.age} years old.")
# Expected Output: The oldest cat is Shadow, and is 8 years old.

# Exercise 2 : Dogs

# Step 1: Create the Dog Class

class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def bark(self):
        print(f"{self.name} goes woof!")

    def jump(self):
        jump_height = self.height * 2
        print(f"{self.name} jumps {jump_height} cm high!")

# Step 2: Create Dog Objects
davids_dog = Dog("Rex", 50)
sarahs_dog = Dog("Luna", 40)

# Step 3: Print Dog Details and Call Methods
print(f"David's dog is named {davids_dog.name} and is {davids_dog.height} cm tall.")
davids_dog.bark()
davids_dog.jump()

print("-" * 20)

print(f"Sarah's dog is named {sarahs_dog.name} and is {sarahs_dog.height} cm tall.")
sarahs_dog.bark()
sarahs_dog.jump()

# Step 4: Compare Dog Sizes
print("\n--- Comparing Dog Sizes ---")
if davids_dog.height > sarahs_dog.height:
    print(f"{davids_dog.name} is taller than {sarahs_dog.name}.")
elif sarahs_dog.height > davids_dog.height:
    print(f"{sarahs_dog.name} is taller than {davids_dog.name}.")
else:
    print(f"{davids_dog.name} and {sarahs_dog.name} are the same height.")

# Exercise 3 : Who’s the song producer?

# Step 1: Create the Song Class
class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

# Example usage
stairway = Song(["There’s a lady who's sure", 
                 "all that glitters is gold", 
                 "and she’s buying a stairway to heaven"])

stairway.sing_me_a_song()
# Expected Output:
# There’s a lady who's sure
# all that glitters is gold
# and she’s buying a stairway to heaven

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