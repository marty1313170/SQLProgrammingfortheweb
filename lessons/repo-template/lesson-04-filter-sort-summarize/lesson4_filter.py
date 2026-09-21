import sqlite3

connection = sqlite3.connect("school.db")

cursor = connection.cursor()

ask_input = input("What year are you looking for")

year_group = ask_input

cursor.execute(
    "SELECT name, year_group FROM students WHERE year_group = ? ORDER BY NAME",
    (year_group,)
)



rows = cursor.fetchall()
for row in rows:
    print(row)

cursor.execute("SELECT COUNT (*) FROM students")
total_students = cursor.fetchone()[0]

rows = cursor.fetchall()
for row in rows:
    print(row)

print("Total students", total_students)

year_total = 0

if row[0] == year_group:
    year_total + 1
    print(year_total)
else:
    print(year_total)
    

connection.close()

