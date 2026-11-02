n=5
count=0
for i in range(2,n):
    if n%i==0:
        count+=1
print(count)
if count==0:
    print("p")
else:
    print("n")