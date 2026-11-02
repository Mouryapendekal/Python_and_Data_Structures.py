def count_substring(string,substring):
    count=0
    i=string.find(substring)
    while i!=-1:
        count+=1
        i=string.find(substring,i+1)
    return count
string="ABCDCDC"
substring="CDC"
print(count_substring(string,substring))