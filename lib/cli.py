import sqlite3
from lib.models.Teacher import Teacher
from lib.models.student import Student
from lib.models.Class import Class
from lib.models.enrolment import Enrollment
DB_NAME = "school.db"
def main():
    print("Welcome to the School Enrollment CLI")
    while True:
        print("\nOptions: 1) Add Teacher 2) Add Student 3) Add Class 4) Enroll Student 5) Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            fname = input("First name: ")
            lname = input("Last name: ")
            email = input("Email: ")
            teacher = Teacher(fname, lname, email)
            teacher.save()
            print("Teacher added.")
        elif choice == "2":
            fname = input("First name: ")
            lname = input("Last name: ")
            email = input("Email: ")
            student = Student(fname, lname, email)
            student.save()
            print("Student added.")
        elif choice == "3":
            name = input("Class name: ")
            teacher_id = int(input("Teacher ID: "))
            class_ = Class(name, teacher_id)
            class_.save()
            print("Class added.")
        elif choice == "4":
            student_id = int(input("Student ID: "))
            class_id = int(input("Class ID: "))
            enrollment = Enrollment(student_id, class_id)
            enrollment.save()
            print("Enrollment successful.")
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()