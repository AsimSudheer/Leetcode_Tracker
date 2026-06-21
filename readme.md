# AI-Powered LeetCode Coach

## About the Project

I built this project to make my LeetCode preparation more organized and interactive. While practicing coding problems, I realized that simply solving questions wasn't enough—I wanted a way to track my progress, identify weak areas, keep revision notes, and get recommendations on what to solve next.

To make it more interesting, I integrated it with Claude Desktop using MCP (Model Context Protocol), allowing me to manage and analyze my LeetCode practice through natural language conversations.

What started as a simple LeetCode tracker gradually evolved into an AI-powered learning assistant.

---

## Features

### Problem Tracking

* Add new problems
* View all problems
* View unsolved problems
* Filter problems by topic
* Mark problems as solved
* Delete problems

### Progress Analysis

* View overall statistics
* Track solved and unsolved problems
* Analyze topic-wise progress

### Smart Recommendations

* Recommend problems from weaker topics
* Help prioritize what to practice next

### Study Planning

* Generate study plans using unsolved problems
* Create structured practice schedules

### Learning Memory

* Add notes to problems
* Track the number of attempts made
* Store important observations for future revision

### Learning Pattern Analysis

* Identify strong topics
* Identify weak topics
* Highlight problems that required multiple attempts

---

## Tech Stack

* Python
* SQLite
* MCP (Model Context Protocol)
* Claude Desktop
* Git & GitHub

---

## How It Works

```text
Claude Desktop
      ↓
Custom MCP Server
      ↓
CRUD Layer (Python)
      ↓
SQLite Database
```

Claude can call tools exposed by the MCP server, which interact with the SQLite database and return relevant information.

---

## MCP Tools

The project currently supports:

* list_problems()
* list_unsolved_problems()
* get_topic_problems()
* insert_problem()
* solve_problem()
* remove_problem()
* tracker_stats()
* recommend_best_problem()
* progress_analysis()
* analyze_learning_pattern()
* generate_study_plan()
* add_problem_notes()
* record_attempt()

---

## What I Learned

This project helped me learn:

* SQLite database design
* CRUD operations
* MCP server development
* Tool calling with Claude Desktop
* Python project organization
* Debugging and troubleshooting
* Building AI-assisted workflows

---

## Future Improvements

Some ideas I may explore in the future:

* Adaptive recommendation engine
* Mock interview agent
* Personalized learning roadmaps
* LeetCode API integration
* More advanced analytics

---

## Author

Asim Sudheer

B.Tech Computer Science Engineering
