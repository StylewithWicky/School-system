import sqlite3

DB_NAME = "school.db"
class Enrollment:
    def __init__(self, student_id, class_id, id=None):
        self.id = id
        self.student_id = student_id
        self.class_id = class_id

    def save(self):
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        if self.id is None:
            cursor.execute('INSERT INTO enrollments (student_id, class_id) VALUES (?, ?)', (self.student_id, self.class_id))
            self.id = cursor.lastrowid
        else:
            cursor.execute('UPDATE enrollments SET student_id=?, class_id=? WHERE id=?', (self.student_id, self.class_id, self.id))
        conn.commit()
        conn.close()

    @classmethod
    def enroll(cls, student, class_):
        enrollment = cls(student.id, class_.id)
        enrollment.save()
        return enrollment

    @classmethod
    def find_all(cls):
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute('SELECT id, student_id, class_id FROM enrollments')
        rows = cursor.fetchall()
        conn.close()
        return [cls(row[1], row[2], id=row[0]) for row in rows]
