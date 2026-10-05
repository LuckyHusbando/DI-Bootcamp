-- Create the Book table
CREATE TABLE Book (
    book_id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255) NOT NULL
);

-- Insert books
INSERT INTO Book (title, author) VALUES
('Alice In Wonderland', 'Lewis Carroll'),
('Harry Potter', 'J.K Rowling'),
('To kill a mockingbird', 'Harper Lee');

-- Create the Student table with a CHECK constraint for age
CREATE TABLE Student (
    student_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL UNIQUE,
    age INTEGER,
    CHECK (age <= 15)
);

-- Insert students
INSERT INTO Student (name, age) VALUES
('John', 12),
('Lera', 11),
('Patrick', 10),
('Bob', 14);

-- Create the Library (Junction) table
CREATE TABLE Library (
    book_fk_id INTEGER REFERENCES Book(book_id) ON DELETE CASCADE ON UPDATE CASCADE,
    student_fk_id INTEGER REFERENCES Student(student_id) ON DELETE CASCADE ON UPDATE CASCADE,
    borrowed_date DATE,
    PRIMARY KEY (book_fk_id, student_fk_id)
);

-- Insert records into the junction table
INSERT INTO Library (student_fk_id, book_fk_id, borrowed_date) VALUES
((SELECT student_id FROM Student WHERE name = 'John'), (SELECT book_id FROM Book WHERE title = 'Alice In Wonderland'), '2022-02-15'),
((SELECT student_id FROM Student WHERE name = 'Bob'), (SELECT book_id FROM Book WHERE title = 'To kill a mockingbird'), '2021-03-03'),
((SELECT student_id FROM Student WHERE name = 'Lera'), (SELECT book_id FROM Book WHERE title = 'Alice In Wonderland'), '2021-05-23'),
((SELECT student_id FROM Student WHERE name = 'Bob'), (SELECT book_id FROM Book WHERE title = 'Harry Potter'), '2021-08-12');

-- Select all columns from the junction table
SELECT * FROM Library;

-- Select the name of the student and the title of the borrowed books
SELECT s.name AS student_name, b.title AS book_title
FROM Library AS l
JOIN Student AS s ON l.student_fk_id = s.student_id
JOIN Book AS b ON l.book_fk_id = b.book_id;

-- Select the average age of the children that borrowed 'Alice in Wonderland'
SELECT AVG(s.age)
FROM Library AS l
JOIN Student AS s ON l.student_fk_id = s.student_id
JOIN Book AS b ON l.book_fk_id = b.book_id
WHERE b.title = 'Alice In Wonderland';

DELETE FROM Student WHERE name = 'John';
