from menu_manager import MenuManager
import sys

def load_manager():
    """
    Creates and returns a new MenuManager instance.
    """
    return MenuManager()

def show_user_menu():
    """
    Displays the program menu and gets user input.
    """
    print("\n--- Restaurant Menu Management System ---")
    print("1. View menu")
    print("2. Add an item")
    print("3. Remove an item")
    print("4. Exit")

    choice = input("Please enter your choice (1-4): ")
    return choice

def add_item_to_menu(manager):
    """
    Asks for item details and adds it to the menu via the MenuManager.
    """
    name = input("Enter the new item's name: ")
    try:
        price = float(input("Enter the new item's price: "))
    except ValueError:
        print("Invalid price. Please enter a number.")
        return

    success, message = manager.add_item(name, price)
    print(message)

def remove_item_from_menu(manager):
    """
    Asks for an item's name and removes it from the menu via the MenuManager.
    """
    name_to_remove = input("Enter the name of the item to remove: ")
    if manager.remove_item(name_to_remove):
        print(f"Item '{name_to_remove}' was successfully removed.")
    else:
        print(f"Error: Item '{name_to_remove}' was not found in the menu.")

def show_restaurant_menu(manager):
    """
    Prints the current restaurant menu.
    """
    menu = manager.get_menu()
    print("\n--- Restaurant Menu ---")
    if not menu["items"]:
        print("The menu is currently empty.")
    else:
        for item in menu["items"]:
            print(f"- {item['name']:<20} ${item['price']:.2f}")

def main():
    """
    Main function to run the menu editor program.
    """
    manager = load_manager()
    
    while True:
        choice = show_user_menu()
        
        if choice == '1':
            show_restaurant_menu(manager)
        elif choice == '2':
            add_item_to_menu(manager)
        elif choice == '3':
            remove_item_from_menu(manager)
        elif choice == '4':
            success, message = manager.save_to_file()
            print(message)
            print("Exiting program.")
            sys.exit()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()