import sqlite3
DB_NAME = "school.db"


class DBHelper:
    @staticmethod
    def execute(query, params=(), fetch=False):
        conn = sqlite3.connect("school.db")
        cursor = conn.cursor()
        cursor.execute(query, params)
        if fetch:
            results = cursor.fetchall()
            conn.close()
            return results
        conn.commit()
        conn.close()
