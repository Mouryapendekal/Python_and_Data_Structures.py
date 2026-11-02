#create a dict to store 5 students and their marks.display students who scored more than 75
D_size=int(input("enter the size:"))
dt={}
for i in range(D_size):
    name=input("enter the name of the student:")
    marks=int(input("enter the marks:"))
    dt[name]=marks
for name,marks in dt.items():
    if marks>75:
        print(name,":",marks)