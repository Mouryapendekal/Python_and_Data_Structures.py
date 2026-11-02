#replace all occurrences of the first character of a string with $, except for the first occurrence itself.
def change_char(str1):
    char=str1[0]
    str1=str1.replace(char,"$")
    str1=char+str1[1:]
    return str1
print(change_char("mourya moumym"))