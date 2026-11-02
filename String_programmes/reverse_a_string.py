def reverse_str(s):
    s1=''
    for char in s:
        s1 = char + s1 
    return s1
print(reverse_str("welcome"))