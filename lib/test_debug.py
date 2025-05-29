
import sys
import os
import sqlite3
import pytest  # <-- Add this

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lib.models.Teacher import Teacher
from lib.models.student import Student
from lib.models.SchoolClass import SchoolClass
from lib.models.enrolment import Enrollment

DB_NAME = "school.db"

def setup_database():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS teachers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        email TEXT NOT NULL
    )''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        email TEXT NOT NULL
    )''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS classes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        teacher_id INTEGER NOT NULL,
        FOREIGN KEY (teacher_id) REFERENCES teachers(id)
    )''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS enrollments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER NOT NULL,
        class_id INTEGER NOT NULL,
        FOREIGN KEY (student_id) REFERENCES students(id),
        FOREIGN KEY (class_id) REFERENCES classes(id)
    )''')

    conn.commit()
    conn.close()

@pytest.fixture  # <-- Decorate this so pytest registers it as a fixture
def setup_data():
    setup_database()

    teacher = Teacher("Jane", "Doe", "janedoe@example.com")
    teacher.save()

    student = Student("Bob", "Brown", "bob@example.com")
    student.save()

    cls = SchoolClass("Science", teacher_id=teacher.id)
    cls.save()

    return teacher, student, cls

def test_teacher_creation(setup_data):
    teacher, _, _ = setup_data
    assert teacher.first_name == "Jane"
    assert teacher.last_name == "Doe"
    assert "@" in teacher.email

def test_student_enrollment(setup_data):
    _, student, cls = setup_data
    Enrollment.enroll(student, cls)
    student_classes = student.get_classes()
    assert any(c.name == "Science" for c in student_classes)

def test_class_students(setup_data):
    _, student, cls = setup_data
    Enrollment.enroll(student, cls)
    students = cls.get_students()
    assert any(s.email == "bob@example.com" for s in students)
