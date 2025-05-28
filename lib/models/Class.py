import sqlite3

DB_NAME = "school.db"

class Class:
    def __init__(self, name, teacher_id, id=None):
        self.id = id
        self.name = name
        self.teacher_id = teacher_id  # FK reference to Teacher.id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Class name must be a string.")
        if not value.strip():
            raise ValueError("Class name cannot be empty.")
        if len(value.strip()) < 2:
            raise ValueError("Class name must be at least 2 characters long.")
        self._name = value.strip().capitalize()

    @property
    def teacher_id(self):
        return self._teacher_id

    @teacher_id.setter
    def teacher_id(self, value):
        if not (isinstance(value, int) or value is None):
            raise TypeError("Teacher ID must be an integer or None.")
        self._teacher_id = value

    def save(self):
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        if self.id is None:
            cursor.execute(
                'INSERT INTO classes (name, teacher_id) VALUES (?, ?)',
                (self.name, self.teacher_id)
            )
            self.id = cursor.lastrowid
        else:
            cursor.execute(
                'UPDATE classes SET name=?, teacher_id=? WHERE id=?',
                (self.name, self.teacher_id, self.id)
            )
        conn.commit()
        conn.close()

    @classmethod
    def find_by_id(cls, id):
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM classes WHERE id = ?", (id,))
        row = cursor.fetchone()
        conn.close()
        if row:
            # row is (id, name, teacher_id)
            return cls(row[1], row[2], id=row[0])
        return None

    def __repr__(self):
        return f"<Class {self.id}: {self.name}, Teacher ID: {self.teacher_id}>"
    def get_classes(self):
        if self.id is None:
            return []
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute('''
            SELECT c.id, c.name, c.teacher_id
            FROM classes c
            JOIN class_students cs ON c.id = cs.class_id
            WHERE cs.student_id = ?
        ''', (self.id,))
        rows = cursor.fetchall()
        conn.close()
        return [Class(row[1], row[2], id=row[0]) for row in rows]

        