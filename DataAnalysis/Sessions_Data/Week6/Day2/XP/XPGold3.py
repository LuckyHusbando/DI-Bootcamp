import psycopg2
import bcrypt

def auth_cli_database():
    logged_in = None

    # Database connection parameters
    DB_NAME = "your_db_name"
    DB_USER = "your_user"
    DB_PASSWORD = "your_password"
    DB_HOST = "localhost"

    def get_db_connection():
        """Establishes and returns a database connection."""
        return psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST
        )

    def login_user():
        """Handles the login process with database lookup and password validation."""
        nonlocal logged_in
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        
        try:
            conn = get_db_connection()
            cur = conn.cursor()
            cur.execute("SELECT password_hash FROM users WHERE username = %s", (username,))
            result = cur.fetchone()
            
            if result:
                password_hash = result[0].encode('utf-8')
                if bcrypt.checkpw(password.encode('utf-8'), password_hash):
                    logged_in = username
                    print("You are now logged in.")
                else:
                    print("Invalid password.")
            else:
                print("User not found.")
                signup_option = input("Would you like to sign up? (yes/no): ").lower()
                if signup_option == "yes":
                    signup_user()

        except psycopg2.Error as e:
            print(f"Database error: {e}")
        finally:
            if conn:
                cur.close()
                conn.close()

    def signup_user():
        """Handles the signup process, checking for unique username and encrypting the password."""
        nonlocal logged_in
        
        while True:
            username = input("Choose a new username: ")
            try:
                conn = get_db_connection()
                cur = conn.cursor()
                cur.execute("SELECT 1 FROM users WHERE username = %s", (username,))
                if cur.fetchone():
                    print("This username already exists. Please choose a different one.")
                    continue
                else:
                    break
            except psycopg2.Error as e:
                print(f"Database error: {e}")
                return
            finally:
                if conn:
                    cur.close()
                    conn.close()

        password = input("Choose a password: ")
        password_bytes = password.encode('utf-8')
        hashed_password = bcrypt.hashpw(password_bytes, bcrypt.gensalt())
        
        try:
            conn = get_db_connection()
            cur = conn.cursor()
            cur.execute(
                "INSERT INTO users (username, password_hash) VALUES (%s, %s)",
                (username, hashed_password.decode('utf-8'))
            )
            conn.commit()
            print("Signup successful! You can now log in.")
            logged_in = username
        except psycopg2.Error as e:
            print(f"Database error: {e}")
            conn.rollback()
        finally:
            if conn:
                cur.close()
                conn.close()

    while True:
        command = input("Enter 'login', 'signup', or 'exit': ").lower()

        if command == "exit":
            print("Exiting...")
            break
        elif command == "login":
            login_user()
        elif command == "signup":
            signup_user()
        else:
            print("Invalid command.")

# Uncomment the line below to run the database-based CLI
# auth_cli_database()