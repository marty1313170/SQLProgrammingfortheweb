import sqlite3
import sys

connection = sqlite3.connect("school.db")

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS books (
id INTEGER PRIMARY KEY,
title TEXT NOT NULL,
author TEXT NOT NULL,
year_released INTEGER NOT NULL,
units_sold INTEGER NOT NULL
)
""")

cursor.execute("DELETE FROM books")

# Menu
option = input("Press 1 to add an book, Press 2 to show all books, Press 3 exit")







cursor.execute("INSERT INTO books (title, author, year_released, units_sold) VALUES (?, ?, ?, ?)", (
    "Holes", "Louis Sachar", 1988, 12000000
))

cursor.execute("INSERT INTO books (title, author, year_released, units_sold) VALUES (?, ?, ?, ?)", (
    "Wonder", "R. J. Palacio", 2010, 6000000
))


cursor.execute("INSERT INTO books (title, author, year_released, units_sold) VALUES (?, ?, ?, ?)", (
    "The Hobbit", "J. R. R. Tolkien", 1937, 32000000
))

cursor.execute("INSERT INTO books (title, author, year_released, units_sold) VALUES (?, ?, ?, ?)", (
    1984,"George Orwell", 1949, 30000000)
)

cursor.execute("INSERT INTO books (title, author, year_released, units_sold) VALUES (?, ?, ?, ?)", (
    "War and peace", "Leo Tolstoy", 1867, 36000000
))

cursor.execute("INSERT INTO books (title, author, year_released, units_sold) VALUES (?, ?, ?, ?)", (
    "Crime and punishment", "Fyodor Dostoevsky", 1866 , 30000000
))




if option == "1":
    a = input("Input a book name")
    b = input("Who wrote this book")
    c = input("What year was this book released")
    d = input("How much copies are sold")

    cursor.execute("INSERT INTO books (title, author, year_released, units_sold) VALUES (?, ?, ?, ?)", (
    a, b, c , d
    ))
elif option == "2":
    cursor.execute("SELECT title, author FROM books ORDER BY title")
    for title, author in cursor.fetchall():
        print(f"{title} by {author}")
elif option == "3":
    sys.exit()


connection.commit()
connection.close()