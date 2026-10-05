#Timed Challenge 1

# Get the input string from the user
input_string = input("Enter a string: ")

# Get the character to search for from the user
search_char = input("Enter a character to count: ")

# Initialize a counter variable
occurrence_count = 0

# Loop through each character in the input string
for char in input_string:
    # Check if the current character matches the character to search for
    if char == search_char:
        # If it's a match, increment the counter
        occurrence_count += 1

# Print the final result
print(f"The character '{search_char}' appears {occurrence_count} times in the string.")
