#Object Oriented Programming

#Objects and Dictionaries are very similar.
#Dictionaries are data structures. A lot of data can be stored that is labeled.

#Objects are part of Classes, this is why it is O.O.P.
#Every data value in Python is an object!

#The goal is to code abstractly so that properties & behaviors are bundled into individual objects.

#How to create a class:

class Dog:

    #The constructor
    def __init__(self, name, color, age, is_trained = False):
        """key & value"""
        """The object is being created"""
        self.name = name
        self.color = color
        self.age = age
        self.is_trained = is_trained
    def bark(self):
        print(f'{self.name} is barking!')

    def run(self):
        if self.age <= 5:
            print("{self.name} is running fast!")
        else: pass

    def walk(self, meters):
        print((self.name), "is walking for", str(meters), "meters.")

    def rename(self, new_name):
        self.name = new_name
        return self

Dog1 = Dog('Rex', 'Brown', 10, 'Trained')
print(Dog1.name)
print(Dog1.color)
print(Dog1.age)
print(Dog1.__dict__)
Dog1.breed = 'Poodle'
print(Dog1.breed)

#Create the second object of Dog, call it Dog2

Dog2 = Dog('Moshu', 'Brown', 5)
print(Dog2.is_trained)

Dog3 = Dog('Fluffy', 'White', 7, True)
print(Dog3.__dict__)

#Create a new attribute to the Dog class. Call it "is_trained"
#The value is a boolean (yes/no) and the default is false.
#Then run the code again. What happens with the object that were created
#before this new attribute was added?

#Behaviors = METHODS

#Functions > Methods (Bigger, more general)
#Methods = Functions related to a certain class
#Self = The object that will be created.

#Create a method for the Dog class called run() and if the dog's age is < 5
#then the dog is running really fast. If greater, they are running. 

Dog1 = Dog('Rex', 'Brown', 10, 'Trained')
Dog1.bark()

#Create a method called walk() that takes a parameter: (meters: int) and
#prints "dog's name is walking (meters) meters."

Dog1.walk(500)
Dog2.walk(1000)
#Two objects can call the same method.
Dog3.run()
#or...
Dog.run(Dog3)
Dog.walk(Dog3, 200)

#Create a method that changes the attribute.

Dog3.rename("Xuxa")
print(Dog3.name)

