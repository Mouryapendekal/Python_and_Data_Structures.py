#Check whether a tuple is a palindrome
t = (1, 2, 3, 2, 1)
if t == t[::-1]:
    print("Palindrome")
else:
    print("Not palindrome")