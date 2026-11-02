# Write a Python program to find the longest word, shortest word, total number of words, and frequency of each word in a sentence.
sentence = "Python is easy and Python is powerful"
words = sentence.split()
print("Total No of words :",len(words))
longest_word=max(words,key=len)
shortest_word=min(words,key=len)
print("longest_word :",longest_word)
print("shortest_word :",shortest_word)
frequency={}
for word in words:
    if word in frequency:
        frequency[word]+=1
    else:
        frequency[word]=1
print(frequency)
for word in frequency:
    print(word, "=", frequency[word])