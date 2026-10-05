#Exercises XP - Week 3 Day 2

#Exercise 1 - Pets

class Animals():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age, walks):
        self.name = name
        self.age = age
        self.walks = walks

    def walk(self):
        return f'{self.name} is just walking around.'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'
    
class Siamese(Cat):
    def sing(self, sounds):
        return f'{sounds}'
    
Cat1 = Bengal('Whiskers', 8, 'goes for a walk')
Cat2 = Chartreux('Midnight', 1, 'goes for a walk')
Cat3 = Siamese('Fluffbutt', 4, 'goes for a walk')

all_cats = [Cat1, Cat2, Cat3]

sara_pets = Pets(all_cats)

print(sara_pets.walk())

#Exercise 2 - Dogs

class Dog():
    is_wonderful = True

    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f'{self.name} is barking a lot!'

    def run_speed(self):
        return (int(self.weight / self.age) * 10)

    def kisses(self, other_dog):
        my_kisses = self.run_speed() * other_dog.weight
        other_dog_kisses = other_dog.run_speed() * other_dog.weight

        if my_kisses > other_dog_kisses:
            return f'{self.name} gave more kisses!'
        elif other_dog_kisses > my_kisses:
            return f'{self.name} gave less kisses!'
        else:
            return "The same number of kisses were given!"
        
Dog1 = Dog('Pepper', 9, 7)
Dog2 = Dog('Lucy', 7, 6)
Dog3 = Dog('Miko', 6, 10)

print(Dog1.bark())
print(Dog3.run_speed())
print(Dog1.kisses(Dog3))

#Exercise 3 - Dogs Domesticated

import random 

class PetDog(Dog):
    is_wonderful = True

    def __init__(self, name, age, weight, trained, tricks):
        super().__init__(name, age, weight)
        self.trained = trained
        self.tricks = tricks

    def trained(self):
        if self.trained:
            return True
        else:
            return False

    def tricks(self):
        return f'{self.name} knows several tricks.'

    def get_crazy(self):
        if self.friendly:
            return f'{self.name} doesn\'t get crazy.'
        else:
            return f'{self.name} is running at full power.'
        
    def train(self):
        print(self.bark())
        self.trained = True

    def play(self, *args):
        dog_names = ", ".join([dog.name for dog in args])
        print(f'{dog_names} all play together.')

    def do_a_trick(self):
        if self.trained:
            tricks = ["does a barrel roll", "stands on back legs", "shakes your hand", "spins in circles"]
            trick = random.choice(tricks)
            print(f'{self.name} {trick}')
        else:
            print(f'{self.name} is not trained yet.')

#Test PetDog Methods

my_dog = PetDog("Pepperoni", 4, 5, False, False)
my_dog.train()
my_dog.play(Dog1, Dog2, Dog3)
my_dog.do_a_trick()

#Exercise 4 - Family & Person Classes

class Person:

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def is_18(self):
        if self.age >= 18:
            return True
        else:
            return False
        
class Family:

    def __init__(self, last_name):
        self.last_name = last_name
        self.members = []

    def born(self, first_name, age):
        new_person = Person(first_name, self.last_name, age)
        self.members.append(new_person)
        print(f'{first_name}{self.last_name} was born into the family.')

    def check_majority(self, first_name):
        found_person = None
        for member in self.members:
            if member.first_name == first_name: 
                found_person = member
                break

        if found_person:
            if found_person.is_18():
                print("You are over 18, your parents Jane and John accept that you will go out with your friends")
            else:
                print("Sorry, you are not allowed to go out with your friends.")
        else:
            print(f"No person with the first name '{first_name}' was found in the family.")

    def family_presentation(self):
        print (f"Family Last Name: {self.last_name}")
        for member in self.members:
            print(f'First Name: {member.first_name}, Age: {member.age}')

# Example usage:
my_family = Family("Smith")
my_family.born("Jane", 40)
my_family.born("John", 42)
my_family.born("Alice", 16)
my_family.born("Bob", 20)

print("\n--- Family Presentation ---")
my_family.family_presentation()

print("\n--- Checking Majority ---")
my_family.check_majority("Alice")
my_family.check_majority("Bob")
my_family.check_majority("Peter") # A name not in the list

