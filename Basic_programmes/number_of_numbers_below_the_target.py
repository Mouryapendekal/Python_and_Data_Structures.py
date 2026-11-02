n=int(input("Enter the number:"))
if n<0:
    print("invalid error")
else:
    s=[]
    for i in range(n):
        m=input("enter the numbers:")
        try:
            y=int(m)
            s.append(y)
        except Exception as e:
            print("invalid elemenets")
            break
    else:
        target=int(input("enter the target:"))
        c=0
        for j in s:
            if j<target:
                c+=1
            else:
                print("no such elements")
        print("the number of numbers below the ",target," is:",c)
