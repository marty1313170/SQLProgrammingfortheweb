import sqlite3

connection = sqlite3.connect("school.db")

cursor = connection.cursor()

cursor.execute("SELECT id, name, year_group FROM students")

rows = cursor.fetchall()


for row in rows:
    print(row)


connection.close()