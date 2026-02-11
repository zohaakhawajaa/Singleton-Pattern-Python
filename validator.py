import sqlite3

class ValidationService:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.conn = sqlite3.connect("systems.db")
        return cls._instance

    def is_valid(self, hostname, ip):
        cursor = self.conn.cursor()
        cursor.execute(
            "SELECT COUNT(*) FROM systems WHERE hostname=? AND ip=?",
            (hostname, ip)
        )
        return cursor.fetchone()[0] > 0
