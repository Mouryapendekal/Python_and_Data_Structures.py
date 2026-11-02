n=19
s=n
while(n>10):
    sum=0
    while n!=0:
        d=n%10
        sum+=d*d
        n//=10
    n=sum
if n==1:
    print(s,"is happy number")
else:
    print(s,"not a happy number")