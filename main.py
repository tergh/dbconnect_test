import sqlite3

# create database connection
connection = sqlite3.connect("books.db")

# create cursor
cursor = connection.cursor()

# execute SQL query
cursor.execute("SELECT * FROM Customer;")

results = cursor.fetchall()

for record in results:
    print(record)

# make changes permanent
connection.commit()

# destroy database connection (and cursor)
connection.close()