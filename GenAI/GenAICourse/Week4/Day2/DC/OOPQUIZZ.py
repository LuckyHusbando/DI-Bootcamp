#OOPQUIZZ

# Part 1 - Object Oriented Programming Quizz:

# 1. What is a class?
# A blueprint or template for creating objects. It defines structure (attributes/data) and behavior (methods/functions) that the created objects will share.

# 2. What is an instance?
# A specific, concrete object created from a class blueprint.

# 3. What is encapsulation?
# The practice of bundling data and the methods that act on that data into a single unit (a class), while restricting direct outside access to the object's internal state. Typically represented with prefix _ or __.

# 4. What is abstraction?
# The concept of hiding complex implementation details from the user and only exposing essential, high-level features. In Pthon, this is often implemented using the ABC (Abstract Base Classes) module.

# 5. What is inheritance?
# A mechanism where a new class (child or subclass) absorbs attributes and methods of an existing class (parent or superclass).

# 6. What is multiple inheritance?
# A feature where a single class can inherit attributes or methods from more than one parent class simultaneously. 

# 7. What is polymorphism?
# In Latin, this means "Multiple Forms". In Python, this is the ability for different objects to be treated as instances of the same class through a common interface.

# 8. What is method resolution order or MRO?
# The speciic, predictable sequence in which Python searches through a hierachy of classes to find a method or attribute, particularly when multiple inheritance is involved.

#Part 2 - Create a deck of cards class

import random

class Card:
    """Represents a single playing card."""
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        #This makes the card look nice when printed.
        return f"{self.value} of {self.suit}"

class Deck:
    """Represents a standard 52 card deck."""
    #Using class attributes to store the constant valid suits and values.
    _suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    _values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

    def __init__(self):
        #This uses composition, not inheritance. The deck has cards.
        self.cards = []
        #Populate and shuffle deck on creation
        self.shuffle()

    def shuffle(self):
        """Ensure deck has all 52 cards and rearranges them randomly."""
        #Uses a list comprehension to build exactly 52 card instances.
        self.cards = [Card(suit, value) for suit in self._suits for value in self._values]

        #Randomize the list in place
        random.shuffle(self.cards)

    def deal(self):
        """Deals a single card from the deck. Removes it from the deck."""
        if not self.cards:
            print("The deck is empty!")
            return None
        
        #Pop() removes and returns the last item in the list
        return self.cards.pop()
    
#---Example Usage---

if __name__ == "__main__":
    my_deck = Deck()

    print(f"Cards in deck: {len(my_deck.cards)}")
    
    dealt_card = my_deck.deal()
    print(f"Dealt card: {dealt_card}")

    print(f"Cards remaining: {len(my_deck.cards)}")