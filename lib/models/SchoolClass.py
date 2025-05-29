import sqlite3
from lib.helpers import DBHelper
from .student import Student


DB_NAME = "school.db"

class SchoolClass:
    def __init__(self, name, teacher_id, id=None):
        self.id = id
        self.name = name
        self.teacher_id = teacher_id  

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("HAS TO BE A STRING !.")
        if not value.strip():
            raise ValueError("CAN;T BE EMPTY.")
        if len(value.strip()) < 2:
            raise ValueError("LAZMA IKUE IMEPITA 2 BRO")
        self._name = value.strip().capitalize()

    @property
    def teacher_id(self):
        return self._teacher_id

    @teacher_id.setter
    def teacher_id(self, value):
        if not (isinstance(value, int) or value is None):
            raise TypeError("LAZMA IKUE AN INTERGER.")
        self._teacher_id = value

    def save(self):
     conn = sqlite3.connect(DB_NAME)
     cursor = conn.cursor()
     cursor.execute('''
        INSERT INTO classes (name, teacher_id) VALUES (?, ?)
    ''', (self.name, self.teacher_id))
     self.id = cursor.lastrowid  
     print(f"[Class.save] New class saved with id {self.id}")
     conn.commit()
     conn.close()


    def get_students(self):
     from lib.models.student import Student  

     conn = sqlite3.connect(DB_NAME)
     cursor = conn.cursor()
     cursor.execute('''
        SELECT students.id, students.first_name, students.last_name, students.email
        FROM students
        JOIN enrollments ON students.id = enrollments.student_id
        WHERE enrollments.class_id = ?
    ''', (self.id,))
     rows = cursor.fetchall()
     conn.close()

     return [Student(first_name=row[1], last_name=row[2], email=row[3], id=row[0]) for row in rows]
