import sqlite3
def get_connection():
    return sqlite3.connect("leetcode.db")
def add_problem(title,difficulty,topic,solved=0):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""INSERT INTO problems(title,difficulty,topic,solved)
                   VALUES(?,?,?,?)""",(title,difficulty,topic,solved))
    conn.commit()
    conn.close()


def get_all_problems():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM problems""")

    rows = cursor.fetchall()

    conn.close()
    return rows


def get_unsolved_problems():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
                   SELECT * FROM problems
                   WHERE solved=0
                   """)
    rows = cursor.fetchall()
    conn.close()
    return rows


def get_problems_by_topic(topic):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""SELECT * FROM problems
                   WHERE topic = ?""",(topic,))
    
    rows = cursor.fetchall()
    conn.close()
    return rows


def mark_solved(problem_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
                   UPDATE problems
                   SET solved = 1
                   WHERE id = ?""",
                   (problem_id,)
                   )
    conn.commit()
    conn.close()

def delete_problem(problem_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""DELETE FROM problems
                   WHERE id = ?""",
                   (problem_id,))
    conn.commit()
    conn.close()    


def get_stats():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""SELECT COUNT(*)
                   FROM problems
                   WHERE solved = 1""")
    solved = cursor.fetchone()[0]

    cursor.execute("""SELECT COUNT(*) FROM problems
                   """)
    total = cursor.fetchone()[0]
    conn.close()
    return solved,total