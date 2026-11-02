s = 'year 2026'
d=y=sp=0
l=[]
di=[]
for i in s:
    if i.isalpha():
        d=d+1
        l.append(i)
    elif i.isdigit():
        y=y+1
        di.append(i)
    else:
        sp=sp+1
print(d,y,sp,"".join(l),"".join(di))