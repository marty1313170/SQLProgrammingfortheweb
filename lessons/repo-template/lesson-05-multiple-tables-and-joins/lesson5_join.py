import sqlite3

connection = sqlite3.connect("school.db")


cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
id INTEGER PRIMARY KEY,
name TEXT NOT NULL,
year_group INTEGER
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS courses (
id INTEGER PRIMARY KEY,
course_name TEXT NOT NULL,
student_id INTEGER,
scaling_ranking FLOAT

)
""")

c = input("Put in a new course")
a = input("Whats your first name")
b = input("what is the scaling rank for this course?")

cursor.execute("DELETE FROM students")
cursor.execute("DELETE FROM courses")

cursor.execute(
    "INSERT INTO students (name, year_group) VALUES (?, ?)",
    ("Ava", 10)
    )
ava_id = cursor.lastrowid


cursor.execute(
    "INSERT INTO students (name, year_group) VALUES(?, ?)",
    ("Leo", 11)
)
leo_id = cursor.lastrowid

cursor.execute(
    "INSERT INTO courses (course_name, student_id, scaling_ranking) VALUES (?, ?, ?)",
    ("Science Club", ava_id, 93.95)
)

cursor.execute(
    f"INSERT INTO courses (course_name, student_id, scaling_ranking) VALUES (?, ?, ?)",
    (c, a, b)
)

cursor.execute(
    "INSERT INTO courses (course_name, student_id, scaling_ranking) VALUES (?, ?, ?)",
    ("Math Club", leo_id, 85.32)
)

cursor.execute("""
SELECT students.name, courses.course_name
FROM students
JOIN courses ON students.id = courses.student_id
""")

rows = cursor.fetchall()
for row in rows:
    print(row)

connection.commit()
connection.close()