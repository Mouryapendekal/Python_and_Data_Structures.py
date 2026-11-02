def right_triangle(n):
    for i in range(n):
        for j in range(n):
            print("*",end=" ")
        print(" ")
n=5
print(right_triangle(n))