#Challenge 1
number = int(input("input a number: "))
length = int(input("input a length: "))
multiples = []
for i in range(1, length +1):
    multiples.append(number * 1)
print (multiples)

#Challenge 2
word = input("input a word with consecutive duplicate letters: ")
letters = []
last_character = ""
for character in word:
    if character != last_character:
        letters.append(character)
        last_character = character
new_word = "".join(letters)
print(new_word)
