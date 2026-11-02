s= "abracadabra"
l=[]
for i in s:
    l.append(i)
l[5]="k"
s="".join(l)
print(s)