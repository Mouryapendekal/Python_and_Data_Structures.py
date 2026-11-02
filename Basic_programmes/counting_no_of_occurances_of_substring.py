s="ABCDCDCDC"
sub="CDCD"
count=0
n=len(s)
m=len(sub)
for i in range(n-m+1):
    if s[i:i+m]==sub:
        count=count+1
print(count)