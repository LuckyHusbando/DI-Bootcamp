#Functions

#A function is a reusable block of code that runs when you 'call it'.

#SYNTAX

def func_name():
    '''prints a string on the console'''
    print('I am a function.')

func_name()

#Pythonic Code - Coding that can be read like a book, as if a normal language.

#Create a function that prints "hello there!", then call the function to
#see the output

def Hello_there():
    '''prints a string that greets the user in English'''
    print("Hello there!")

Hello_there()

#Passing ARGUMENTS to the function

# def Hello_there_adv(language):
#     '''prints a greeting depending on the language'''
#     if language == 'PT':
#         print('Ola, tudo bem?')
#     elif language == "ES":
#         print('Hola, que tal?')
#     else:
#         print('Unknown language')

# Hello_there_adv('PT')

#Exercise - IF to Argument

# def Hello_there_adv(language = 'EN', name = 'John'):
#     '''prints a greeting to a name depending on the language'''
#     if language == 'PT':
#         print(f'Ola {name}, tudo bem?')
#     elif language == "ES":
#         print(f'Hola {name}, que tal?')
#     elif language == "EN":
#         print(f'Hi {name}, how are you?')
#     else:
#         print('Unknown language')

# Hello_there_adv("ES", "Dolores")

# Hello_there_adv(name = 'Pedro', language = 'PT')

# Hello_there_adv()

#Returning values from a function
def calculation(num1, num2)-> int:
    '''sums two input numbers'''
    result = num1 + num2
    return result

print(calculation(5, 3))

def multiply(calc)-> int:
    '''takes a number and multiplies by 5'''
    result = calc * 5
    return result

calc = calculation(5, 3)
print(multiply(calc))

def Hello_there_adv(language = 'EN', name = 'John')-> str:
    '''prints a greeting to a name depending on the language'''
    if language == 'PT':
        return(f'Ola {name}, tudo bem?')
    elif language == "ES":
        return(f'Hola {name}, que tal?')
    elif language == "EN":
        return(f'Hi {name}, how are you?')
    else:
        return('Unknown language')

Hello_there_adv()

# Create a function called country_info that receives a country name as
# argument and prints the capital of that country. Make the country name
# argument default Naboo (Star Wars Planet). It's capital is Theed.

def country_info(name = "Naboo", capital = "Theed")-> str:
    '''prints a capital when a country is requested'''
    if name == 'USA':
        return(f'Washington')
    elif name == 'Germany':
        return(f'Berlin')
    elif name == 'Russia':
        return(f'Moscow')
    elif name == 'Brazil':
        return(f'Brasilia')
    else:
        return('Unknown')
    
print(country_info('Germany'))

#Global & Local Scope

age = 25

def current_age():
    print(age)
    my_age = 35
    my_age += 1

current_age()

def happy_birthday():
    global age
    age += 1
    print(age)

happy_birthday()

#Global variables often used more for games, like for setting 
#persistent rules in engine behavior, etc.



