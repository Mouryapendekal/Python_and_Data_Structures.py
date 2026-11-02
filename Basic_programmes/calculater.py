x=int(input("enter the number: "))
y=int(input("enter the number2: "))
operator=input(" Choose an operator(+,-,*,/): ")
if (operator== '+'):
    print("sum= ",x+y)
elif (operator== '-'):
    print("diff= ",x-y)
elif (operator=='*'):
    print("product= ",x*y)
elif(operator=='/'):
    if(y!=0):
        print("quo= ",x/y)
    else:
        print("invalid input")
else:
    print("invalid operator")