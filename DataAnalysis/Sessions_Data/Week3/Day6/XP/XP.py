#Exercise XP - Week 3 Day 6

#Exercise 1 - Random Sentence Generator

import random
import os

def get_words_from_file(file_path):
    """
    Reads a list of words from a file.
    
    Args:
        file_path (str): The path to the word list file.
        
    Returns:
        list: A list of words from the file.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            words = f.read().split()
        return words
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return []

def get_random_sentence(length):
    """
    Generates a random sentence of a specified length.
    
    Args:
        length (int): The number of words in the sentence.
        
    Returns:
        str: A randomly generated sentence.
    """
    # Assuming 'word_list.txt' is in the same directory as the script.
    file_path = os.path.join(os.path.dirname(__file__), 'word_list.txt')
    words = get_words_from_file(file_path)
    
    if not words:
        return "Cannot generate a sentence; word list is empty or not found."
    
    random_words = random.choices(words, k=length)
    sentence = " ".join(random_words)
    return sentence.lower()

def main():
    """
    Main function to handle user input and program flow.
    """
    print("Welcome to the Random Sentence Generator!")
    print("This program generates a random sentence using a word list.")
    
    try:
        length_input = input("Please enter the desired sentence length (between 2 and 20): ")
        length = int(length_input)
        
        if 2 <= length <= 20:
            sentence = get_random_sentence(length)
            print("\nGenerated Sentence:")
            print(sentence)
        else:
            print("Error: The length must be between 2 and 20.")
            exit()
    except ValueError:
        print("Error: Invalid input. Please enter an integer.")
        exit()

if __name__ == "__main__":
    # To run this, you need a 'word_list.txt' file in the same directory.
    # A sample 'word_list.txt' could contain:
    # the quick brown fox jumps over the lazy dog and a lot of other words
    # create a dummy file for demonstration purposes
    with open('word_list.txt', 'w', encoding='utf-8') as f:
        f.write("The quick brown fox jumps over the lazy dog. A lot of words are here.")
    
    main()

# ============Exercise 2 - Working with Json==============

import json

sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

# Step 1: Load the JSON string
data = json.loads(sampleJson)

# Step 2: Access the nested “salary” key
salary = data["company"]["employee"]["payable"]["salary"]
print(f"The salary is: {salary}")

# Step 3: Add the “birth_date” key
data["company"]["employee"]["birth_date"] = "1990-05-15"

# Step 4: Save the modified JSON to a file
with open("modified_data.json", "w") as json_file:
    json.dump(data, json_file, indent=4)

print("Modified JSON saved to 'modified_data.json'")

#end
