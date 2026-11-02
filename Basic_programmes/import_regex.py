import re    
n="PPPPPP@PPP@PP$PP"
s=[]
m=re.split(r'[@$]',n)
k=[word for word in m]
s.append(k)
z=max(len(w) for w in k)
print(z)