import sqlite3
from lib.helpers import DBHelper
DB_NAME = "school.db"
class Enrollment:
    def __init__(self, student_id, class_id, id=None):
        self.id = id
        self.student_id = student_id
        self.class_id = class_id

    def save(self):
        if self.id is None:
            DBHelper.execute(
                'INSERT INTO enrollments (student_id, class_id) VALUES (?, ?)',
                (self.student_id, self.class_id)
            )
            last_id = DBHelper.execute('SELECT last_insert_rowid()', fetch=True)[0][0]
            self.id = last_id
            print(f"[Enrollment.save] New enrollment saved with id {self.id}")
        else:
            DBHelper.execute(
                'UPDATE enrollments SET student_id=?, class_id=? WHERE id=?',
                (self.student_id, self.class_id, self.id)
            )
            print(f"[Enrollment.save] Enrollment updated with id {self.id}")

    @staticmethod
    def enroll(student, class_):
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        print(f"Enroll called with student.id={student.id}, class_.id={class_.id}")
        cursor.execute('''
            INSERT INTO enrollments (student_id, class_id) VALUES (?, ?)
        ''', (student.id, class_.id))
        conn.commit()
        conn.close()
