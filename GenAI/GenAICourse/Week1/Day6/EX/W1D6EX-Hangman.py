#W1D6EX

#Mini-Project - Hangman

#Parameters:

# The computer choose a random word and mark stars for each letter of each word.
# Then the player will guess a letter.
# If that letter is in the word(s) then the computer fills the letter in all the correct positions of the word.
# If the letter isn’t in the word(s) then add a body part to the gallows (head, body, left arm, right arm, left leg, right leg).
# The player will continue guessing letters until they can either solve the word(s) (or phrase) or all six body parts are on the gallows.
# The player can’t guess the same letter twice.

import random

#Starter Code

wordslist = ['correction', 'childish', 'beach', 'python', 'assertive', 'interference', 'complete', 'share', 'credit card', 'rush', 'south']
word = random.choice(wordslist)

#New variables

guessed_letters = [] #To track what the user has typed
incorrect_guesses = 0
max_guesses = 6

#Generate the hidden word

hidden_word = []
for char in word:
    if char == " ":
        hidden_word.append(" ") #Reveal spaces automatically
    else:
        hidden_word.append("*") #Hide letters with stars

print("Welcome to Derek's Hangman!")

#Run while errors are under 6 AND there are still stars in the list.
while incorrect_guesses < max_guesses and "*" in hidden_word:

    #.Join() combines list of stars/letters into readable string
    print("\nWord: " + "".join(hidden_word))
    print(f"guessed letters: {', '.join(guessed_letters)}")

    #Get player input, convert to lowercase, and remove accidental spaces
    guess = input("guess a letter: ").lower().strip()

    #Validate entry is a single letter
    if len(guess) != 1 or not guess.isalpha():
        print("Invalid input. Please enter a single letter.")
        continue #Skips rest of loop and asks again.

    #Validate by checking if letter is already guessed
    if guess in guessed_letters:
        print("You already guessed that letter! Please try again.")
        continue

    #If passes both validations, add it to our guessed list
    guessed_letters.append(guess)

    #Check if guess is correct
    if guess in word:
        print(f"Good job! '{guess}' is in the word!")
        #Loop through the length of the word to find all matches
        for i in range(len(word)):
            if word[i] == guess:
                hidden_word[i] = guess #Swap the star for letter

    else:
        incorrect_guesses += 1
        #List of body parts matching error count
        body_parts = ["Head", "Body", "Left Arm", "Right Arm", "Left Leg", "Right Leg"]

        print(f"Wrong guess! Added to gallows: {body_parts[incorrect_guesses - 1]}")
        print(f"You have {max_guesses - incorrect_guesses} mistakes left.")

if "*" not in hidden_word:
    print(f"\n Congratulations! You survived. The word was: {word}")
else:
    print(f"\n Game Over! You've been hanged. The word was: {word}")