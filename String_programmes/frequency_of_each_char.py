# Write a Python program to find the frequency of each character in a string and display the characters that occur more than once.
s = "programming"
checked = ""
for i in s:
    if i not in checked:
        count = s.count(i)
        if count > 1:
            print(i, "=", count)
        checked += i