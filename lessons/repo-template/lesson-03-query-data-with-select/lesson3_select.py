import sqlite3

connection = sqlite3.connect("school.db")

cursor = connection.cursor()

cursor.execute("SELECT name FROM students")

rows = cursor.fetchall()



for row in rows:
    print(f"The students name is {row[0]}")


connection.close()