from mcp.server.fastmcp import FastMCP
from crud import (get_all_problems,
                  get_stats,
                  get_unsolved_problems,
                  get_problems_by_topic,
                  add_problem,
                  delete_problem,
                  mark_solved)
import os

print("Current Working Directory:", os.getcwd())

mcp = FastMCP("Leetcode Tracker")
@mcp.tool()
def list_problems():
    """To get all the problem"""
    try:
        return get_all_problems()
    except Exception as e:
        print("ERROR:",e)
        raise

@mcp.tool()
def list_unsolved_problems():
    """TO get all the unsolved problem"""
    return get_unsolved_problems()

@mcp.tool()
def get_topic_problems(topic: str):
    """To get the problem based on topic"""
    return get_problems_by_topic(topic)

@mcp.tool()
def insert_problem(
    title: str,
    difficulty: str,
    topic: str,
):
    try:
        add_problem(title, difficulty, topic)
        return f"Added {title} successfully"
    except Exception as e:
        print("ERROR:", e)
        raise

@mcp.tool()
def solve_problem(problem_id: int):
    """To mark the solved problem in Leetcode Tracker"""
    mark_solved(problem_id)
    return f"Problem {problem_id} marked as solved"

@mcp.tool()
def tracker_stats():
    """To get the solved problem from Leetcode Tracker"""
    return get_stats()

@mcp.tool()
def remove_problem(problem_id: int):
    """To remove a problem from Leetcode Tracker"""
    delete_problem(problem_id)
    return f"Problem {problem_id} has been deleted"

print("server starting...")

if __name__=="__main__":
    mcp.run()