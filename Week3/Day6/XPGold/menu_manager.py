import json

class MenuManager:
    def __init__(self, file_path="restaurant_menu.json"):
        """
        Initializes the MenuManager by loading the menu from the specified JSON file.
        """
        self.file_path = file_path
        self.menu = self._load_menu()

    def _load_menu(self):
        """
        Reads the menu data from the JSON file.
        """
        try:
            with open(self.file_path, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"Error: The file '{self.file_path}' was not found.")
            return {"items": []} # Return an empty menu if the file doesn't exist

    def add_item(self, name, price):
        """
        Adds a new item to the menu in memory.
        """
        # Ensure name and price are not empty and price is a valid number
        if not name or not isinstance(price, (int, float)) or price <= 0:
            return False, "Invalid item name or price."

        self.menu["items"].append({"name": name, "price": price})
        return True, "Item added successfully."

    def remove_item(self, name):
        """
        Removes an item from the menu in memory if it exists.
        Returns True if successful, False otherwise.
        """
        # Use a list comprehension to rebuild the list without the item to remove
        initial_count = len(self.menu["items"])
        self.menu["items"] = [item for item in self.menu["items"] if item["name"] != name]
        
        # Check if the list size changed to see if an item was removed
        return len(self.menu["items"]) < initial_count

    def save_to_file(self):
        """
        Saves the current state of the menu to the JSON file.
        """
        try:
            with open(self.file_path, 'w') as f:
                json.dump(self.menu, f, indent=4)
            return True, "Menu saved successfully."
        except IOError as e:
            return False, f"Error saving file: {e}"

    def get_menu(self):
        """
        Returns the current menu.
        """
        return self.menu
    
