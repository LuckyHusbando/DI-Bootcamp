import requests
import psycopg2
import random

# Database connection details
DB_NAME = "your_db_name"
DB_USER = "your_user"
DB_PASSWORD = "your_password"
DB_HOST = "localhost"

def get_db_connection():
    """Establishes and returns a database connection."""
    try:
        conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST
        )
        return conn
    except psycopg2.Error as e:
        print(f"Error connecting to the database: {e}")
        return None

def fetch_all_countries():
    """Fetches all countries from the REST Countries API."""
    url = "https://restcountries.com/v3.1/all"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from API: {e}")
        return None

def populate_database_with_countries():
    """Fetches 10 random countries and populates the database."""
    all_countries = fetch_all_countries()
    if not all_countries:
        return

    random_countries = random.sample(all_countries, 10)
    
    countries_to_insert = []
    for country in random_countries:
        name = country.get('name', {}).get('common', 'N/A')
        capital = country.get('capital', ['N/A'])[0] if country.get('capital') else 'N/A'
        flag_url = country.get('flags', {}).get('svg', 'N/A')
        subregion = country.get('subregion', 'N/A')
        population = country.get('population', 0)
        
        countries_to_insert.append((name, capital, flag_url, subregion, population))
    
    conn = get_db_connection()
    if conn is None:
        return

    try:
        cur = conn.cursor()
        
        # Use executemany for efficient bulk insertion
        insert_query = """
        INSERT INTO countries (name, capital, flag, subregion, population)
        VALUES (%s, %s, %s, %s, %s)
        """
        cur.executemany(insert_query, countries_to_insert)
        conn.commit()
        print(f"Successfully inserted {len(countries_to_insert)} countries into the database.")
        
    except psycopg2.Error as e:
        print(f"Database error during insertion: {e}")
        conn.rollback()
    finally:
        if conn:
            cur.close()
            conn.close()

# Example usage
if __name__ == '__main__':
    populate_database_with_countries()
