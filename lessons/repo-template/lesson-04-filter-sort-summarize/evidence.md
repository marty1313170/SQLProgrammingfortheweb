# Lesson 04 Evidence Pro-Forma

## Commit evidence (minimum 2)
- Commit 1 hash + message:
- Commit 2 hash + message:
- Optional Commit 3 hash + message:

## Run evidence
- Command run: python lesson4_filter.py
- Terminal output pasted below: 
('James', 10)
Total students 3

## Typed-work confirmation
- Briefly describe how you typed your changes step-by-step (including at least one pause to run and check output):
I first wrote out of the extension of the SELECT command, and checked that it would receive the correct information from the SQLite datebase

## Prediction before run
- Query version: 
SELECT name, year_group FROM students WHERE year_group = ? ORDER BY NAME

- My prediction (filtered rows, order, or count):
It will output basic lines

- What actually happened:
It outputted with no formatting

## SQL/Python changes I made
- Change 1: Added a seperate count to know how much studnets are in that year group 
- Change 2: Added an input to know what year the user wanted to search
- Why these changes were mine (not just starter code):
They give the user more personlisation and help the user go thorugh code quickly and input() allowed the result to flexible and not be hardcoded

## Error and fix
- Error I hit:
  File "c:\Users\martin.han1\SQLUNIT\lessons\repo-template\lesson-04-filter-sort-summarize\lesson4_filter.py", line 27
    if 
       ^
SyntaxError: invalid syntax
- How I fixed it:

Fixed syntax code

## Understanding check (answer in your own words)
1. What does `WHERE` do?
WHERE tells the database to sort and only pick out the data that has that specific year group
2. Why is `?` used in the query?
It is used as an placeholder or parameter in the query

3. What does `COUNT(*)` tell you in this lesson?
COUNT, tells me that that for every result count it, and add it to the total once.

## Quality checklist
- [ Yes ] Script runs without unhandled errors
- [ Yes ] I included at least 2 lesson commits
- [ Yes ] I included filtered/sorted summary evidence
- [ Yes ] I showed a prediction and compared it to actual output
- [ Yes ] I made at least 2 personal changes to the starter work
- [ Yes ] I answered all questions in my own words
