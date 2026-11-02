a=[7,6,8,16,12,3]
b=sorted(a)
d=max(b)
sum=0
for i in b:
    sum=sum+(i*d)
print(sum)
