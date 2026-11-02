def del_chr(str1,str2):
    lst=list(str1)
    lst.remove(str2)
    res_str=" ".join(lst)
    return res_str
print(del_chr("PYTHON",'N'))