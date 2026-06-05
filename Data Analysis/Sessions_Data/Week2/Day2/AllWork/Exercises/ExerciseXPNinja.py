#Exercise 1 XP NINJA

def get_full_name(first_name, last_name, middle_name=None):
    """
    Constructs a full name from first, middle (optional), and last names.
    The function capitalizes the first letter of each name.
    """
    # Capitalize the first and last names
    first_name_capitalized = first_name.title()
    last_name_capitalized = last_name.title()

    # Check if a middle name was provided
    if middle_name:
        middle_name_capitalized = middle_name.title()
        # Return the full name including the middle name
        full_name = f"{first_name_capitalized} {middle_name_capitalized} {last_name_capitalized}"
    else:
        # Return the full name without the middle name
        full_name = f"{first_name_capitalized} {last_name_capitalized}"
    
    return full_name

# Example 1: Calling the function with a middle name
full_name_1 = get_full_name(first_name="john", middle_name="hooker", last_name="lee")
print(full_name_1)

# Example 2: Calling the function without a middle name
full_name_2 = get_full_name(first_name="bruce", last_name="lee")
print(full_name_2)

#Exercise 2

# Sourced from standard Morse code tables.
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
    ',': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-',
    '(': '-.--.', ')': '-.--.-'
}

# Create a reverse dictionary for decoding, swapping keys and values.
# The `dict(item, item)` syntax is a quick way to create a new dictionary.
DECODE_DICT = {code: letter for letter, code in MORSE_CODE_DICT.items()}

def encrypt(message):
    """
    Converts a string message to Morse code.
    Each letter is separated by a space, and each word by a '/'.
    """
    morse_code = []
    # Split the message into words to handle word separation
    words = message.upper().split()
    
    for word in words:
        morse_word = []
        # Convert each character of the word to its Morse code representation
        for char in word:
            # Check if the character is in our dictionary
            if char in MORSE_CODE_DICT:
                morse_word.append(MORSE_CODE_DICT[char])
        # Join the Morse code for each letter with a space
        morse_code.append(" ".join(morse_word))
    
    # Join the Morse code for each word with a slash
    return " / ".join(morse_code)

def decrypt(morse_code):
    """
    Converts a Morse code string back to English text.
    """
    decoded_message = []
    # Split the Morse code string by ' / ' to get words
    morse_words = morse_code.strip().split(" / ")
    
    for morse_word in morse_words:
        english_word = []
        # Split the Morse word by spaces to get individual letter codes
        morse_letters = morse_word.split(' ')
        for code in morse_letters:
            # Check if the code is in our decoding dictionary
            if code in DECODE_DICT:
                english_word.append(DECODE_DICT[code])
        # Join the decoded letters to form the English word
        decoded_message.append("".join(english_word))
        
    # Join the English words with a space
    return " ".join(decoded_message)

# --- Example Usage ---

# Example 1: Encrypting a message
message_to_encrypt = "Hello World"
encrypted_message = encrypt(message_to_encrypt)
print(f"Original message: '{message_to_encrypt}'")
print(f"Encrypted Morse code: '{encrypted_message}'")
# Expected Output: '.... . .-.. .-.. --- / .-- --- .-. .-.. -..'

print("-" * 20)

# Example 2: Decrypting a message
morse_to_decrypt = ".... . .-.. .-.. --- / .-- --- .-. .-.. -.."
decrypted_message = decrypt(morse_to_decrypt)
print(f"Original Morse code: '{morse_to_decrypt}'")
print(f"Decrypted message: '{decrypted_message}'")
# Expected Output: 'HELLO WORLD'

#Exercise 3

def box_printer(*args):
    """
    Prints a list of strings, one per line, inside a rectangular frame.
    """
    # 1. Determine the length of the longest string to set the box width.
    if not args:
        print("No strings provided.")
        return

    max_length = max(len(s) for s in args)

    # 2. Calculate the total width of the box.
    #    This includes the max string length, 2 spaces for padding, and 2 asterisks for the border.
    box_width = max_length + 4

    # 3. Print the top border of the box.
    print("*" * box_width)

    # 4. Print each string inside the box.
    for text in args:
        # Use str.ljust() to pad the string with spaces to the maximum length.
        # This ensures all strings are the same length inside the box.
        print(f"* {text.ljust(max_length)} *")

    # 5. Print the bottom border of the box.
    print("*" * box_width)

# Example call from the instructions
box_printer("Hello", "World", "in", "reallylongword", "a", "frame")

# Another example call to demonstrate flexibility
print("\n")
box_printer("Python", "is", "awesome")

#Exercise 4

# This Python code implements the Insertion Sort algorithm.

# The primary purpose of the insertion_sort function is to sort a list of numbers in ascending order. 
# The rest of the script demonstrates how to use this function on a sample list of integers and then prints the sorted result.