import os
from MiniProjectAnagramChecker import AnagramChecker

def get_user_input():
    '''Prompts the user for a word and validates the input.'''
    while True:
        user_input = input("Enter a word to find its anagrams (or type 'exit' to quit): ").strip()

        if user_input.lower() == 'exit':
            return None
        
        #Checks for incorrect objects
        if not user_input.isalpha():
            print("Error: Only alphabetic characters are allowed.")
            continue

        return user_input
    
def display_results(word, is_valid, anagrams):
    '''Displays the results in a user-friendly format.'''
    print(f"\nYour word :\"{word.upper()}\"")
    if is_valid:
        print("This is a valid English word.")
    else:
        print("This is not a valid English word.")

    if anagrams:
        print(f"Anagrams for your word: {', '.join(anagrams)}.\n")
    else:
        print("No anagrams found for this word.\n")

def main():
    '''Main function to run the anagram program.'''
    print("Welcome to the Anagram Checker!")

    #Initialize the AnagramChecker Instance
    #Aassuming 'sowpods.txt' is in the same directory
    
    # Get the directory of the current script file
    current_dir = os.path.dirname(os.path.realpath(__file__))
    # Create the full, absolute path to the sowpods.txt file
    file_path = os.path.join(current_dir, 'sowpods.txt')
    
    # Pass the correct file path to the AnagramChecker
    checker = AnagramChecker(file_path=file_path)

    while True:
        user_word = get_user_input()

        if user_word is None:
            print("Goodbye!")
            break

        is_valid = checker.is_valid_word(user_word)
        anagrams = checker.get_anagrams(user_word)

        display_results(user_word, is_valid, anagrams)

if __name__ == "__main__":
    main()