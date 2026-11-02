student = {
    "name": "Mourya",
    "marks": 85
}
with open("student.txt", "w", encoding="utf-8") as f:
    f.write(student["name"] + "\n")
    f.write(str(student["marks"]) + "\n")