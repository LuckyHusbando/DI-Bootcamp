#AnagramsProject

from anagram_checker import AnagramChecker

def main():
    #Initialize checker using text file containing words.
    #Replace words.txt with actual name of saved text file.
    checker = AnagramChecker(r'c:\DI-Bootcamp\GenAI\GenAICourse\Week4\Day2\EX\words.txt')

    while True:
        print("\n--- Anagram Checker Menu ---")
        print("1. Input a word")
        print("2. Exit")
        choice = input("Choose an option (1 or 2): ").strip()

        if choice == '2':
            print("Goodbye!")
            break

        elif choice == "1":
            user_input = input("Enter a single word: ").strip()

            #Validation 1 - Check how many words were typed
            #Hint applied - we split the string by spaces to count words
            if len(user_input.split()) > 1:
                print("Error: Only a single word is allowed. Please do not type multiple words.")
                continue

            #Validation 2 - Check for alphabetic characters only
            if not user_input.isalpha():
                print("Error: Only alphabetic characters are allowed. No numbers or special characters can be entered.")
                continue

            #Process valid input
            if checker.is_valid_word(user_input):
                anagrams = checker.get_anagrams(user_input)

                print(f"\nYOUR WORD :\"{user_input.upper()}\"")
                print("This is a valid English word.")

                if anagrams:
                    #Join list of anagrams into a single string separated by commas
                    print(f"Anagrams for your word: {', '.join(anagrams)}.")
                else:
                    print("Anagrams for your word: None found.")
            else:
                print(f"\nYOUR WORD :\"{user_input.upper()}\"")
                print("This is not a valid English word according to the source dictionary.")

        else:
            print("Invalid choice. Please enter a 1 or 2.")

if __name__ == "__main__":
    main()