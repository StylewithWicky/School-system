import sqlite3
from lib.models.Teacher import Teacher
from lib.models.student import Student
from lib.models.Class import Class
from lib.models.enrolment import Enrollment
DB_NAME = "school.db"

if __name__ == "__main__":
    t1 = Teacher("John", "Doe", "johndoe@example.com")
    t1.save()
    
    s1 = Student("Alice", "Smith", "alice@example.com")
    s1.save()

    c1 = Class("Math", teacher_id=1)
    c1.save()

    Enrollment.enroll(s1, c1)
