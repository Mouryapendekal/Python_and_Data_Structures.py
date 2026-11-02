def remove(s, i):
    if i < 0 or i >= len(s):
        return s
    return s[:i] + s[i+1:]
s = input().strip()
i = int(input("enter index to remove"))
print(remove(s, i)) 