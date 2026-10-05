#Old McDonald's Farm

# Step 1: Create the Farm Class
class Farm:
    
    # Step 2: Implement the __init__ Method
    def __init__(self, farm_name):
        self.name = farm_name
        self.animals = {}

    # Step 3: Implement the add_animal Method
    def add_animal(self, animal_type, count=1):
        if animal_type in self.animals:
            self.animals[animal_type] += count
        else:
            self.animals[animal_type] = count

    # Step 4: Implement the get_info Method
    def get_info(self):
        # Start the output string with the farm's name
        info_string = f"{self.name}'s farm\n"
        
        # Add a line for each animal and its count
        for animal, count in self.animals.items():
            info_string += f"{animal} : {count}\n"
            
        # Add the final E-I-E-I-0! phrase, with proper indentation
        info_string += "    E-I-E-I-0!"
        
        return info_string
    
    # Step 6: Implement the get_animal_types Method (Bonus)
    def get_animal_types(self):
        return sorted(self.animals.keys())

    # Step 7: Implement the get_short_info Method (Bonus)
    def get_short_info(self):
        animal_types = self.get_animal_types()
        
        # Pluralize animal names based on their count
        formatted_animals = []
        for animal_type in animal_types:
            animal_name = animal_type
            if self.animals[animal_type] > 1:
                # The example output uses "sheeps", so we'll add 's' regardless of grammar
                animal_name += 's' 
            formatted_animals.append(animal_name)
            
        # Join the list of formatted animal names into a human-readable string
        if len(formatted_animals) == 1:
            animals_str = formatted_animals[0]
        elif len(formatted_animals) == 2:
            animals_str = f"{formatted_animals[0]} and {formatted_animals[1]}"
        else:
            last_animal = formatted_animals.pop()
            animals_str = ", ".join(formatted_animals) + f", and {last_animal}"
            
        return f"{self.name}'s farm has {animals_str}."


# Step 5: Test Your Code
# Create a Farm object and add animals as per the example
macdonald = Farm("McDonald")
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')  # Default count is 1
macdonald.add_animal('sheep')  # Incrementing sheep count
macdonald.add_animal('goat', 12)

# Print the full farm info to match the main example
print(macdonald.get_info())

# Bonus: Test the new methods
print("\n--- Bonus Methods ---")
print(f"Animal types: {macdonald.get_animal_types()}")
print(f"Short info: {macdonald.get_short_info()}")