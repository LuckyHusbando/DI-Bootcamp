#Functions & Data Structures

students = ['Harry', 'Ron', 'Hermione', 'Luna']

#create a function that says '(Name), Welcome to Hogwarts!' for all students in the given list.

def welcome():
    for name in students:
        print(f"{name}, Welcome to Hogwarts!")

welcome()

def get_house():
    for i, name in enumerate(students):
        students[i] = f'{name} - Gryphondor'

get_house()
print(students)

