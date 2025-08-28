from menu_item import MenuItem
from menu_manager import MenuManager

def show_user_menu():
    """
    Displays the program menu to the user and handles their input.
    """
    while True:
        print("\n--- Program Menu ---")
        print("View an Item (V)")
        print("Add an Item (A)")
        print("Delete an Item (D)")
        print("Update an Item (U)")
        print("Show the Menu (S)")
        print("Exit (E)")
        
        choice = input("Please enter your choice: ").upper()
        
        if choice == 'V':
            view_item()
        elif choice == 'A':
            add_item_to_menu()
        elif choice == 'D':
            remove_item_from_menu()
        elif choice == 'U':
            update_item_from_menu()
        elif choice == 'S':
            show_restaurant_menu()
        elif choice == 'E':
            print("\nExiting program...")
            show_restaurant_menu()
            break
        else:
            print("Invalid choice. Please try again.")

def view_item():
    """Asks the user for an item name and displays its details if found."""
    item_name = input("Enter the name of the item to view: ")
    item = MenuManager.get_by_name(item_name)
    if item:
        print(f"Item found: {item.item_name} - ${item.item_price}")
    else:
        print(f"Item '{item_name}' not found.")

def add_item_to_menu():
    """
    Prompts the user for item details and adds a new MenuItem.
    """
    item_name = input("Enter the new item's name: ")
    try:
        item_price = int(input("Enter the new item's price: "))
        if item_price < 0:
            raise ValueError
        item = MenuItem(item_name, item_price)
        item.save()
    except ValueError:
        print("Error: Price must be a non-negative integer.")

def remove_item_from_menu():
    """
    Prompts the user for an item name to remove.
    """
    item_name = input("Enter the name of the item to delete: ")
    
    # We first retrieve the item to get its full details for the MenuItem object
    item_to_delete = MenuManager.get_by_name(item_name)
    
    if item_to_delete:
        item_to_delete.delete()
    else:
        print(f"Error: Item '{item_name}' was not found in the menu.")

def update_item_from_menu():
    """
    Prompts the user for old and new item details to perform an update.
    """
    old_name = input("Enter the name of the item you want to update: ")
    
    # We need to retrieve the item first to ensure it exists
    item_to_update = MenuManager.get_by_name(old_name)
    
    if item_to_update:
        new_name = input("Enter the new name (press Enter to keep the same): ")
        new_price_str = input("Enter the new price (press Enter to keep the same): ")
        
        new_name_val = new_name if new_name else None
        new_price_val = None
        
        if new_price_str:
            try:
                new_price_val = int(new_price_str)
            except ValueError:
                print("Error: Price must be an integer. Update failed.")
                return
        
        item_to_update.update(new_name=new_name_val, new_price=new_price_val)
    else:
        print(f"Error: Item '{old_name}' not found.")

def show_restaurant_menu():
    """
    Retrieves and prints all items from the restaurant menu.
    """
    menu_items = MenuManager.all_items()
    if not menu_items:
        print("\nThe menu is currently empty.")
        return
        
    print("\n--- Restaurant Menu ---")
    for item in menu_items:
        print(f"- {item.item_name}: ${item.item_price}")

# Run the program
if __name__ == '__main__':
    show_user_menu()