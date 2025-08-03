#Exercise XP - Week 2 Day 6

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