import sqlite3

connection = sqlite3.connect("school.db")

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    year_group INTEGER,
    favourite_subject TEXT,
    detentions INTEGER
)
""")

cursor.execute("DELETE FROM students")



cursor.execute("INSERT INTO students (name, year_group, favourite_subject, detentions) VALUES (?, ?)", ("James", 10, "English", 0))
cursor.execute("INSERT INTO students (name, year_group,  favourite_subject, detentions) VALUES (?, ?)", ("Leo", 12, "Math", 2))
cursor.execute("INSERT INTO students (name, year_group  , favourite_subject , detentions) VALUES (?, ?)", ("Jimmy", 8, "Science", 19))



connection.commit()

connection.close()

"""
Create the script shown above.
Run it in VS Code.
Change one name value and run it again.
Discuss why IF NOT EXISTS is useful.

IF NOT EXISTS is useful because it ensures that you don't create a duplicate table with the same name

Identify which column is the primary key.
id is the primary key.

"""


"""
Exit Check

Why do we use commit()?

To keep the changes we made to the database so it doesn't revert

What does PRIMARY KEY mean?

It is the unique key given to each record to prevent duplicates and maintain integrity
"""