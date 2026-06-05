#Exercise 1 - Boolean Logic

first = "Hello World!"

#This is a comment.

print("I AM A COMPUTER!")

if 1 < 2 and 4 > 2:
    print("Math is fun!")

nope = None

# Demonstrating the integer values
print(int(True))   # Output: 1
print(int(False))  # Output: 0

string = "What's my length?"
length = len(string)
print(length)

print(first.capitalize())

string_num = "1000"
number = int(string_num)
print (number)

str(4) + "real"

3 * "cool"

numerator = 1
denominator = 0
try: 
    result = numerator/denominator
    print (result)
except ZeroDivisionError:
    print("Error: You cannot divide by Zero.")

listresult = type([])
print(listresult) #Output - Class "List"

user_name = input("What is your name?")
print("Your name is", user_name)

user_input = input("What is your favorite number?")
numbering = int(user_input)

if numbering < 0: 
    print("That number is less than 0!")
elif numbering > 0:
    print("That number is greater than 0!")
elif numbering == 0:
    print("You picked 0!")

word = "apple"
index = word.index("l")
print(index) #Output: 3

wordz = "xylophone"
check = "y" in wordz
print(check) #True

my_stringer = "Is this all in lowercase?"
if my_stringer.islower():
    print("The stringer is all lowercase")
else:
    print("The string contains uppercase letters or no cased characters.")

#Exercise 2 - Cat's & Dog's Years

#I have a cat and a dog. I got them at the same time as kitten/puppy. 
#That was humanYears years ago. Print their respective ages now as [humanYears,catYears,dogYears]

def calculate_pet_ages(human_years: int) -> list[int]:
    """
    Calculates the equivalent cat and dog years from human years.
    Returns a list in the format: [human_years, cat_years, dog_years]
    """
    if human_years == 1:
        return [1, 15, 15]
    elif human_years == 2:
        return [2, 24, 24]
    else:
        #24 is the base for 2 years, then add the additional years.
        cat_age = 24 + (human_years - 2) * 4
        dog_age = 24 + (human_years - 2) * 5
        return [human_years, cat_age, dog_age]
    
#Testing with requested values

test_values = [10, 1, 2]

for year in test_values:
    result = calculate_pet_ages(year)
    print(result)