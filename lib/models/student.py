import sqlite3
from lib.helpers import DBHelper



DB_NAME = "school.db"

class Student:
    def __init__(self, first_name, last_name, email, id=None):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def enroll(self, class_id):
        from lib.models.SchoolClass import SchoolClass  # Local import to avoid circular import
        from lib.models.enrolment import Enrollment  # Import Enrollment class

        cls = SchoolClass.find_by_id(class_id)
        if cls is None:
            raise ValueError(f"Class with id {class_id} does not exist")

        Enrollment.enroll(self, cls)

    def get_classes(self):
     from lib.models.SchoolClass import SchoolClass  # <- moved here to avoid circular import

     conn = sqlite3.connect(DB_NAME)
     cursor = conn.cursor()
     cursor.execute('''
        SELECT classes.id, classes.name, classes.teacher_id
        FROM classes
        JOIN enrollments ON classes.id = enrollments.class_id
        WHERE enrollments.student_id = ?
    ''', (self.id,))
     rows = cursor.fetchall()
     conn.close()

     return [SchoolClass(name=row[1], teacher_id=row[2], id=row[0]) for row in rows]

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise TypeError("First name must be a string.")
        if not value.strip():
            raise ValueError("First name cannot be empty.")
        if len(value.strip()) < 2:
            raise ValueError("First name must be at least 2 characters long.")
        self._first_name = value.strip().capitalize()

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        if not isinstance(value, str):
            raise TypeError("Last name must be a string.")
        if not value.strip():
            raise ValueError("Last name cannot be empty.")
        if len(value.strip()) < 2:
            raise ValueError("Last name must be at least 2 characters long.")
        self._last_name = value.strip().capitalize()

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if not isinstance(value, str):
            raise TypeError("Email must be a string.")
        if not value.strip():
            raise ValueError("Email cannot be empty.")
        if len(value.strip()) < 5 or '@' not in value:
            raise ValueError("Invalid email address.")
        self._email = value.strip()

    def save(self):
     conn = sqlite3.connect(DB_NAME)
     cursor = conn.cursor()
     cursor.execute('''
        INSERT INTO students (first_name, last_name, email) VALUES (?, ?, ?)
    ''', (self.first_name, self.last_name, self.email))
     self.id = cursor.lastrowid  # ✅ Important line
     conn.commit()
     conn.close()
