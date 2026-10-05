#ARGS & KWARGS
# ARGS = Arguments = Lists, Tuples, Sets
# Key, KWARG = Arguments = Dictionary

students = ['Harry', 'Ron', 'Hermione']

def welcome(*args):
    if args:
        for name in args:
            print(f'{name}, welcome!')
    else:
        print('You did not pass names')

# welcome(students)
welcome('Camilla', 'Niv', 'David', 'Flavia')

def user_info(**kwargs):
    print(kwargs)
    for value in kwargs.values():
        print(value)

user_info(name = "Juliana", email = "Juliana@gmail.com", Age = 35, is_online = True, pets = ['cat', 'dog'])

numbers = [[1,2,3],[4,5,6],[7,8,9]]
#Tables are two-dimensional lists in programming
# [1,2,3],
# [4,5,6],
# [7,8,9]

print(numbers[0][1])