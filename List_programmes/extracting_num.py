#Write a Python program using list comprehension to extract numbers greater than 10.
num=[2,21,3,31,4,45,5,26,6,56,7,63,8,57,9,74,83,90]
res=[i for i in num if i>10]
print(res)