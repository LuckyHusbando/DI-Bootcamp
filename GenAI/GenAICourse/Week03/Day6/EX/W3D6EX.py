#W3D6EX

#Exercise 1

import random
import sys
from pathlib import Path

# Step 1: Create the get_words_from_file function
def get_words_from_file(folder_path):
    try:
        # Combine the folder with the specific file using Path
        filepath = Path(folder_path) / "words.txt"

        with open(filepath, "r") as file:
            content = file.read()
            # Split the content into a list of words and return it
            return content.split()
            
    except FileNotFoundError:
        print(f"Error: Could not find the file '{filepath}'.")
        sys.exit(1)

# Step 2: Create the get_random_sentence function
def get_random_sentence(length):
    # Pass the correct host folder context from previous steps
    folder_path = r"C:\DI-Bootcamp\GenAI\GenAICourse\Week3\Day6\EX"
    
    # Call get_words_from_file to get the list of words
    words = get_words_from_file(folder_path)
    
    if not words:
        print("Error: The file is empty.")
        sys.exit(1)
        
    # Select a random word from the list 'length' times
    selected_words = random.choices(words, k=length)
    
    # Create a sentence and convert it to lowercase
    sentence = " ".join(selected_words).lower()
    return sentence

# Step 3: Create the main function
def main():
    # Print a message explaining the program’s purpose
    print("Welcome! This program reads words from a text file (words.txt) ")
    print("and generates a completely random sentence based on the length you choose.\n")
    
    # Ask the user for the desired sentence length
    user_input = input("Please enter the desired sentence length (2-20): ")
    
    # Validate the user input (Check if it is an integer)
    try:
        length = int(user_input)
    except ValueError:
        print("Error: Invalid input. You must enter a whole integer.")
        return  # Exit the program
        
    # Validate the user input (Check if it is between 2 and 20 inclusive)
    if length < 2 or length > 20:
        print("Error: The sentence length must be between 2 and 20.")
        return  # Exit the program
        
    # If valid, call get_random_sentence with the length and print it
    generated_sentence = get_random_sentence(length)
    print("\nYour random sentence:")
    print(generated_sentence)

if __name__ == "__main__":
    main()

import json

#Sample JSON string based on your nested structure
json_string = '''
{
    "company": {
        "employee": {
            "name": "Alex Smith",
            "payable": {
                "salary": 85000,
                "bonus": 5000
            }
        }
    }
}
'''

# Parse the JSON string into a Python dictionary
data = json.loads(json_string)

# Access the deeply nested salary key
salary = data["company"]["employee"]["payable"]["salary"]

print(f"Employee Salary: ${salary}")

# Add a birth date to the employee record
data["company"]["employee"]["birth_date"] = "1992-08-24"

# Save the updated dictionary to a local file
with open("employee_data.json", "w") as file:
    json.dump(data, file, indent=4)
    
print("Data successfully saved to employee_data.json")