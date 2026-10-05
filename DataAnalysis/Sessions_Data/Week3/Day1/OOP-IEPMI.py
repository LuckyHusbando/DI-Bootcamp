# Object Oriented Programming - Inheritance, Encapsulation, Polymorphism, and Multiple Inheritance

# Inheritance (Parent)
# Advantages of Inheritance - Reusable & Structured Code

class Parent:
    def speak(self):
        print(f'Parent speaking')

class Child(Parent):
    def speak(self):
        print(f'Child speaking')

class Grandchild(Child):
    pass

object1 = Child()
object1.speak()

object2 = Grandchild()
object2.speak()

class Animal:

    def __init__(self, name, family, legs):
        self.name = name
        self.family = family
        self.legs = legs

    def sleep(self):
        return f'{self.name} is sleeping - from Animal'

class Dog(Animal):
    def __init__(self, name, family, legs, trained, age):
        super().__init__(name, family, legs)
        self.trained = trained
        self.age = age

    def bark(self):
        return f'{self.name} is barking.'

dog1 = Dog('Rex', 'Canine', 4, True, 5)
print(dog1.bark())

class Cat(Animal):
    def __init__(self, name, family, legs, friendly, age, nickname):
        super().__init__(name, family, legs)
        self.friendly = friendly
        self.nickname = nickname
        self.age = age

    def get_crazy(self):
        if self.friendly:
            return f'{self.name} doesn\'t get crazy.'
        else:
            return f'{self.name} is running at full power.'

class Alien:
    def __init__(self, name, planet):
        self.name = name
        self.planet = planet

    def bark(self):
        return f'{self.name} goes Ululululu'

class AlienDog(Alien, Dog):
    def __init__(self, name, family, legs, trained, age, planet):
        Alien.__init__(self, name, planet)
        Dog.__init__(self, name, family, legs, trained, age)

Alien_Dog1 = AlienDog('Buba', 'Canine', 6, True, 135, 'Jupiter')
print(Alien_Dog1.bark())

print(Dog.bark(Alien_Dog1))

#Exercise Cat+Alien

# Create an Alien Cat class that inherits from Cat & Alien.
# Create a method fly_away that checks if the cat is friendly, prints output and add 'is an alien cat.'

class AlienCat(Cat, Alien):
    def __init__(self, name, family, legs, friendly, age, nickname, planet):
        Alien.__init__(self, name, planet)
        Cat.__init__(self, name, family, legs, friendly, age, nickname)

    def fly_away(self):
        output = f'{self.get_crazy()} is an alien cat.'
        return output

AlienCat1 = AlienCat('Whiskers', 'Feline', '8', True, '135', 'Chomper', 'Jupiter')
print(AlienCat1.fly_away())

# Polymorphism



# Encapsulation



# Multiple Inheritance

