import sqlite3
from
DB_NAME = "school.db"


if __name__ == "__main__":
    teacher = Teacher("Jane", "Doe", "janedoe@example.com")
    teacher.save()
    print("Created Teacher:", teacher)

    student = Student("Bob", "Brown", "bob@example.com")
    student.save()
    print("Created Student:", student)

    cls = Class("Science", teacher_id=teacher.id)
    cls.save()
    print("Created Class:", cls)

    enrollment = Enrollment.enroll(student, cls)
    print("Enrolled Student:", enrollment)

    print("Student's Classes:", student.get_classes())
    print("Class's Students:", cls.get_students())
