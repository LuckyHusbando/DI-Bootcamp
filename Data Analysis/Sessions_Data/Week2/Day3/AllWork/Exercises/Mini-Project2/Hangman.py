#Hangman Game

import random

def main():
    """
    Main function to run the Hangman game.
    """
    wordslist = ['correction', 'childish', 'beach', 'python', 'assertive', 'interference', 'complete', 'share', 'credit card', 'rush', 'south']
    word = random.choice(wordslist)

    # Set up initial game state variables
    guesses_left = 6
    guessed_letters = set()
    
    # Create the hidden representation of the word(s)
    # Spaces will be visible, letters will be stars
    hidden_word_list = []
    for char in word:
        if char == ' ':
            hidden_word_list.append(' ')
        else:
            hidden_word_list.append('*')
            
    print("Welcome to Hangman!")

    # The main game loop
    while guesses_left > 0 and '*' in hidden_word_list:
        # Display the current state of the game
        print("\n" + " ".join(hidden_word_list))
        print(f"Body parts remaining: {guesses_left}")
        print(f"Guessed letters: {', '.join(sorted(list(guessed_letters)))}")
        
        # Get a letter guess from the player
        guess = input("Guess a letter: ").lower()
        
        # Validate the player's input
        if not guess.isalpha() or len(guess) != 1:
            print("Invalid input. Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print("You have already guessed that letter. Try again.")
            continue
        
        # Add the new guess to the set of guessed letters
        guessed_letters.add(guess)
        
        # Check if the guess is in the word
        if guess in word.lower():
            print("Good guess! The letter is in the word.")
            # Update the hidden word with the correctly guessed letter
            for i, char in enumerate(word.lower()):
                if char == guess:
                    hidden_word_list[i] = word[i] # Preserve original case
        else:
            print("Sorry, that letter is not in the word.")
            guesses_left -= 1

    # End of game logic
    print("\n" + " ".join(hidden_word_list))
    if '*' not in hidden_word_list:
        print("Congratulations! You have solved the word!")
    else:
        print("Game over! You ran out of body parts.")
        print(f"The word was: {word}")

# Run the game
if __name__ == "__main__":
    main()

#end