#Dictionaries
#Syntax
# {'key': value, 'key': value}

dict_constructor = {'name':'Derek', 
                    'age': 41, 
                    'pet': ['Pepper']}

student_info = {
    'first_name': 'Harry',
    'last_name': 'Potter',
    'age': 14,
    'address': 'Hogwarts University',
    'pets': ['Hedwig', 'Buckbeak'],
    'houses': {'main': 'Griffyndor', 'second': 'Slytherin'},
    'best_friends': ('Ron Weasley', 'Hermione Granger')
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
        "student":{
            "name":"Mike",
            "marks":{
                "physics":70,
                "history":80
            }
        }
    }
}

print(sample_dict['class']["student"]["marks"]["history"])

#Loops and built-in methods for dictionaries

#keys()

for k in student_info.keys():
    print(k)

#values()
for v in student_info.values():
    print(v)

#Items()

for key, value in student_info.items():
    print(key, value)

#Update() method - The most important for dictionaries

student_info.update({'patron': 'stag'})
print(student_info)

#Exercise 2

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New York"

}

keys_to_remove = ["name", "salary"]

for key in keys_to_remove:
    if key in sample_dict:
        del sample_dict[key]

print(sample_dict)

print(sample_dict.keys())

#Zip() - Iterables - Other useful built-in functions
names = ['Derek', 'Yosef', 'Juliana', 'Sonia']
addresses = ['Ramat Gan', 'Jerusalem', "Tel Aviv", "Holon"]

print(list(zip(names, addresses)))

topics = ("Math", "English", "History", "Physics")
grades = (85, 90, 100, 75)

print(dict(zip(topics, grades)))
