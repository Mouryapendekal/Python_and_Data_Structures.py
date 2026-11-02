# Write a Python program using list comprehension to extract all vowels from the string.
s='RAMU IS DECEnt boy as known as vishnu'
lst=list(s)
n=[i for i in lst if i in 'AEIOUaeiou']
print(n)
