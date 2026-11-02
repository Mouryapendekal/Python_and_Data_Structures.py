def is_palindrome(n):
    rev=""
    for char in n:
        rev=char+rev
    return rev==n
word=input("enter the word:")
if is_palindrome(word):
    print("palindrome")
else:
    print("not  a palindrome")