#find the frequency of each element
t = (1, 2, 1, 3, 2, 1)
for i in t:
    if t.index(i) == t.index(i):
        if i not in t[:t.index(i)]:
            print(i, "=", t.count(i))