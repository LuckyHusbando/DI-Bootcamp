#W2D4DC

#Daily Challenge - Advanced Algorithms

#Here is a python code that generates a list of 20000 random numbers, called list_of_numbers, and a target number.

# import random

# list_of_numbers = [random.randint(0, 10000) for _ in range(20000)]
# target_number   = 3728

#Copy this code, and create a program that finds, within list_of_numbers all the pairs of number that sum to the target number

#Example

#1000 and 2728 sums to the target_number 3728
#1864 and 1864 sums to the target_number 3728

#We use algebra -- y = target_number - x

#Initialize Tracking Structures
#Two containers needed - "seen" and "found_pairs"

import random

def find_sum_pairs():
    #Generate data
    list_of_numbers = [random.randint(0, 10000) for _ in range(20000)]
    target_number   = 3728

    #Setup memory collections
    seen = set()
    found_pairs = set()

    #For loop to check each number one by one

    for num in list_of_numbers:
    #Calculate exact matching piece
        complement = target_number - num

    #Check if we already passed matching piece earlier
        if complement in seen:
            pair = (min(num, complement), max(num, complement))
            found_pairs.add(pair)
            print(f"Found a match: {pair}")

    #Add current number to seen memory bank
        seen.add(num)

    #Print Results

    print(f"Found {len(found_pairs)} unique pairs that sum up to {target_number}:\n")

    for pair in sorted(found_pairs):
        print(f"{pair[0]} and {pair[1]} sums to the target_number {target_number}")

if __name__ == "__main__":
    find_sum_pairs()