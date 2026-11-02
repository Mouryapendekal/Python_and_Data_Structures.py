n="hello good morning welcome you"
s=n.split()
odd=[word for word in s if len(word)%2==1]
if odd:
    max_len=max(len(w) for w in odd)
    for w in odd:
        if len(w)==max_len:
            print(w)
            break
else:
    print("Better luck next time")