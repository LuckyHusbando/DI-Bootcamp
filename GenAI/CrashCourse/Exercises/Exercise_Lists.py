#Python Iterables - Exercise 1 - Lists

#1 - Given a list [1, 2, 3, 4], print out all the values in the list one by one.

Numbers = [1, 2, 3, 4]
for value in Numbers:
    print(value)

#2 - Given a list [1, 2, 3, 4], print out all the values in the list multiplied by 20.

Numbers = [1, 2, 3, 4]

for value in Numbers:
    print(value * 20)

#3 - Given a list ["Elie", "Tim", "Matt"], return a new list with only the first letter of each name: ["E", "T", "M"].

Names = ["Elie", "Tim", "Matt"]
first_letters = [name[0] for name in Names]
print(first_letters)

#4 - Given a list [1, 2, 3, 4, 5, 6], return a new list with all the even values: [2, 4, 6].

numbers = [1, 2, 3, 4, 5, 6]

evens = [num for num in numbers if num % 2 == 0]
print(evens)

#5 - Given two lists [1, 2, 3, 4] and [3, 4, 5, 6], return a new list that contains only the values present in both lists: [3, 4].

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

intersection = list(set(list1) & set(list2))
print(intersection)

#6 - Given a list of words ["Elie", "Tim", "Matt"], return a new list with each word reversed and in lowercase: ["eile", "mit", "ttam"].

NewNames = ["Elie", "Tim", "Matt"]
reversed_names = [name[::-1].lower() for name in NewNames]
print (reversed_names)

#7 - Given two strings "first" and "third", return a new list of the letters that are present in both strings: ["i", "r", "t"].

str1 = "first"
str2 = "third"

common_letters = list(set(str1) & set(str2))
print(common_letters)

#8 - For all numbers between 1 and 100, return a list of the numbers that are divisible by 12: [12, 24, 36, 48, 60, 72, 84, 96].

divisible_by_12 = [num for num in range(1, 101) if num % 12 == 0]
print(divisible_by_12)

#9 - Given the string "amazing", return a list with all the vowels removed: ["m", "z", "n", "g"].

word = "amazing"
vowels = "aeiouAEIOU"

no_vowels = [char for char in word if char not in vowels]
print(no_vowels)

#10 - Generate a list with the following value: [[0, 1, 2], [0, 1, 2], [0, 1, 2]].

matrix = [[col for col in range(3)] for row in range(3)]
print(matrix)

#11 - Generate a list with the following structure:

# # [
#   [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
#   [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
#   [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
#   [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
#   [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
#   [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
#   [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
#   [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
#   [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
#   [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# ]

matrix_10x10 = [[col for col in range(10)] for row in range(10)]

from pprint import pprint
pprint(matrix_10x10)