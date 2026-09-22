# Lesson 02 Evidence Pro-Forma

## Commit evidence (minimum 2)
- Commit 1 hash + message: a3ea9b037080a8487996c9430e56d4b056743255
- Commit 2 hash + message: 3135cfa2f7f716933727acd349e1889bbd329eb8
- Optional Commit 3 hash + message:

## Run evidence
- Command run: python lesson2_create_table.py
- Terminal output pasted below: no output in terminal look in db

## SQL/Python changes I made
- Added starter code from lesson

## Error and fix
- Error I hit: sqlite3.OperationalError: 2 values for 3 columns
- How I fixed it: Made sure to add another placeholder with 3 question marks ? instead of two

## Understanding check (answer in your own words)
1. Why do we use `commit()`?
To ensure the changes we made are saved and kept 

2. What does `PRIMARY KEY` mean?
An indivdual unique key that keeps track of record in a table

3. Why is `IF NOT EXISTS` useful when creating tables?

To ensure no duplicate tables are made

## Quality checklist
- [ YEs] Script runs without unhandled errors
- [ yES] I included at least 2 lesson commits
- [ yes] I showed inserts and saved changes
- [ ]yes I answered all questions in my own words
