def hallow_square(n):
    for i in range(1,n+1,1):
        for j in range(1,n+1,1):
            if(i==1 or j==1 or i==n or j==n):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
n=5
print(hallow_square(n))