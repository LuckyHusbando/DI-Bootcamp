import psycopg2

class MenuItem:
    def __init__(self, name, price):
        self.item_name = name
        self.item_price = price

    def save(self):
        """Saves the menu item to the Menu_Items table."""
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
                "INSERT INTO Menu_Items (item_name, item_price) VALUES (%s, %s);",
                (self.item_name, self.item_price)
            )
            conn.commit()
            print(f"Item '{self.item_name}' saved successfully.")
        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to PostgreSQL:", error)
        finally:
            if conn:
                cur.close()
                conn.close()

    def delete(self):
        """Deletes the menu item from the Menu_Items table."""
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
                "DELETE FROM Menu_Items WHERE item_name = %s AND item_price = %s;",
                (self.item_name, self.item_price)
            )
            conn.commit()
            if cur.rowcount > 0:
                print(f"Item '{self.item_name}' deleted successfully.")
            else:
                print(f"No item named '{self.item_name}' with price '{self.item_price}' was found to delete.")
        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to PostgreSQL:", error)
        finally:
            if conn:
                cur.close()
                conn.close()

    def update(self, new_name=None, new_price=None):
        """Updates the name and/or price of the menu item."""
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
            query_parts = []
            params = []
            
            if new_name is not None:
                query_parts.append("item_name = %s")
                params.append(new_name)
            if new_price is not None:
                query_parts.append("item_price = %s")
                params.append(new_price)
            
            if not query_parts:
                print("No new name or price provided for update.")
                return

            params.extend([self.item_name, self.item_price])
            
            query = f"UPDATE Menu_Items SET {', '.join(query_parts)} WHERE item_name = %s AND item_price = %s;"
            
            cur.execute(query, tuple(params))
            conn.commit()
            if cur.rowcount > 0:
                print(f"Item '{self.item_name}' updated successfully.")
            else:
                print(f"No item named '{self.item_name}' with price '{self.item_price}' was found to update.")

            # Update the object's attributes if the update was successful
            if new_name is not None:
                self.item_name = new_name
            if new_price is not None:
                self.item_price = new_price

        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to PostgreSQL:", error)
        finally:
            if conn:
                cur.close()
                conn.close()
