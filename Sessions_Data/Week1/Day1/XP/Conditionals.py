#CONDITIONALS

#SYNTAX
#if <condition>:
#     action

if 5 > 3 :
    print('Hello world')
else: 
    print('Not Hello')

age = input ('Age?')

if age < 18:
    print('Sorry, you cannot watch the movie.')
elif age == 21:
    print ('You got a free popcorn!')
else: 
    print('You can watch the movie.')

#Exercise 2

user_name = input('Name?')

if len(user_name) < 5: 
    print('you have a short name')
    