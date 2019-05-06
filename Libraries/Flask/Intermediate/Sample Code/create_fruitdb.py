# This python script creates a fruit database that will
# be used by the flask application

import sqlite3
from sqlite3 import Error

def create_connection():
    try:
        connection = sqlite3.connect('fruits.db')
        return connection
    except Error:
        print(Error)

def create_table(connection):
    cursor_obj = connection.cursor()
    cursor_obj.execute('''
        CREATE TABLE fruit(
            id integer PRIMARY KEY,
            name text,
            price real
        )
    ''')
    connection.commit()

def insert_values(connection):
    cursor_object = connection.cursor()
    cursor_object.execute('''
        INSERT INTO fruit values 
        (1, "Sour Sop", 23),
        (2, "Dragon Fruit", 67),
        (3, "Star apple", 33),
        (4 "Star fruit", 83)
    ''')
    connection.commit()

connection = create_connection()

try:
    create_table(connection)
except: 
    print('Oops, Database is already created!')

try:
    insert_values(connection)
except:
    print('Error inserting values :(')