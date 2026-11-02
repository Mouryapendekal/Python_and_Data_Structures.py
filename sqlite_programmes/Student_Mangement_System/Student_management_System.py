import sqlite3
def create_table():
    with sqlite3.connect("students.db")as con:
        cur=con.cursor()
        cur.execute("""
        CREATE TABLE IF NOT EXISTS students(
        st_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        marks INTEGER NOT NULL,
        course TEXT NOT NULL
        )
        """)
        print("table created successfully!")
def insert_students():
    n=int(input("how many student records do you want to insert(1-5)?"))
    if n<1 or n>5:
        print("please enter a number between 1-5")
        return
    with sqlite3.connect("students.db") as con:
        cur=con.cursor()
        for i in range(n):
            print(f"\n enter details for student{i+1}")
            st_id=int(input("enter student_id:"))
            name=input("enter the student name:")
            marks=int(input("enter the marks of student:"))
            course=input("enter the course name:")
            cur.execute("INSERT INTO students(st_id,name,marks,course) values(?,?,?,?)",(st_id,name,marks,course))
            print(f"\n {n} student record inserted succesfully!")
def view_records():
    with sqlite3.connect("students.db") as con:
        cur=con.cursor()
        cur.execute("SELECT * FROM students")
        rows=cur.fetchall()
        for r in rows:
            print(f"st_id{r[0]}|name:{r[1]}|marks:{r[2]}|course:{r[3]}")
        print()
def update_student():
    student_id=int(input("enter the student_id to update:"))
    new_marks=int(input("enter the marks of students to update:"))
    with sqlite3.connect("students.db") as con:
        cur=con.cursor()
        cur.execute("""
        UPDATE students
        set marks=?
        where st_id=?
        """,(new_marks,student_id))
        if cur.rowcount>0:
            print("record updated successfully!")
        else:
            print("record not found.\n")
def delete_student():
    student_id=int(input("enter the student_id to delete the record:"))
    with sqlite3.connect("students.db") as con:
        cur=con.cursor()
        cur.execute("DELETE FROM students WHERE st_id=?",(student_id,))
        print("record deleted successfully!.\n")
def display_distinction_students():
    with sqlite3.connect("students.db") as con:
        cur=con.cursor()
        cur.execute("SELECT * FROM students WHERE marks>?",(80,))
        students=cur.fetchall()
        if students:
            for st in students:
                print(st)
        else:
            print("no student scored above 80 marks.\n")
def display_course():
    with sqlite3.connect("students.db") as con:
        cur=con.cursor()
        cur.execute("SELECT * FROM students WHERE course=?",("python",))
        students=cur.fetchall()
        if students:
            for st in students:
                print(st)
        else:
            print("no students enrolled for course python")
def count_avg():
    with sqlite3.connect("students.db") as con:
        cur=con.cursor()
        cur.execute("""
        SELECT COUNT(*),AVG(marks)
        FROM students
        """)
        res=cur.fetchone()
        print("total no of students:",res[0])
        print("avg marks of students:",res[1])
def desc_ord():
    with sqlite3.connect("students.db") as con:
        cur=con.cursor()
        cur.execute("""
        SELECT * FROM students
        ORDER BY marks DESC
        """)
        st=cur.fetchall()
        for s in st:
            print(s)
def menu():
    create_table()
    while True:
        print("""
        STUDENT MANAGEMENT SYSTEM
        1.insert_records
        2.view_records
        3.update_student_marks
        4.delete_student_record
        5.view who scored above 80 marks
        6.view who enrolled for the course python
        7.view total no of students and avg marks of all students
        8.view the records are in desc order considering marks
        9.exit
        """)
        choice=input("enter choice:")
        if choice=="1":
            print(insert_students())
        elif choice=="2":
            print(view_records())
        elif choice=="3":
            print(update_student())
        elif choice=="4":
            print(delete_student())
        elif choice=="5":
            print(display_distinction_students())
        elif choice=="6":
            print(display_course())
        elif choice=="7":
            print(count_avg())
        elif choice=="8":
            print(desc_ord())
        elif choice=="9":
            print("Exiting.......")
            break
        else:
            print("invalid choice! try agian .\n")
if __name__ == "__main__":
    menu()


