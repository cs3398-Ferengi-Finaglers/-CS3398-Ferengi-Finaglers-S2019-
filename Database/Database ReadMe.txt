Setup Database: 
1. Download Postgres 
2. “Import data from file option”-> select file


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