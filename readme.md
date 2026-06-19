# AI-Powered LeetCode Tracker

## Overview

AI-Powered LeetCode Tracker is a Python-based application that combines SQLite, MCP (Model Context Protocol), and Claude Desktop to provide an intelligent LeetCode tracking experience.

The project allows users to manage coding problems, analyze progress, generate study plans, and receive personalized problem recommendations through natural language interactions.

---

## Tech Stack

* Python
* SQLite
* MCP (Model Context Protocol)
* Claude Desktop
* Git & GitHub

---

## Architecture

Claude Desktop
→ MCP Server (server.py)
→ CRUD Layer (crud.py)
→ SQLite Database (leetcode.db)

---

## Features

### Problem Management

* Add Problems
* View Problems
* View Unsolved Problems
* Filter by Topic
* Mark Problems as Solved
* Delete Problems

### Analytics

* Tracker Statistics
* Progress Analysis
* Topic-wise Performance Tracking

### AI Features

* Problem Recommendation Engine
* Study Plan Generator
* Natural Language Tool Calling through Claude Desktop

---

## MCP Tools

* list_problems()
* list_unsolved_problems()
* get_topic_problems()
* insert_problem()
* solve_problem()
* remove_problem()
* tracker_stats()
* recommend_best_problem()
* progress_analysis()
* generate_study_plan()

---

## Future Improvements

* LeetCode API Integration
* Streamlit Dashboard
* Interview Practice Mode
* Advanced Recommendation Engine

---

## Author

Asim Sudheer
B.Tech Computer Science Engineering
