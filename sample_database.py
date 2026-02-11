import sqlite3

conn = sqlite3.connect("systems.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS systems (
    hostname TEXT,
    ip TEXT
)
""")

cur.execute("INSERT INTO systems VALUES ('DESKTOP-123', '192.168.1.10')")
conn.commit()
conn.close()
