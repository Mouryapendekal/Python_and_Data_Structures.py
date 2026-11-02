# Write a Python program to remove duplicate characters from a string while maintaining their original order.
# s = "programming"
# result = ""
# for i in s:
#     if i not in result:
#         result += i
# print(result)

s = "programming"
result = ''.join(dict.fromkeys(s))
print(result)



        
    
        
     
        
     
        
    
        