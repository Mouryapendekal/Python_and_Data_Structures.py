k=100
for n in range(1,k+1):
    sum=0
    for i in range(1,n):
        if n%i==0:
            sum+=i
    if sum==n:       
        print(sum)
