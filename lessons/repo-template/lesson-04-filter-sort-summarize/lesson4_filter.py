import sqlite3

connection = sqlite3.connect("school.db")

cursor = connection.cursor()

year_group = 10

cursor.execute(
    "SELECT name, year_group FROM students WHERE year_group = ? ORDER BY NAME",
    (year_group,)
)

rows = cursor.fetchall()
for row in rows:
    print(row)

cursor.execute("SELECT COUNT (*) FROM students")
total_students = cursor.fetchone()[0]

print("Total students", total_students)

connection.close()

