#W2D6DC

class Farm:
    def __init__(self, farm_name):
        # Step 2: Initialize name and empty animals dictionary
        self.name = farm_name
        self.animals = {}

    def add_animal(self, animal_type=None, count=1, **kwargs):
        # Step 3: Handle single animal additions via positional arguments
        if animal_type:
            self.animals[animal_type] = self.animals.get(animal_type, 0) + count
        
        # Step 8: Handle multiple animal additions via **kwargs
        for animal, qty in kwargs.items():
            self.animals[animal] = self.animals.get(animal, 0) + qty

    def get_info(self):
        # Step 4: Display farm info with column alignment
        lines = [f"{self.name}'s farm\n"]
        
        if self.animals:
            # Find the maximum string length among animal names to align the colons
            max_len = max(len(animal) for animal in self.animals.keys())
            
            for animal, count in self.animals.items():
                lines.append(f"{animal.ljust(max_len)} : {count}")
                
        lines.append("\n    E-I-E-I-0!")
        return "\n".join(lines)

    def get_animal_types(self):
        # Step 6: Return a sorted list of the keys
        return sorted(self.animals.keys())

    def get_short_info(self):
        # Step 7: Construct the summary string with dynamic pluralization
        types = self.get_animal_types()
        animal_strings = []
        
        for animal in types:
            # Append an "s" if count > 1 (creating "sheeps" as requested by the logic)
            if self.animals[animal] > 1:
                animal_strings.append(f"{animal}s")
            else:
                animal_strings.append(animal)
                
        # Handle formatting based on the number of animal types
        if not animal_strings:
            return f"{self.name}'s farm has no animals."
        elif len(animal_strings) == 1:
            joined_names = animal_strings[0]
        else:
            joined_names = ", ".join(animal_strings[:-1]) + f" and {animal_strings[-1]}"
            
        return f"{self.name}'s farm has {joined_names}."


# ==========================================
# Testing the Code
# ==========================================

# Step 5: Test the basic functionality
macdonald = Farm("McDonald")
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)

print("--- Step 5 Output ---")
print(macdonald.get_info())
print("\n")

# Step 7: Test the short info output
print("--- Step 7 Output ---")
print(macdonald.get_short_info())
print("\n")

# Step 8: Test the upgraded add_animal method with **kwargs
print("--- Step 8 Output ---")
macdonald = Farm("McDonald") # Resetting the farm
macdonald.add_animal(cow=5, sheep=2, goat=12)
print(macdonald.get_info())