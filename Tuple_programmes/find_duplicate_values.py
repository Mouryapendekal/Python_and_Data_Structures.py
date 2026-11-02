t = (10, 20, 30, 20, 40, 10)
seen = ()
duplicates = ()
for i in t:
    if i in seen:
        if i not in duplicates:
            duplicates += (i,)
    else:
        seen += (i,)
print(duplicates)  # (20, 10)