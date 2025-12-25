#Class Attributes

#Attributes can be assigned to classes, not just objects.

class Animal:
    
    mammal = True

from datetime import datetime, date

class Person:

    ID_number = 1

    def __init__(self, name, last_name, birth_date):
        self.name = self.format_name(name)
        self.last_name = self.format_name(last_name)
        self.birth_date = self.parse_birthdate(birth_date)
        Person.ID_number += 1

    @staticmethod
    def parse_birthdate(date_str):
       return datetime.strptime(date_str, '%d-%m-%y').date()

#Class Decorators - Functions defined within classes. Built-in.
#e.g. @classmethod, @staticmethod, @property
#They are functions that change our existing functions!

#Create a static method that formats the name and last name.
#In case the first letter is not upper case, search for isupper() method)
#Check that it works:
#Print(Person.format_name('lise'))

    @staticmethod
    def format_name(name):
       if not name[0].isupper():
          return name.capitalize()
       else:
          return name

P1 = ('John', 'Snow', 18)

# print(type(P1.birth_date))

#Class Method
#Methods that are not bound to an object but to a class.
#The first argument is the class itself.

@classmethod
def from_age(cls, name, last_name, age):
   current_year = datetime.today().year
   birth_year = current_year - age
   birth_date = f'-1-1-{birth_year})'
   return cls(name, last_name, birth_date)
    
# P2 = Person.from_age('arya', 'stark', 18)
# print(P2.birth_date)

#Property
#Like an argument, but using a method instead to get or set a value from a class.
#Creates a new property without having to use __init__

P1 = ('John', 'Snow', 18)
P2 = ('Tom' 'Johns', 20)

@property
def age(self):
   today = date.today()
   age = today.year - self.birth_date.year
   return age

#Dunder Methods
#We don't need to call them, they are used to test information about the classes and past actions that need doing.
#Defining dunder methods is only 1-2 lines typically. Many are used for comparing one object with another.

def __str__(self):
   return f'name: {self.name} \n last_name: {self.last_name} \n age: {self.age}'

def __repr__(self): #For developers, to get information.
   return f'{self.__dict__}'

def __lt__(self, other):
   return self.age > other.age

print(P1<P2)

#Modules

