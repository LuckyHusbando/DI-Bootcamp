#Exercise 1 - Dictionary

# 1 - Given a list: [("name", "Elie"), ("job", "Instructor")], create a dictionary that looks like this: {'job': 'Instructor', 'name': 'Elie'} (Note: The order does not matter).

data = [("name", "Elie"), ("job", "Instructor")]

result_dict = dict(data)
print(result_dict)

# 2 - Given two lists: ["CA", "NJ", "RI"] and ["California", "New Jersey", "Rhode Island"], return a dictionary that looks like this: {'CA': 'California', 'NJ': 'New Jersey', 'RI': 'Rhode Island'}.

State_Codes = ["CA", "NJ", "RI"]
States = ["California", "New Jersey", "Rhode Island"]

state_dict = dict(zip(State_Codes, States))
print(state_dict)

# 3 - Create a dictionary where the keys are vowels in the alphabet and the values are 0. Your dictionary should look like this: {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}. (Do not use the fromkeys method).

Vowels = ["a", "e", "i", "o", "u"]
vowel_dict = {char: 0 for char in Vowels}
print(vowel_dict)

# 4 - Create a dictionary where the key is the position of the letter in the alphabet, and the value is the letter itself. You should return something like this:

import string

alphabet_dict = {index: letter for index, letter in enumerate(string.ascii_uppercase, start=1)}
print(alphabet_dict)

#Super Bonus - Given the string "awesome sauce", return a dictionary where the keys are vowels, and the values are the count of each vowel in the string. Your dictionary should look like this: {'a': 2, 'e': 3, 'i': 0, 'o': 1, 'u': 1}.

phrase = "awesome sauce"
vowels = "aeiou"

vowel_counts = {vowel: phrase.count(vowel) for vowel in vowels}

print(vowel_counts)