#Exercise 1 - Cars

import collections

# --- Part 1: Initial String to List Conversion and Analysis ---

# Copy the string into a variable
manufacturers_string = "Volkswagen, Toyota, Ford Motor, Honda, Chevrolet"

# Convert the string into a list
manufacturers_list = [name.strip() for name in manufacturers_string.split(',')]

# Print the number of manufacturers
print("--- Initial Analysis ---")
print(f"There are {len(manufacturers_list)} manufacturers in the list.")

# Print the list in reverse alphabetical order (Z-A)
manufacturers_list.sort(reverse=True)
print(f"Manufacturers in reverse order: {manufacturers_list}")

# Find names with the letter 'o'
o_count = sum(1 for name in manufacturers_list if 'o' in name.lower())
print(f"Number of manufacturers' names with the letter 'o': {o_count}")

# Find names without the letter 'i'
no_i_count = sum(1 for name in manufacturers_list if 'i' not in name.lower())
print(f"Number of manufacturers' names without the letter 'i': {no_i_count}")

# --- Bonus 1: Remove Duplicates ---

print("\n--- Bonus 1: Handling Duplicates ---")
duplicates_list = ["Honda", "Volkswagen", "Toyota", "Ford Motor", "Honda", "Chevrolet", "Toyota"]

# Convert the list to a set to remove duplicates, then convert it back to a list
unique_manufacturers = sorted(list(set(duplicates_list)))

# Join the list into a comma-separated string
unique_manufacturers_string = ", ".join(unique_manufacturers)
print(f"Companies without duplicates: {unique_manufacturers_string}")
print(f"There are now {len(unique_manufacturers)} companies in the list.")

# --- Bonus 2: Ascending Order with Reversed Names ---

print("\n--- Bonus 2: Reversed Names ---")
# Sort the unique list in ascending order (A-Z)
unique_manufacturers.sort()

# Create a new list with each manufacturer's name reversed
reversed_names = [name[::-1] for name in unique_manufacturers]

print(f"Manufacturers in ascending order with reversed names: {reversed_names}")