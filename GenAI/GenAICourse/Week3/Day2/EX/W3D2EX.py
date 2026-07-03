#W3D2EX

#Exercise 1 - Pets

class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat:
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.color = age

    def walk(self):
        return f"{self.name} is just walking around."

class Siamese(Cat):
    def __init__(self, sounds):
        def __init__(self, sounds):
            self.sounds = sounds
            return f'{sounds}'

class Bengal(Cat):
    def __init__(self, sounds):
        self.sounds = sounds
        return f'{sounds}'

class Chartreux(Cat):
    def __init__(self, sounds):
        self.sounds = sounds
        return f'{sounds}'

Bengal = Cat("Sandy", 10)
Chartreux = Cat("Beauty", 5)
Siamese = Cat("Cleo", 2)

all_cats = [Bengal, Chartreux, Siamese]
sara_pets = Pets(all_cats)
sara_pets.walk()

#Exercise 2 - Dogs

class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f"{self.name} is barking loudly!"
    
    def run_speed(self):
        return f"{self.name}'s run speed is: {(self.weight / self.age) * 10}"
    
    def play(self, other_dog):
        if self.age >= other_dog.age:
            return(f"{self.name} out-played {other_dog.name}!")
        elif self.age <= self.age:
            return(f"{self.name} is still younger and they outplayed {other_dog.name}")
        else:
            return(f"These dogs love to play!")

Poodle = Dog("Pierre", 5, 20)
Puggit = Dog("Pepper", 10, 7)
Doberman = Dog("Goofy", 2, 30)
dog_names = [Poodle, Puggit, Doberman]

print(Poodle.bark())
print(Puggit.run_speed())
print(Doberman.play(Puggit))