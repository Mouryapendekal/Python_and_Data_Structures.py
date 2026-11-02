
def right_triangle(n):
    for i in range(1,n+1,1):
        for j in range(i):
            print(" ",end="")
        for j in range(n+1,i,-1):
            print("*",end="")
        print()
n=5
print(right_triangle(n)) 