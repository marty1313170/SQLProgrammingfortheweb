# Lesson 03 Evidence Pro-Forma

## Commit evidence (minimum 2)
- Commit 1 hash + message:
- Commit 2 hash + message:
- Optional Commit 3 hash + message:

## Run evidence
- Command run: python lesson3_select.py
- Terminal output pasted below:

(1, 'James', 10)
(2, 'Leo', 12)
(3, 'Jimmy', 8)

## Typed-work confirmation
- Briefly describe how you typed your changes step-by-step (including at least one pause to run and check output):

I adde a new column named 'detentions', and made a check by ensuring that the column existed and successfully outputted

## Prediction before run
- Query version: 
- My prediction (rows/columns or sample output):
The columns and rows will be outputted


- What actually happened:
(1, 'James', 10)
(2, 'Leo', 12)
(3, 'Jimmy', 8)

## SQL/Python changes I made
- Change 1: New column
- Change 2: I added an f string to just retrieve one part of the db
- Why these changes were mine (not just starter code): 
They were extension of the starter code

## Error and fix
- Error I hit:

  File "c:\Users\martin.han1\SQLUNIT\lessons\repo-template\lesson-03-query-data-with-select\lesson3_select.py", line 14
    print(f"The students row is"row[0])
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: invalid syntax. Perhaps you forgot a comma?

- How I fixed it:

Properly formatting the f string

## Understanding check (answer in your own words)
1. What is the job of `SELECT`?
To SELECT a certain column in the database

2. What type of value does `fetchall()` return?
All the data in the database

3. How did your output change when you selected fewer columns?
It only outputted the name or year_group by its self

## Quality checklist
- [ ] Script runs without unhandled errors
- [ ] I included at least 2 lesson commits
- [ ] I included query output evidence
- [ ] I showed a prediction and compared it to actual output
- [ ] I made at least 2 personal changes to the starter work
- [ ] I answered all questions in my own words
