import psycopg2
from menu_item import MenuItem

class MenuManager:
    @classmethod
    def get_by_name(cls, item_name):
        """
        Returns a single MenuItem object by its name.
        Returns None if no item is found.
        """
        conn = None
        try:
            conn = psycopg2.connect(
                dbname="restaurant_db",
                user="your_username",
                password="your_password",
                host="localhost",
                port="5432"
            )
            cur = conn.cursor()
            cur.execute(
                "SELECT item_name, item_price FROM Menu_Items WHERE item_name = %s;",
                (item_name,)
            )
            item_data = cur.fetchone()
            if item_data:
                name, price = item_data
                return MenuItem(name, price)
            else:
                return None
        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to PostgreSQL:", error)
            return None
        finally:
            if conn:
                cur.close()
                conn.close()

    @classmethod
    def all_items(cls):
        """Returns a list of all MenuItem objects from the table."""
        conn = None
        menu_items = []
        try:
            conn = psycopg2.connect(
                dbname="restaurant_db",
                user="your_username",
                password="your_password",
                host="localhost",
                port="5432"
            )
            cur = conn.cursor()
            cur.execute("SELECT item_name, item_price FROM Menu_Items;")
            rows = cur.fetchall()
            for row in rows:
                name, price = row
                menu_items.append(MenuItem(name, price))
            return menu_items
        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to PostgreSQL:", error)
            return []
        finally:
            if conn:
                cur.close()
                conn.close()

# Example Usage:
if __name__ == '__main__':
    # Add a new item
    item1 = MenuItem('Burger', 10)
    item1.save()

    # Get an item by name
    found_item = MenuManager.get_by_name('Burger')
    if found_item:
        print(f"Found Item: {found_item.item_name} - {found_item.item_price}")

    # Update the item
    found_item.update(new_price=12)

    # Get all items
    all_menu_items = MenuManager.all_items()
    print("\nAll Items:")
    for item in all_menu_items:
        print(f"Item: {item.item_name} - {item.item_price}")

    # Delete the item
    found_item.delete()
