k=5000
for n in range(k+1):
    sum=0
    p=len(str(n))
    temp=n
    while n!=0:
        d=n%10
        sum+=d**p
        n//=10
    if temp==sum:
        print(sum)