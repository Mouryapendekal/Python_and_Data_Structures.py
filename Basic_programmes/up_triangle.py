def up_triangle(n):
    for i in range(1,n+1,1):
        for j in range(i,n+1):
            print("*",end=" ")
        print()
n=5
print(up_triangle(n))