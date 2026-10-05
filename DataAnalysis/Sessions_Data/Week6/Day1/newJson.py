import psycopg2
import requests
import json
import os
dir_path = os.path.dirname(os.path.realpath(__file__))


connection = psycopg2.connect(database = 'Countries',
    user = 'postgres',
    password = 'Tetriandoch',
    host = 'localhost',
    port = '5432')

cursor = connection.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS Countries(
               country_id SERIAL PRIMARY KEY,
               country_name VARCHAR (200) NOT NULL,
               capital VARCHAR (200),
               flag_png VARCHAR(200),
               region VARCHAR (200),
               population INTEGER NOT NULL)''')

connection.commit()

print('connection successfully made. Table was created')

response = requests.get('https://www.apicountries.com/countries')
data = response.json()

with open(f'{dir_path}/countries.json', "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

for i in range(10):
    country_name = data[i]['name']
    try:
        capital = data[i]['capital']
    except:
        capital = 'Unknown'
    if '\'' in capital:
        capital = capital.replace('\'', '`')    
    flag_png = data[i]['flags']['png']
    region = data[i]['region']
    population = data[i]['population']

    cursor.execute(f'''INSERT INTO countries (country_name, capital, flag_png, region, population)
                   VALUES ('{country_name}', '{capital}', '{flag_png}', '{region}', '{population}')''')
    
    connection.commit()

print('table successfully populated')

cursor.execute("SELECT * FROM countries")

rows = cursor.fetchall()

for row in rows:
    print(row)

cursor.close()
connection.close()
