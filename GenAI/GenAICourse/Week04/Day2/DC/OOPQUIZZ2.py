#OOPQUIZZ-2

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