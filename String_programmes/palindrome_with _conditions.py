# Write a Python program to check whether a given string is a palindrome. The program should ignore spaces and case differences.
string="madam madam"
string=string.lower().replace(" ","")
if string==string[::-1]:
    print("palindrome")
else:
    print("not a palindrome")
print(string)