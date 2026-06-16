from crud import add_problem
from crud import get_all_problems
from crud import get_unsolved_problems
from crud import get_problems_by_topic
from crud import mark_solved
from crud import delete_problem
from crud import get_stats


solved,total = get_stats()
print(f"SOLVED:{solved} | TOTAL:{total}")
print()
print("ALL PROBLEM")
print()

for row in get_all_problems():
    id,title,difficulty,topic,solved = row
    print(f"ID:{id} | PROBLEM:{title} | DIFFICULTY:{difficulty} | TOPIC:{topic} | SOLVED:{solved}")

print()
print("UNSOLVED PROBLEM")
print()
for row in get_unsolved_problems():
    id,title,difficulty,topic,solved = row
    print(f"ID:{id} | PROBLEM:{title} | DIFFICULTY:{difficulty} | TOPIC:{topic} | SOLVED:{solved}")
print()
print("PROBLEMS OF ARRAY")
print()
for row in get_problems_by_topic("Array"):
    id,title,difficulty,topic,solved = row
    print(f"ID:{id} | PROBLEM:{title} | DIFFICULTY:{difficulty} | TOPIC:{topic} | SOLVED:{solved}")

mark_solved(3)
delete_problem(2)