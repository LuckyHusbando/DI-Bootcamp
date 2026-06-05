import psycopg2
from connect import DATABASE, USER, PASSWORD, HOST, PORT

connection = psycopg2.connect(database = DATABASE,
    user = USER,
    password = PASSWORD,
    host = HOST,
    port = PORT)

cursor = connection.cursor()

# IN THE END OF THE PROJECT, LAST STEP IS: CREATE A requirements.txt FILE:
# ON THE TERMINAL RUN: py -m pip freeze > requirements.txt 
# the requirements file SHOULD be pushed to github