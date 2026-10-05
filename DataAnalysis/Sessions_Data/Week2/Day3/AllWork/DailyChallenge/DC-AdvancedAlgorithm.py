#Daily Challenge - Advanced Algorithm

import random

# Provided starter code
list_of_numbers = [random.randint(0, 10000) for _ in range(20000)]
target_number = 3728

def find_sum_pairs(numbers, target):
    """
    Finds all unique pairs of numbers in a list that sum up to a target number.
    This solution uses a set for efficient O(n) lookup.
    """
    found_pairs = []
    seen_numbers = set()

    for number in numbers:
        complement = target - number
        
        # Check if the complement has been seen before
        if complement in seen_numbers:
            # Found a pair! Add it to our list of pairs.
            found_pairs.append((number, complement))
        
        # Add the current number to the set for future lookups
        seen_numbers.add(number)
    
    return found_pairs

# Find the pairs that sum to the target number
pairs = find_sum_pairs(list_of_numbers, target_number)

# Print the results
print(f"Finding pairs that sum to {target_number}...")

if pairs:
    print(f"Found {len(pairs)} pairs:")
    for num1, num2 in pairs:
        print(f"{num1} and {num2} sums to the target_number {target_number}")
else:
    print("No pairs found that sum to the target number.")

#end