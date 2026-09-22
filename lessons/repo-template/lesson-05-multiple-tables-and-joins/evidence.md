# Lesson 05 Evidence Pro-Forma

## Commit evidence (minimum 2)
- Commit 1 hash + message:
- Commit 2 hash + message:
- Optional Commit 3 hash + message:

## Run evidence
- Command run: python lesson5_join.py
- Terminal output pasted below:
('Ava', 'Science Club')
('Leo', 'Math Club')

## Typed-work confirmation
- Briefly describe how you typed your changes step-by-step (including at least one pause to run and check output):
I first create the table and ran to ensure that table was made and then typed out the code to put in the infomation of the students and the club, and ran again. I finished it off my typing the rest of the code and commit closing

## Prediction before run
- JOIN query version: 

SELECT students.name, courses.course_name
FROM students
JOIN courses ON students.id = courses.student_id

- My prediction (student-course pairs): It will output the sutdents name and course out
- What actually happened:
It outputted the accurate information with brackets

## SQL/Python changes I made
- Change 1: I added a scaling rank to courses
- Change 2: I added an option to input a new course in
- Why these changes were mine (not just starter code):
These changes were mine becasue 

## Error and fix
- Error I hit:
- How I fixed it:

## Understanding check (answer in your own words)
1. Why do we use more than one table?
2. What is the purpose of `JOIN`?
3. Which columns connect your two tables?

## Quality checklist
- [ ] Script runs without unhandled errors
- [ ] I included at least 2 lesson commits
- [ ] I included joined output evidence
- [ ] I showed a prediction and compared it to actual output
- [ ] I made at least 2 personal changes to the starter work
- [ ] I answered all questions in my own words
