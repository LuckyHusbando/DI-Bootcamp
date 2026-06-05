#DC 2 - Caesar Cypher

def caesar_cipher():
    """
    Encrypts or decrypts a message using the Caesar cipher.
    """
    # Ask the user whether to encrypt or decrypt
    while True:
        choice = input("Do you want to 'encrypt' or 'decrypt'? ").lower()
        if choice in ['encrypt', 'decrypt']:
            break
        print("Invalid choice. Please type 'encrypt' or 'decrypt'.")
    
    # Get the message and the shift value
    message = input("Enter your message: ")
    while True:
        try:
            shift = int(input("Enter the shift number (e.g., 3): "))
            break
        except ValueError:
            print("Invalid shift number. Please enter an integer.")

    result = ""
    # Adjust the shift direction based on the user's choice
    if choice == 'decrypt':
        shift = -shift

    # Loop through each character in the message
    for char in message:
        # Check if the character is a letter
        if char.isalpha():
            # Determine if the letter is uppercase or lowercase
            start_point = ord('A') if char.isupper() else ord('a')
            
            # Apply the cipher shift with wrap-around logic
            # (ord(char) - start_point) gets the 0-25 index of the letter
            # ( ... + shift) % 26 applies the shift and wraps it
            # + start_point converts the new index back to an ASCII code
            shifted_char = chr((ord(char) - start_point + shift) % 26 + start_point)
            result += shifted_char
        else:
            # If the character is not a letter, add it unchanged
            result += char
            
    # Print the final result
    print(f"The {'encrypted' if choice == 'encrypt' else 'decrypted'} message is: {result}")

# Run the program
caesar_cipher()