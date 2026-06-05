#Challenge Series 1

#Exercise 1

# A sample list
my_list = ['apple', 'banana', 'cherry']

# The item to insert
item_to_insert = 'orange'

# The index at which to insert the item
index_to_insert = 1

# Using the list.insert() method to add the item
# The method takes two arguments: the index and the item
my_list.insert(index_to_insert, item_to_insert)

# Print the modified list to show the result
print(my_list)

#Exercise 2

# A sample string
my_string = "Hello, world! This is a test."

# Initialize a counter for the spaces
space_count = 0

# Loop through each character in the string
for char in my_string:
    # Check if the character is a space
    if char == ' ':
        # If it is, increment the counter
        space_count += 1

# Print the final count
print(f"The number of spaces in the string is: {space_count}")

#Exercise 3

# A sample string
my_string = "Hello World! This is a TeSt."

# Initialize counters for uppercase and lowercase letters
upper_count = 0
lower_count = 0

# Loop through each character in the string
for char in my_string:
    # Check if the character is an uppercase letter
    if char.isupper():
        upper_count += 1
    # Check if the character is a lowercase letter
    elif char.islower():
        lower_count += 1

# Print the final counts
print(f"Number of uppercase letters: {upper_count}")
print(f"Number of lowercase letters: {lower_count}")

#Exercise 4

def my_sum(numbers):
    """
    Calculates the sum of a list of numbers without using the built-in sum() function.
    """
    # Initialize a variable to store the total sum
    total = 0
    
    # Loop through each number in the list
    for number in numbers:
        # Add the current number to the total
        total += number
        
    # Return the final sum
    return total

# Example usage
numbers_list = [1, 5, 4, 2]
sum_of_list = my_sum(numbers_list)

print(f"The sum of the list {numbers_list} is: {sum_of_list}")

#Exercise 5

def find_max(numbers):
    """
    Finds the maximum number in a list without using the built-in max() function.
    """
    # Handle the edge case of an empty list
    if not numbers:
        return None
        
    # Initialize max_num with the first element of the list
    max_num = numbers[0]
    
    # Loop through the rest of the elements in the list
    for number in numbers[1:]:
        # If the current number is greater than max_num, update max_num
        if number > max_num:
            max_num = number
            
    # Return the final maximum number
    return max_num

# Example usage
numbers_list = [0, 1, 3, 50]
max_number = find_max(numbers_list)

print(f"The maximum number in the list {numbers_list} is: {max_number}")

#Exercise 6

def factorial(n):
    """
    Calculates the factorial of a non-negative integer.
    """
    # Handle edge cases for non-negative integers
    if n < 0:
        return "Factorial is not defined for negative numbers"
    if n == 0 or n == 1:
        return 1
    
    # Initialize the result
    result = 1
    
    # Loop from 2 up to n to calculate the factorial
    for i in range(2, n + 1):
        result *= i
        
    # Return the final result
    return result

# Example usage
number = 4
factorial_result = factorial(number)

print(f"The factorial of {number} is: {factorial_result}")

#Exercise 7

def list_count(items, element):
    """
    Counts the number of occurrences of an element in a list without
    using the built-in list.count() method.
    """
    # Initialize a counter variable
    count = 0
    
    # Loop through each item in the list
    for item in items:
        # Check if the current item is the one we are looking for
        if item == element:
            # If it is, increment the counter
            count += 1
            
    # Return the final count
    return count

# Example usage
my_list = ['a', 'a', 't', 'o']
element_to_count = 'a'
occurrences = list_count(my_list, element_to_count)

print(f"The element '{element_to_count}' appears {occurrences} times.")

#Exercise 8

import math

def norm(numbers):
    """
    Calculates the L2-norm (square root of the sum of squares) of a list of numbers.
    """
    # Initialize a variable to store the sum of the squares
    sum_of_squares = 0
    
    # Loop through each number in the list
    for number in numbers:
        # Square the number and add it to the sum
        sum_of_squares += number ** 2
        
    # Return the square root of the sum of squares
    return math.sqrt(sum_of_squares)

# Example usage
numbers_list = [1, 2, 2]
l2_norm = norm(numbers_list)

print(f"The L2-norm of the list {numbers_list} is: {l2_norm}")

#Exercise 9

def is_mono(arr):
    """
    Checks if an array is monotonic (sorted either ascending or descending).
    """
    # An empty or single-element list is considered monotonic
    if len(arr) <= 1:
        return True
    
    # Check for a non-decreasing sequence
    is_non_decreasing = all(arr[i] <= arr[i+1] for i in range(len(arr) - 1))
    
    # Check for a non-increasing sequence
    is_non_increasing = all(arr[i] >= arr[i+1] for i in range(len(arr) - 1))
    
    # The array is monotonic if it is either non-decreasing or non-increasing
    return is_non_decreasing or is_non_increasing

# Example usages
print(is_mono([7,6,5,5,2,0]))
# Expected output: True

print(is_mono([2,3,3,3]))
# Expected output: True

print(is_mono([1,2,0,4]))
# Expected output: False

#Exercise 10

def print_longest_word(words):
    """
    Finds and prints the longest word in a list of words.
    """
    # Handle the edge case of an empty list
    if not words:
        print("The list is empty.")
        return
        
    # Initialize the longest_word variable with the first word in the list
    longest_word = words[0]
    
    # Iterate through the rest of the words in the list
    for word in words[1:]:
        # If the current word is longer than the current longest_word,
        # update longest_word
        if len(word) > len(longest_word):
            longest_word = word
            
    # Print the final longest word
    print(longest_word)

# Example usage
word_list = ["hello", "world", "python", "programming", "is", "fun"]
print_longest_word(word_list)

# Expected output: programming

#Exercise 11

# A sample list containing a mix of integers and strings
mixed_list = [1, 'apple', 2, 'banana', 3, 'cherry', 4, 'date', 'orange', 5]

# Initialize two empty lists to store the separated items
integers = []
strings = []

# Loop through each item in the mixed list
for item in mixed_list:
    # Check if the item is an integer
    if isinstance(item, int):
        integers.append(item)
    # Check if the item is a string
    elif isinstance(item, str):
        strings.append(item)

# Print the final lists
print(f"Original list: {mixed_list}")
print(f"Integers: {integers}")
print(f"Strings: {strings}")

# Expected output:
# Integers: [1, 2, 3, 4, 5]
# Strings: ['apple', 'banana', 'cherry', 'date', 'orange']

#Exercise 12

def is_palindrome(text):
    """
    Checks if a string is a palindrome (reads the same forwards and backward).
    """
    # The simplest way to check is to compare the string with its reversed version.
    # The slicing syntax text[::-1] creates a reversed copy of the string.
    return text == text[::-1]

# Example usage from the instructions
print(is_palindrome('radar'))
# Expected output: True

print(is_palindrome('John'))
# Expected output: False

# Another example
print(is_palindrome('madam'))
# Expected output: True

#Exercise 13

def sum_over_k(sentence, k):
    """
    Returns the number of words in a sentence with a length greater than k.
    """
    # Split the sentence into a list of words
    words = sentence.split()
    
    # Initialize a counter for words longer than k
    count = 0
    
    # Loop through each word in the list
    for word in words:
        # Check if the length of the word is greater than k
        if len(word) > k:
            count += 1
            
    # Return the final count
    return count

# Example usage from the instructions
sentence = 'Do or do not there is no try'
k = 2

result = sum_over_k(sentence, k)
print(result)

#Exercise 14

def dict_avg(my_dict):
    """
    Calculates the average of all numeric values in a dictionary.
    """
    # Handle the edge case of an empty dictionary
    if not my_dict:
        return 0
    
    # Get a list of all values from the dictionary
    values = my_dict.values()
    
    # Calculate the sum of all values
    total_sum = sum(values)
    
    # Get the number of items in the dictionary
    count = len(my_dict)
    
    # Calculate and return the average
    average = total_sum / count
    return average

# Example usage from the instructions
my_dict = {'a': 1, 'b': 2, 'c': 8, 'd': 1}
average_value = dict_avg(my_dict)

print(average_value)

#Exercise 15

def common_div(a, b):
    """
    Finds all common divisors of two numbers.
    """
    divisors = []
    
    # The common divisors cannot be greater than the smaller of the two numbers.
    min_num = min(a, b)
    
    # Loop from 1 up to the minimum number
    for i in range(1, min_num + 1):
        # Check if 'i' divides both 'a' and 'b' with no remainder
        if a % i == 0 and b % i == 0:
            divisors.append(i)
            
    return divisors

# Example usage from the instructions
print(common_div(10,20))

#Exercise 16

import math

def is_prime(n):
    """
    Tests if a number is a prime number.
    A prime number is a natural number greater than 1 that has no
    positive divisors other than 1 and itself.
    """
    # Prime numbers must be greater than 1.
    if n <= 1:
        return False
    
    # Check for divisors from 2 up to the square root of n.
    # We only need to check up to the square root because if n has a
    # divisor greater than its square root, it must also have one smaller.
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            # If a divisor is found, the number is not prime.
            return False
            
    # If the loop completes without finding any divisors, the number is prime.
    return True

# Example usage from the instructions
print(is_prime(11))
# Expected output: True

# Another example with a non-prime number
print(is_prime(10))
# Expected output: False

#Exercise 17

def weird_print(numbers):
    """
    Finds elements in a list where both the index and the value are even,
    and prints them as a new list.
    """
    even_elements = []
    
    # Use enumerate to get both the index and the value
    for index, value in enumerate(numbers):
        # Check if the index is even and the value is even
        if index % 2 == 0 and value % 2 == 0:
            even_elements.append(value)
            
    # Print the final list of elements
    print(even_elements)

# Example usage from the instructions
weird_print([1, 2, 2, 3, 4, 5])
# Expected output: [2, 4]

#Exercise 18

def type_count(**kwargs):
    """
    Accepts an undefined number of keyword arguments and returns a string
    with the count of each argument type.
    """
    counts = {}
    
    # Iterate through the values of the keyword arguments
    for value in kwargs.values():
        # Get the name of the type of the current value
        type_name = type(value).__name__
        
        # Increment the count for this type, or start a new count if it's new
        counts[type_name] = counts.get(type_name, 0) + 1
        
    # Format the counts dictionary into the desired string format
    output_parts = [f"{key}: {value}" for key, value in counts.items()]
    return ", ".join(output_parts)

# Example usage from the instructions
result = type_count(a=1, b='string', c=1.0, d=True, e=False)
print(result)

# Expected output: int: 1, str: 1, float: 1, bool: 2

#Exercise 19

def my_split(text, delimiter=' '):
    """
    Mimics the built-in str.split() method.
    Splits a string by a given delimiter, defaulting to whitespace.
    """
    result = []
    current_word = ""
    
    # Iterate through each character of the string
    for char in text:
        # If the character is the delimiter, we have finished a word
        if char == delimiter:
            # Add the accumulated word to the result list
            if current_word:  # This check prevents adding empty strings
                result.append(current_word)
            current_word = ""  # Reset the word accumulator
        else:
            # If not a delimiter, append the character to the current word
            current_word += char
    
    # After the loop, append the last word if there is one
    if current_word:
        result.append(current_word)
        
    return result

# Example 1: Using the default whitespace delimiter
sentence = 'Hello world, this is a test.'
print(f"Splitting '{sentence}' by default delimiter: {my_split(sentence)}")
# Expected output: ['Hello', 'world,', 'this', 'is', 'a', 'test.']

# Example 2: Using a custom delimiter
hyphenated_string = 'one-two-three'
print(f"Splitting '{hyphenated_string}' by '-': {my_split(hyphenated_string, '-')}")
# Expected output: ['one', 'two', 'three']

#Exercise 20

def to_password_format(text):
    """
    Converts a string into a password format by replacing each character with an asterisk.
    """
    # Get the length of the input string
    password_length = len(text)
    
    # Create a new string with asterisks repeated by the length
    password_format = '*' * password_length
    
    return password_format

# Example usage from the instructions
input_string = "mypassword"
output_string = to_password_format(input_string)

print(f'input : "{input_string}"')
print(f'output: "{output_string}"')

# Expected output:
# input : "mypassword"
# output: "**********"

#end