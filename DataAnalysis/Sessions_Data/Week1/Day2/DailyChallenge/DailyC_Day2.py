
#Daily Challenge - Day 2

import random

user_input = input("Please enter a string exactly 10 characters long: ")
if len(user_input) < 10:
    print("String not long enough")
elif len(user_input) > 10:
    print("String too long")
else: print("Perfect string")

first_char = user_input[0]
last_char = user_input[-1]
print(f'First character: {first_char}')
print(f'Last character: {last_char}')

for i in range(1, len(user_input) +1):
    print(user_input[:i])

characters = list(user_input)
random.shuffle(characters)
Jumbled = ''.join(characters)
print(f'Jumbled string: {Jumbled}')
