def add_str(str1):
    length=len(str1)
    if length<3:
        return str1
    elif str1[-3:]=="ing":
        return str1+"ly"
    else:
        return str1+"ing"
print(add_str("criing"))