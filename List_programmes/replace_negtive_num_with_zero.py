# Create a list of numbers and replace every negative number with 0.
c=[-1,5,6,2,-2,-6,-7,-8,1,3,56,95,-42,-23]
# for i in range(len(c)):
#     if c[i]<0:
#         c[i]=0
# print(c)
w=[0 if i<0 else i for i in c]
print(w)