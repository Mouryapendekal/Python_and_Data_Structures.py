def upleft_triangle(n):
    for i in range(1,n+1,1):
        for j in range(i,n+1):
            print(" ",end=" ")
        for j in range(1,i,1):
            print("*",end=" ")
        print()
n=5
print(upleft_triangle(n))