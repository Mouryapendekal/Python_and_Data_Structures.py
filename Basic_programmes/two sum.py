n=int(input("Enter the numbers:"))
s=[]
for i in range(n):
    m=int(input("enter the elements:"))
    s.append(m)
target=int(input("Enter the target:"))
d=len(s)
for i in range(d):
    for j in range(i+1,d):
        if s[i]+s[j]==target:
            print([i,j])