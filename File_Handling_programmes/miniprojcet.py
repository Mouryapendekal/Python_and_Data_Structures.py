# Write student names into a file
# Read student names from the file
# Append a new student
# Handle a missing file
with open("students.txt","w",encoding="utf-8") as f:
    f.write("Manideep\n")
    f.write("Laya\n")
    f.write("shiva\n")
    f.write("Malli\n")
print("Data entered successfully !")
with open("students.txt","r",encoding="utf-8") as f:
    print("\nstudents names:")
    for line in f:
        print(line.strip())
with open("students.txt","a",encoding="utf-8") as f:
    f.write("Mourya\n")
print("new student added !")
try:
    with open("missingfile.txt","r")as f:
        print(f.read())
except FileNotFoundError:
    print("The requested file was not found.")