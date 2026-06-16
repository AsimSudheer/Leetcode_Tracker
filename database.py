import sqlite3

conn = sqlite3.connect("leetcode.db")

cursor = conn.cursor()

cursor.execute(""" CREATE TABLE IF NOT EXISTS problems(id INTEGER PRIMARY KEY AUTOINCREMENT,
               title TEXT,
               difficulty TEXT,
               topic TEXT,
               solved INTEGER)""")

conn.commit()
conn.close()

print("databases created succesfully")