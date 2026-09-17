import sqlite3

connection = sqlite3.connect("school.db")

print("Database connected")

connection.close()

print("Hello you are opening an connection to the database")
print("Database closed?")

"""
- What is the difference between Python and SQLite?

SQlite is a database engine that runs data in a file and runs SQL while Python is a programming language, which talks with SQLite

- What file was created when the script ran?

school.db was created

- What does the connection do?

It creates the file and opens an connection to allow python to talk to the data
"""