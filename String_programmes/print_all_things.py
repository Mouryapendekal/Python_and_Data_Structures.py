string="Python Is a* Dynamic! Language^ 98"
char=words=spaces=vowels=consonants=digits=alpha=uppercase=lowercase=special=0
# l=list(string)
# char=len(l)
w=string.split()
words=len(w)
for i in string:
    char=char+1

    if i in "aeiouAEIOU":
        vowels+=1
    else:
        consonants+=1
    if i.isdigit():
        digits+=1
    if i.isalpha():
        alpha+=1
    if i>="A" and i<="Z":
        uppercase+=1
    if i>="a" and i<="z":
        lowercase+=1
    if i==" ":
        spaces+=1
    if not i.isalnum() and i!=" ":
        special+=1
print("No of char in string:",char)
print("No of words in string:",words)
print("vowels:",vowels)
print("consonants:",consonants)
print("no of spaces in string:",spaces)
print("no of digits in given string:",digits)
print("no of alphabets in given string:",alpha)
print("no of uppercase in given string:",uppercase)
print("no of lowercase in given string:",lowercase)
print("no of special charecters in given string:",special)
