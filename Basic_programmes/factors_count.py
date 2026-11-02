def factors_count(n):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c=c+1
    print(c)
while True:
    k=input("enter:")
    if k=="stop" or k=="":
        break
    z=int(k)
    print(factors_count(z))