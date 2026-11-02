students = ["Mourya", "Manideep", "malli","laya","shiva"]
with open("students.txt", "w", encoding="utf-8") as f:
    for name in students:
        f.write(name + "\n")
print("Students saved!")