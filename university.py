import sqlite3
conn = sqlite3.connect("university.db")
cur = conn.cursor()

cur.executescript("""
DROP TABLE IF EXISTS enrollments;
DROP TABLE IF EXISTS students;

CREATE TABLE students (
    student_id INTEGER PRIMARY KEY,
    name TEXT,
    department TEXT
);

CREATE TABLE enrollments (
    enroll_id INTEGER PRIMARY KEY,
    student_id INTEGER,
    course TEXT,
    marks INTEGER,
    FOREIGN KEY (student_id) REFERENCES students(student_id)
);

INSERT INTO students VALUES
(1, 'Ali', 'CS'), (2, 'Sara', 'SE'),
(3, 'Bilal', 'CS'), (4, 'Ayesha', 'AI');

INSERT INTO enrollments VALUES
(1, 1, 'Databases', 85),
(2, 1, 'AI', 78),
(3, 2, 'Databases', 92),
(4, 3, 'AI', 88),
(5, 4, 'Databases', 74);
""")
conn.commit()
print("Database created.")

print("\nSection 8: CS students")
cur.execute("""
SELECT name AS student_name, department
FROM students
WHERE department = 'CS'
ORDER BY name;
""")
for row in cur.fetchall():
    print(row)

print("\nSection 9: JOIN")
cur.execute("""
SELECT s.name, e.course, e.marks
FROM students s
INNER JOIN enrollments e ON s.student_id = e.student_id
ORDER BY e.marks DESC;
""")
for row in cur.fetchall():
    print(row)

print("\nSection 10: GROUP BY")
cur.execute("""
SELECT s.department, AVG(e.marks) AS avg_marks, COUNT(*) AS num_enrollments
FROM students s
JOIN enrollments e ON s.student_id = e.student_id
GROUP BY s.department
HAVING AVG(e.marks) > 75;
""")
for row in cur.fetchall():
    print(row)

conn.close()