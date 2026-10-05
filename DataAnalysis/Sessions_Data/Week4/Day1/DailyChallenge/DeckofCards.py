#Deck of Cards

import random

class Card:
    """
    Represents a single playing card with a suit and a value.
    """
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        """
        Returns a string representation of the Card object.
        This allows for readable printing of card instances.
        """
        return f"{self.value} of {self.suit}"

class Deck:
    """
    Represents a deck of 52 playing cards.
    """
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        """
        Populates the deck with all 52 cards.
        """
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        
        self.cards = [Card(suit, value) for suit in suits for value in values]

    def shuffle(self):
        """
        Shuffles the deck randomly.
        """
        if len(self.cards) < 52:
            print("Deck has fewer than 52 cards. Rebuilding and shuffling.")
            self.build()
        random.shuffle(self.cards)
        print("The deck has been shuffled.")

    def deal(self):
        """
        Deals a single card from the top of the deck.
        Removes the dealt card from the deck.
        Returns None if the deck is empty.
        """
        if not self.cards:
            print("No cards left in the deck.")
            return None
        return self.cards.pop()

# Example Usage:
if __name__ == "__main__":
    deck = Deck()
    print("Initial deck created.")
    
    deck.shuffle()
    
    print("\nDealing a card...")
    card1 = deck.deal()
    if card1:
        print(f"Dealt card: {card1}")
    
    print("\nDealing another card...")
    card2 = deck.deal()
    if card2:
        print(f"Dealt card: {card2}")
        
    print(f"\nNumber of cards left in the deck: {len(deck.cards)}")
