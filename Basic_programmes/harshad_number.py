n=int(input("Enter the element:"))
sum=0
while(n!=0):
    sum+=n%10
    n//=10
if(n%sum==0):
    print("IT IS HARSAHD NUMBER")
else:
    print("not")