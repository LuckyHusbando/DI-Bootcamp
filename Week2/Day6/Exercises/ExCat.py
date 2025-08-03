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