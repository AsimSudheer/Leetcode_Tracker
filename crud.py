import sqlite3

import os

DB_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "leetcode.db"
)

print("DATABASE PATH:", DB_PATH)

def add_note(problem_id,notes):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""UPDATE problems 
                   SET notes = ?
                   WHERE id=?""",(notes,problem_id))
    conn.commit()
    conn.close()

def increment_attempt(problem_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""UPDATE problems 
                   SET attempts = attempts +1 
                   WHERE id =?""",(problem_id,))
    conn.commit()
    conn.close()

def smart_recommendation():
    conn = get_connection()
    cursor=conn.cursor()
    cursor.execute("""SELECT topic,COALESCE(SUM(solved),0) AS solved_count
                   FROM problems
                   GROUP BY topic
                   ORDER BY solved_count ASC
                   LIMIT 1""")
    weakest_topic = cursor.fetchone()
    if not weakest_topic:
        conn.close()
        return None
    topic = weakest_topic[0]
    cursor.execute("""SELECT id,title,difficulty,topic 
                   FROM problems
                   WHERE topic = ?
                   AND solved=0
                   LIMIT 1""",(topic,))
    problem = cursor.fetchone()
    conn.close()
    return problem

def anazlyze_progress():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""SELECT topic,
                   COUNT(*) as total,
                   SUM(solved) as solved
                   FROM problems
                   GROUP BY TOPICS""")
    data = cursor.fetchall()
    conn.close()
    return data

def get_connection():
    print("Connecting to:", DB_PATH)
    return sqlite3.connect(DB_PATH)

def recommend_next_problem():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""SELECT id,title,difficulty,topic FROM problems
                   WHERE SOLVED = 0
                   ORDER BY id
                   LIMIT 1""")
    problem = cursor.fetchone()
    conn.close()
    return problem

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