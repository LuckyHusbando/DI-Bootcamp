#Challenge Series 2

# Exercise 1

# Pattern 1: Isosceles Triangle

rows1 = 3
print("Pattern 1:")
for i in range(rows1):
    # Print leading spaces
    print(' ' * (rows1 - i - 1), end='')
    # Print asterisks
    print('*' * (2 * i + 1))


# Pattern 2: Right-aligned Triangle

rows2 = 5
print("\nPattern 2:")
for i in range(rows2):
    # Print leading spaces
    print(' ' * (rows2 - i - 1), end='')
    # Print asterisks
    print('*' * (i + 1))


# Pattern 3: Increasing and Decreasing Triangle

rows3 = 5
print("\nPattern 3:")

# Part 1: Increasing triangle
for i in range(rows3):
    print('*' * (i + 1))

# Part 2: Decreasing triangle (with a small modification for the top line)
# The user's example shows the top line of the decreasing triangle having the same number of stars as the bottom of the increasing one.
for i in range(rows3):
    # Print leading spaces
    print(' ' * i, end='')
    # Print asterisks
    print('*' * (rows3 - i))

# Exercise 2

# This code attempts to implement the Selection Sort algorithm. The goal of Selection Sort is to sort a list of elements in ascending order. 
# It works by repeatedly finding the minimum element from the unsorted part of the list and swapping it with the first unsorted element.

# However, the provided code has a logical flaw in its implementation. It performs a swap inside the inner loop whenever a smaller element is found, 
# rather than waiting for the entire inner loop to complete to find the true minimum for that pass. Despite this inefficiency, in this specific example, 
# the code still manages to produce a sorted list.