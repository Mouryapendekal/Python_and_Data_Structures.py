'''
def str_check(s):
    d=w=0
    for s1 in s:
        s2=s1.split(":")
        if s2[0]=="D":
            dep= int(s2[1])
            d = d + dep
        else:
            wit = int(s2[1])
            w = w + wit           
    return(d-w)
s=["D:300","D:300","W:200","D:100"] 
print(str_check(s))
'''
def str_check(s):
    d=w=0
    for i in s:
        typ,amount=i.split(":")
        amount=int(amount)
        if typ=="D":
            d=d+amount
        else:
            w=w+amount
    return(d-w)
s=["D:300","D:300","W:200","D:100"] 
print(str_check(s))