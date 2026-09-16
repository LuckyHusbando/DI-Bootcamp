#W2D6EX

class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

# Step 1: Create cat objects
cat1 = Cat("Luna", 3)
cat2 = Cat("Garfield", 7)
cat3 = Cat("Milo", 5)

# Step 2: Create a function to find the oldest cat
def find_oldest_cat(c1, c2, c3):
    # max() evaluates the age attribute of each cat and returns the object with the highest value
    return max(c1, c2, c3, key=lambda cat: cat.age)

# Step 3: Print the oldest cat's details
oldest = find_oldest_cat(cat1, cat2, cat3)
print(f"The oldest cat is {oldest.name}, and is {oldest.age} years old.")

class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def bark(self):
        print(f"{self.name} goes woof!")

    def jump(self):
        print(f"{self.name} jumps {self.height * 2} cm high!")

# Step 2: Create Dog Objects
davids_dog = Dog("Rex", 50)
sarahs_dog = Dog("Teacup", 20)

# Step 3: Print Dog Details and Call Methods
for dog in (davids_dog, sarahs_dog):
    print(f"Dog: {dog.name}, Height: {dog.height}cm")
    dog.bark()
    dog.jump()
    print("-" * 20)

# Step 4: Compare Dog Sizes
if davids_dog.height > sarahs_dog.height:
    print(f"{davids_dog.name} is bigger than {sarahs_dog.name}.")
elif sarahs_dog.height > davids_dog.height:
    print(f"{sarahs_dog.name} is bigger than {davids_dog.name}.")
else:
    print(f"{davids_dog.name} and {sarahs_dog.name} are the exact same size.")

class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

stairway = Song([
    "There’s a lady who's sure", 
    "all that glitters is gold", 
    "and she’s buying a stairway to heaven"
])

stairway.sing_me_a_song()

class Zoo:
    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.animals = []
        self.grouped_animals = {} # Dictionary to store the sorted groups

    # Bonus: *new_animals allows passing multiple animals separated by commas
    def add_animal(self, *new_animals):
        for animal in new_animals:
            if animal not in self.animals:
                self.animals.append(animal)

    def get_animals(self):
        print("Animals currently in the zoo:", self.animals)

    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
            print(f"{animal_sold} has been sold.")
        else:
            print(f"{animal_sold} is not in the zoo.")

    def sort_animals(self):
        # First, sort the list alphabetically
        self.animals.sort()
        
        # Reset the dictionary to avoid duplicates if called multiple times
        self.grouped_animals = {}
        
        # Group animals by their first letter
        for animal in self.animals:
            first_letter = animal[0].upper()
            if first_letter not in self.grouped_animals:
                self.grouped_animals[first_letter] = []
            self.grouped_animals[first_letter].append(animal)

    def get_groups(self):
        for letter, animals in self.grouped_animals.items():
            print(f"{letter}: {animals}")


# Step 2: Create a Zoo instance
brooklyn_safari = Zoo("Brooklyn Safari")

# Step 3: Use the Zoo methods
# Testing the *args bonus by adding multiple animals at once
brooklyn_safari.add_animal("Giraffe", "Bear", "Baboon", "Zebra", "Cat", "Cougar", "Lion")

print("--- Initial Animals ---")
brooklyn_safari.get_animals()

print("\n--- Selling Bear ---")
brooklyn_safari.sell_animal("Bear")
brooklyn_safari.get_animals()

print("\n--- Sorted Groups ---")
brooklyn_safari.sort_animals()
brooklyn_safari.get_groups()