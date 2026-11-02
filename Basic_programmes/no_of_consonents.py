n=11
if n<0:
    print("invalid input")
else:
    s=[]
    for i in range(n):
        k=input()
        if k.isalpha():
            s.append(k)
        else:
            print("invalid array elements")
            break
    c=0
    for j in s:
        if j not in "aeiou":
            c+=1
    print("Count:",c)
            
