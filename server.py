from mcp.server.fastmcp import FastMCP
from crud import (increment_attempt,
                  add_note,
                  smart_recommendation,
                  recommend_next_problem,
                  anazlyze_progress,
                  get_all_problems,
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
def add_problem_notes(problem_id:int,notes:str):
    """add notes of the problem"""
    add_note(problem_id,notes)
    return f"notes added to the problem {problem_id}"

@mcp.tool()
def record_attempt(problem_id:int):
    increment_attempt(problem_id)
    return f"attempted record of the problem {problem_id}"

@mcp.tool()
def recommend_best_problem():
    """recommend the next problem that needed to be solved from weakest topic"""
    problem = smart_recommendation()
    if not problem:
        return " There is on recommendation"
    return{
        "id":problem[0],
        "title":problem[1],
        "difficulty":problem[2],
        "topic":problem[3]
    }

@mcp.tool()
def generate_study_plan(days:int):
    """To generate a study plan for the given days"""
    problems = get_unsolved_problems()
    plan =[]
    if not problems:
        return "There is no unsolved problems"
    for day,problem in enumerate(problems[:days],start=1):
        plan.append({
            "Day":day,
            "Title":problem[0],
            "Difficulty":problem[1],
            "Topic":problem[2]
        })
    return plan

@mcp.tool()
def progress_analysis():
    """Analyze topic wise progress"""
    data = anazlyze_progress()
    result = []
    for topic,total,solved in data:
        solved =0 or solved #to prevent clash during division
        result.append({
            "topic":topic,
            "Total":total,
            "Solved":solved,
            "Completion-Percentage": round((total/solved)*100,2)
        })
        return result


@mcp.tool()
def recommend_problem():
    """To get the next unsolved problem"""
    problem = recommend_next_problem()
    if not problem:
        return "There is no unsolved problem"

    return {
        "id":problem[0],
        "Title":problem[1],
        "Difficulty":problem[2],
        "topic":problem[3]
    }

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