with open("students.txt", "r", encoding="utf-8") as f:
    students = f.readlines()
students = [name.strip() for name in students]
print(students)