#XP Ninja

#Exercise 1

import json
import os
import re

# Function to create or load the menu file
def get_menu(filename="valentines_menu.json"):
    """Creates an empty menu file if it doesn't exist, or loads the existing one."""
    if not os.path.exists(filename):
        with open(filename, 'w') as f:
            json.dump({"valentines_specials": []}, f, indent=4)
    with open(filename, 'r') as f:
        return json.load(f)

# Function to save the menu to the file
def save_menu(menu, filename="valentines_menu.json"):
    """Saves the updated menu dictionary to the JSON file."""
    with open(filename, 'w') as f:
        json.dump(menu, f, indent=4)

# Function to validate a new menu item
def validate_item(item_name, item_price):
    """Checks if the item name and price follow the Valentine's Day rules."""
    
    # Rule 1: Each word in the name begins with an uppercase letter
    # and the first word begins with 'V'. Connection words are lowercase.
    words = item_name.split()
    if not words[0].startswith('V'):
        print("Error: The first word must start with a capital 'V'.")
        return False
    
    # Check each word for proper capitalization
    for word in words:
        if word.lower() in ["of", "and", "the", "for", "with", "a", "an"]:
            if not word.islower():
                print(f"Error: Connection word '{word}' must be in lowercase.")
                return False
        elif not word.istitle():
            print(f"Error: Word '{word}' must start with an uppercase letter.")
            return False

    # Rule 2: Name must contain at least two 'e's and no numbers.
    if item_name.lower().count('e') < 2:
        print("Error: The item name must contain at least two 'e's.")
        return False
    if any(char.isdigit() for char in item_name):
        print("Error: The item name cannot contain numbers.")
        return False

    # Rule 3: Price must match the pattern XX.14
    if not re.match(r'^\d{2}\.14$', item_price):
        print("Error: The price must be in the format XX.14 (e.g., 25.14).")
        return False
    
    return True

# Function to display the heart
def display_heart():
    """Prints a heart shape made of asterisks."""
    print()
    print("           *** ***")
    print("         * * *")
    print("        * *")
    print("        * *")
    print("         * *")
    print("          * *")
    print("           * *")
    print("            * *")
    print("             * *")
    print("              * *")
    print("               *")
    print()

def main():
    """Main function to run the Valentine's Day menu manager."""
    menu = get_menu()
    
    display_heart()
    print("Welcome to the Valentine's Day Menu Manager! 💖")
    print("Current Special Valentine's Day Items:")
    if menu["valentines_specials"]:
        for item in menu["valentines_specials"]:
            print(f"- {item['name']} (Price: ${item['price']})")
    else:
        print("The menu is currently empty.")

    while True:
        print("\n--- Add a new Valentine's item ---")
        item_name = input("Enter the name of the new item: ")
        item_price = input("Enter the price (e.g., 25.14): ")
        
        if validate_item(item_name, item_price):
            new_item = {"name": item_name, "price": item_price}
            menu["valentines_specials"].append(new_item)
            save_menu(menu)
            print("\nItem successfully added!")
        
        choice = input("Would you like to add another item? (yes/no): ").lower()
        if choice != 'yes':
            break

if __name__ == "__main__":
    main()

#Exercise 2

# Character Class
# The Character class is responsible for generating a single character. It handles rolling the dice for each of the six attributes.
import random

class Character:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.stats = self.generate_stats()

    def roll_stats(self):
        """Rolls four 6-sided dice and returns the sum of the highest three."""
        rolls = [random.randint(1, 6) for _ in range(4)]
        rolls.sort(reverse=True)
        return sum(rolls[:3])

    def generate_stats(self):
        """Generates all six attributes for the character."""
        return {
            "Strength": self.roll_stats(),
            "Dexterity": self.roll_stats(),
            "Constitution": self.roll_stats(),
            "Intelligence": self.roll_stats(),
            "Wisdom": self.roll_stats(),
            "Charisma": self.roll_stats()
        }

    def to_dict(self):
        """Returns the character's data as a dictionary."""
        return {
            "name": self.name,
            "age": self.age,
            "stats": self.stats
        }

    def __str__(self):
        """Returns a nicely formatted string representation of the character."""
        stats_str = "\n".join([f"    {stat}: {score}" for stat, score in self.stats.items()])
        return (f"Character Name: {self.name}\n"
                f"Age: {self.age}\n"
                f"Stats:\n{stats_str}")

import json

class Game:
    def __init__(self):
        self.players = []

    def create_characters(self):
        """Asks for the number of players and creates a character for each."""
        try:
            num_players = int(input("How many players are playing? "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            return

        for i in range(num_players):
            print(f"\n--- Player {i + 1} ---")
            name = input("Enter your character's name: ")
            age = input("Enter your character's age: ")
            
            new_character = Character(name, age)
            self.players.append(new_character)
            print(f"Character '{new_character.name}' created!")

    def export_data(self):
        """Exports the player data to a JSON and a TXT file."""
        if not self.players:
            print("No characters to export. Please create characters first.")
            return

        # Export to JSON
        with open("dnd_characters.json", "w") as json_file:
            json_data = [player.to_dict() for player in self.players]
            json.dump(json_data, json_file, indent=4)
        print("Character data exported to dnd_characters.json")

        # Export to TXT
        with open("dnd_characters.txt", "w") as txt_file:
            for player in self.players:
                txt_file.write(str(player) + "\n\n")
        print("Character data exported to dnd_characters.txt")
        
        print("\nAll characters have been created and saved!")


# Main execution
if __name__ == "__main__":
    game = Game()
    game.create_characters()
    game.export_data()
