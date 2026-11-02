def count_with_positions(string,sub):
    count=0
    pos=[]
    i=string.find(sub)
    while i!=-1:
        count+=1
        pos.append(i)
        i=string.find(sub,i+1)
    return count,pos
string="ABCDCDC"
sub="CDC"
count,pos=count_with_positions(string,sub)
print(count,pos)

# s= "ABCDCDC"
# sub = 'CDC'
# count = 0
# pos=[]
# n = len(s) 
# m = len(sub)
# for i in range(n-m+1):
#     if s[i:i+m]==sub:
#         count+=1
#         pos.append(i)
# print(count,pos)
