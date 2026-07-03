#W3D2EX2

#Exercise 3 - Dogs Domesticated

from W3D2EX import Dog
import random

class PetDog(Dog):
    def __init__ (self, name, age, weight, trained=False):
        super().__init__(name, age, weight)
        self.trained = trained

    def train(self):
        print(self.bark())
        self.trained = True

    def play(self, *args):
        dog_names = [dog.name for dog in args]
        all_names = [self.name] + dog_names
        if len(all_names) > 1:
            names_str = ", ".join(all_names[:-1]) + f" and {all_names[-1]}"
        else:
            names_str = self.name
        print (f"{names_str} all play together!")

    def do_a_trick(self):
        if self.trained:
            tricks = ["does a barrel roll", "stands on their back legs", "shakes your hand", "plays dead."]
            chosen_trick = random.choice(tricks)
            print(f"{self.name} {chosen_trick}!")
        else:
            print(f"{self.name} is not trained yet and doesn't know any tricks.")

#Test PetDog methods

goofy = PetDog("Goofy", 2, 30)
pierre = ("Pierre", 5, 20)
pepper = PetDog("Pepper", 10, 7)

myPet = PetDog("Pepper", 10, 7)
myPet.train()
myPet.play(goofy)
myPet.do_a_trick()

#Exercise 4 - Family and Person Classes

class Person:
    def __init__(self, first_name, age, last_name):
        self.first_name = first_name
        self.age = age
        self.last_name = last_name

    def is_18(self):
        if self.age >= 18:
            return True
        else:
            return False

class Family:
    def __init__ (self, last_name):
        self.last_name = last_name
        self.members = []

    def born(self, first_name, age):
        new_baby = Person(first_name, age, self.last_name)
        self.members.append(new_baby)
        print(f"Congratulations! {first_name}{self.last_name} was added to the family.")

    def check_majority(self, first_name):
        for person in self.members:
            if person.first_name == first_name:
                if person.is_18():
                    print("You are over 18, your parents Jane and John accept that you will go out with your friends.")
                else:
                    print("Sorry, you are not allowed to go out with your friends.")
                return
            
        print(f"{first_name} is not a member of this family.")

    def family_presentation(self):
        print(f"\n--- The {self.last_name} Family Presentation ---")
        for person in self.members:
            print(f"Name: {person.first_name}, Age: {person.age}")

fam = Family(" Smith")

fam.born("John", 45)
fam.born("Jane", 44)
fam.born("Alice", 20) #Adult
fam.born("Charlie", 12) #Minor

print("\n--- Checking Majority---")
fam.check_majority("Alice") #Should allow out
fam.check_majority("Charlie") #Should deny

fam.family_presentation()