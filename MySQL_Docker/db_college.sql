CREATE DATABASE IF NOT EXISTS college;
USE college;

CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    FirstName VARCHAR(100) NOT NULL,
    Surname VARCHAR(100) NOT NULL
);
INSERT INTO students(FirstName, Surname)
VALUES ("Aaradhya", "Agrawal"), ("Rashi", "Garg");
