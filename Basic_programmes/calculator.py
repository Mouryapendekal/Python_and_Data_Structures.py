x=int(input("A :"))
y=int(input("B :"))
operator=input("enter the operator:")
if(operator=="+"):
    print("sum",x+y)
elif(operator =="-"):
    print("sub",x-y)
elif(operator =="/"):
    if(y!=0):
        print("divison",x/y)
    else:("invalid operator")
else:("invaled operator")
      

