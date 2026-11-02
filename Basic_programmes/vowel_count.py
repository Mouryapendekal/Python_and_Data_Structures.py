def vowel_count(n):
    vowels="aeiou"
    count=0
    for char in n:
        if char in vowels:
            count+=1
    return count
print(f"count={vowel_count('mourya')}")
