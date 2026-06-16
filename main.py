from crud import *

def display_problems(problems):
    for p in problems:
         print(
            f"ID:{p[0]} | "
            f"Problem:{p[1]} | "
            f"Difficulty:{p[2]} | "
            f"Topic:{p[3]} | "
            f"Solved:{p[4]}"
        )

while True:
    print("\n===== LEETCODE TRACKER =====")
    print("1. View Problems")
    print("2. View Unsolved Problems")
    print("3. View Stats")
    print("4. Exit")

    choice = input("Enter your choice:")

    if choice == "1":
        display_problems(get_all_problems())
    elif choice == "2":
        display_problems(get_unsolved_problems())
    elif choice == "3":
        solved,total = get_stats()
        print(f"SOLVED:{solved} | TOTAL:{total}")
    elif choice == "4":
        break
    else:
        print("invalid choice")