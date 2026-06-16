import sqlite3

conn = sqlite3.connect("leetcode.db")
cursor = conn.cursor()

cursor.execute("""
               SELECT * FROM problems
                WHERE solved=0
               """)

rows = cursor.fetchall()

for row in rows:
    id,title,difficulty,topic,solved = row
    print(f"ID:{id} | PROBLEM:{title} | DIFFICULTY:{difficulty} | TOPIC:{topic} | SOLVED:{solved}")

conn.close()