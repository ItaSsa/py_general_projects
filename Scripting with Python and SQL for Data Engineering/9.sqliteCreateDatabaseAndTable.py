import sqlite3

connection = sqlite3.connect('sample.db')

table = '''CREATE TABLE people(
        id integer primary key,
        name TEXT,
        surname TEXT
)'''
cursor = connection.cursor()
cursor.execute(table)
connection.commit()