def factorial_num(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    return fact
n=5
print(factorial_num(n))
print(factorial_num(7))
print(factorial_num(8))
print(factorial_num(9))
print(factorial_num(10))