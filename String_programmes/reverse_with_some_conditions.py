# Write a Python program that displays:
# the string in reverse
# the words in reverse order
# each word with its characters reversed.
s = "Python is very easy"
print("the string in reverse:",s[::-1])
words=s.split()
print("the words in reverse order"," ".join(words[::-1]))
res=[]
for word in words:
    res.append(word[::-1])
print("Each word reversed:", " ".join(res))