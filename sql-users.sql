/*
In an aws aurora-mysql database, create the following tables if does not exist:
- users
*/ 
 CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);  

#anoter lab:

-- 
-- for the users table,alter the table and add the following columns:
-- add unique email constraint
-- add phone number column
-- add is_student column
-- add is_admin column
-- add is_active column
-- add an index to phone number column
-- add an index to name column
--
 ALTER TABLE users
 ADD CONSTRAINT unique_email UNIQUE (email);  

 --
-- create a trigger to update the is_active column when a user is created
--
 CREATE TRIGGER update_is_active 
 BEFORE INSERT ON users 
 FOR EACH ROW SET NEW.is_active = 1; 
 --
-- create a trigger to update the is_active column when a user is deleted
--
 CREATE TRIGGER update_is_active 
 BEFORE DELETE ON users 
 UPDATE users SET is_active = 0 WHERE id = OLD.id; 


-----------------

/*
for the users table, create an ansi query that returns the name,  and email address of all users.

for the users table, create an ansi query that returns the name,  and email address of each user based on the user id.

for the users table, create an ansi query that returns the name,  and email address of each user based on the email address.

for the users table, create an ansi query that returns the name,  and email address of each user based on the name;

select user based on name starting with three letters and the email address ending with .com, and id greater than 100.

for the users table, select users where name starts with three letters and create_at is between two dates.

for the users table, select the top 10 most recent users.

for the users table, select the first 10 rows.
*/
 SELECT name, email FROM users; 
 SELECT name, email FROM users WHERE id = 1; 
 SELECT name, email FROM users WHERE email = 'john.doe@example.com'; SELECT name, email FROM users WHERE name = 'John Doe'; 
 SELECT name, email FROM users WHERE name LIKE 'J%' AND email LIKE '%.com' AND id > 100; 
 SELECT name, email FROM users WHERE name LIKE 'J%' AND created_at BETWEEN '2020-01-01' AND '2020-12-31'; 
 SELECT name, email FROM users ORDER BY created_at DESC LIMIT 10;   
 SELECT name, email FROM users LIMIT 10; 