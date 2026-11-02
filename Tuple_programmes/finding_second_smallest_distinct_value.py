# Find the second-smallest distinct value without min() or sort()
t = (5, 2, 8, 1, 4, 1)
small = None
second = None
for i in t:
    if small is None or i < small:
        if small != i:
            second = small
        small = i
    elif i != small and (second is None or i < second):
        second = i
print(second)  # 2