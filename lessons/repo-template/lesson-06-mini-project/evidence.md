# Lesson 06 Evidence Pro-Forma

## Commit evidence (minimum 2)
- Commit 1 hash + message: d41ce43d5336ef43edf6d789670bf2d17e2b3efd
- Commit 2 hash + message: 834ec5238fa9015a049d83fab3f37640b54dee8f
- Optional Commit 3 hash + message:

## Run evidence
- Command run: python3 lesson6_project.py
- Terminal output pasted below:
1984 by George Orwell
Crime and punishment by Fyodor Dostoevsky
Holes by Louis Sachar
The Hobbit by J. R. R. Tolkien
War and peace by Leo Tolstoy
Wonder by R. J. Palacio


## SQL/Python changes I made
- I added three more books to the database
- added an option to add your own book to the database

## Error and fix
- Error I hit: sqlite3.OperationalError: table books has no column named authors
- How I fixed it:
This error was caused by a typo and I changed authors to author 

## Understanding check (answer in your own words)
1. Which skills from earlier lessons were reused here?
SELECT command and to fiter out the information you want to display in terminal. As well as basics such as creating a table and querying data. 

2. Which part of your program is SQL and which part is Python?
The cursor executing a create table command and inputting information using cursor to add default information. Python was connecting to the database and printing the title and author name. With inputting your own books name

3. What would you add next to improve the app?
A better GUI or an actual website, and more information that can be added so that users can actually learn something, such as a summary or ratings. 

## Quality checklist
- [ Yes ] Script runs without unhandled errors
- [ Yes ] I included at least 2 lesson commits
- [ Yes ] I included mini-project output evidence
- [ Yes ] I answered all questions in my own words
