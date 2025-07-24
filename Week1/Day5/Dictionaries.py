#Dictionaries
#Syntax
# {'key': value, 'key': value}

dict_constructor = {'name':'Derek', 
                    'age': 41, 
                    'pet': ['Pepper']}

student_info = {
    'first_name': 'Harry'
    'last_name': 'Potter'
    'age': 14
    'address': 'Hogwarts University'
    'pets': ['Hedwig', 'Buckbeak']
    'houses': {'main': 'Griffyndor', 'second': 'Slytherin'}
    'best_friends:' ('Ron Weasley', 'Hermione Granger')
}

#Accessing Data
print(student_info['pets'])
print(student_info['pets'][1])

#Using methods on the values
student_info['pets'].append('Fenix')
print(student_info['pets'])
print(student_info['first_name'].upper())

#Changing Values
student_info['address'] = "Hogwarts"
print(student_info)

#Deleting A Key
del student_info['age']
print(student_info)

#Creating key value pair

student_info['teachers'] = {'Dumbledore', 'Snape', 'McGonagal'}
print(student_info)

#Exercise
#Access the value of key history

sample_dict = {
    "class":{
        "student:"{
            "name":"Mike",
            "marks":{
                "physics":70,
                "history":80
            }
        }
    }
}