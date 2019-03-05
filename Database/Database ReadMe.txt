Setup Database: 
1. Download Postgres 
2. “Import data from file option”-> select file (downloaded from Github)


A. Login


Table Name: “user_info”
Columns: 
* “user_id” : numerical id of new user; integer; auto increments; primary key; CANNOT be null 
* “username” : character username of user; VARCHAR(255); unique; CANNOT be null 
* “password”: character password of user; VARCHAR(255); CANNOT be null
* “name“: text name of the user; VARCHAR(255); CANNOT be null
* “email” : email of user; VARCHAR(255); CANNOT be null


Script to add new user:


INSERT INTO user_info (username, password, name, email)
VALUES
      ('myName', 'somePass8', 'Ana Pryamachenko', 'apryvdfh@gmail.com');


Note: the user_id will generate automatically, there is no need to add one; current example uses strings but can use string variables as well


Script to test username and password:


SELECT user_id
FROM user_info
WHERE password = 'somePass8' AND username = 'myName';


Note: the user_id keeps track of the user and is used to jump from table to table. We need to select it to use it for questionnaire table (coming soon) ; Also, current example uses strings can use string variables to do the same thing


B. Questionnaire


Table Name: “questionnaire”
Columns: 
* “user_id” : numerical id of user; integer; DOES NOT auto increments; primary key; CANNOT be null 
* “question1” : one character answer of user (A, B, C, D, etc); character; CANNOT be null 
* “question2” : one character answer of user (A, B, C, D, etc); character; CANNOT be null
* “question3” : one character answer of user (A, B, C, D, etc); character; CANNOT be null 
* “question4” : one character answer of user (A, B, C, D, etc); character; CANNOT be null 
* “question5” : one character answer of user (A, B, C, D, etc); character; CANNOT be null 
* “question6” : one character answer of user (A, B, C, D, etc); character; CANNOT be null 
* “question7” : one character answer of user (A, B, C, D, etc); character; CANNOT be null 
* “question8” : one character answer of user (A, B, C, D, etc); character; CANNOT be null 
* “question9” : one character answer of user (A, B, C, D, etc); character; CANNOT be null 
* “question10” : one character answer of user (A, B, C, D, etc); character; CANNOT be null 


Script to add user answers to DB (MUST KNOW user_id and answers to questions):


INSERT INTO questionnaire (user_id, question1, question2, question3, question4, question5, question6, question7, question8, question9, question10)
VALUES
     (1, 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A');




Note: The user_id is not auto generated because we need to use it to keep track of the user_info in the other table; The user_id must match to the user_info table user_id. In this example, actual values are used but this also works with variables.