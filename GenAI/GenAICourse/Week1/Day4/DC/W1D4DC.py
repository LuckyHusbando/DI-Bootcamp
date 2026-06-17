#W1D4DC

print("--- Challenge 1: Multiples of a Number ---")

# 1. Ask the user for the two inputs and convert them to integers
number = int(input("Enter the base number: "))
length = int(input("Enter how many multiples you want (length): "))

# Initialize an empty list to store the sequence
multiples_list = []

# 2 & 3. Loop from 1 up to length (inclusive) to generate the multiples
for i in range(1, length + 1):
    multiples_list.append(number * i)

# Print the final generated list
print(f"Output:\n{multiples_list}")

#Challenge 2

# 1. Ask the user for a string input
user_word = input("Enter a word: ").strip()

# Initialize an empty string to build our result
modified_word = ""

# 2. Process the string character by character
for letter in user_word:
    # If our new string is empty, or the current letter is different 
    # from the last letter we successfully added, we keep it.
    if len(modified_word) == 0 or letter != modified_word[-1]:
        modified_word += letter

# 3. Print the final modified string
print(f"Output:\n\"{modified_word}\"")