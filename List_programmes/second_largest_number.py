#Create a list of numbers and find the second-largest number.
n=[2,41,56,89,78,63,54,24,15,23]
# n.sort()
# print(n[-2])
# res=sorted(set(n))
# print(res[-2])
largest_num=n[0]
second=n[0]
for i in n:
    if i>largest_num:
        second=largest_num
        largest_num=i
    elif i>second and i!=largest_num:
        second=i
print(second)

