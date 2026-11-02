num=int(input("Enter the num:"))
count=0
n=1
while(n<=num):
    if(num%n==0):
        count+=1
    n+=1
if(count==2):
    print("prime")
else:
    print("not prime")
