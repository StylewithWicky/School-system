import sqlite3
from Class import Class
DB_NAME = "school.db"

class Student:
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
        if self.id is None:
            cursor.execute(
                'INSERT INTO students (first_name, last_name, email) VALUES (?, ?, ?)',
                (self.first_name, self.last_name, self.email)
            )
            self.id = cursor.lastrowid
        else:
            cursor.execute(
                'UPDATE students SET first_name=?, last_name=?, email=? WHERE id=?',
                (self.first_name, self.last_name, self.email, self.id)
            )
        conn.commit()
        conn.close()

    def get_classes(self):
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute('''
            SELECT c.id, c.name, c.teacher_id
            FROM classes c
            JOIN enrollments e ON c.id = e.class_id
            WHERE e.student_id = ?
        ''', (self.id,))
        rows = cursor.fetchall()
        conn.close()
        return [Class(row[1], row[2], id=row[0]) for row in rows]
