import sqlite3
from .SchoolClass import SchoolClass
from lib.helpers import DBHelper
DB_NAME = "school.db"

class Teacher:
    def __init__(self, first_name, last_name, email, id=None):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise TypeError("LAZMA IKUE A STRING.")
        if not value.strip():
            raise ValueError("HAIFAI KUKUA EMPTY.")
        if len(value.strip()) < 2:
            raise ValueError(" 2 characters long OR MORE.")
        self._first_name = value.strip().capitalize()

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        if not isinstance(value, str):
            raise TypeError("LAZMA IKUE A STRING.")
        if not value.strip():
            raise ValueError("HAIFAI KUKUA EMPTY.")
        if len(value.strip()) < 2:
            raise ValueError("2 characters long OR MORE.")
        self._last_name = value.strip().capitalize()

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if not isinstance(value, str):
            raise TypeError("LAZMA IKUE A STRING.")
        if not value.strip():
            raise ValueError("HAIFAI KUKUA EMPTY.")
        if len(value.strip()) < 5:
            raise ValueError("2 characters long OR MORE.") 
        self._email = value.strip()

    def save(self):
        if self.id is None:
            DBHelper.execute(
                'INSERT INTO teachers (first_name, last_name, email) VALUES (?, ?, ?)',
                (self.first_name, self.last_name, self.email)
            )
            last_id = DBHelper.execute('SELECT last_insert_rowid()', fetch=True)[0][0]
            self.id = last_id
        else:
            DBHelper.execute(
                'UPDATE teachers SET first_name=?, last_name=?, email=? WHERE id=?',
                (self.first_name, self.last_name, self.email, self.id)
            )

    def get_classes(self):
     from lib.models.SchoolClass import SchoolClass 
     
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
