n=int(input("Enter the no :"))
a=0
b=1
print(a,b, end=' ')
for i in range(2,n+1):
    c=a+b
    a=b
    b=c
    print(c, end=' ')
