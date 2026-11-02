n="gOOd morning mam hello world"
s=n.lower().split(" ")
for i in s:
    count=0
    for j in i:
        if (j not in "aeiou"):
            count+=1
    print(f"count of {i}:{count}")