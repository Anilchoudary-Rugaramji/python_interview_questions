# Mini Project: Student Grade Tracker

# Features:
# - Add student name + grade
# - List all students with grades
# - Find student with highest grade
# - Average grade

students = {}

action = input("Select add/list/highest/avg/exit:")

while True:
    if action == "add":
        name = input("Enter the name of the student")
        grade = input("Enter the grade of the student")
        students[name] = grade
    elif action == "list":
        for name, grade in students.items():
            print(f"{name}:{grade}")
    elif action == "highest":
        name = max(students, key=students.get)
        print(f"Top student: {name} with grade {students[name]}")
    elif action == "avg":
        avg = sum(students.values()) / len(students)
        print(f"Average grade: {avg:.2f}")
    elif action == "exit":
        break
