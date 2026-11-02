keys = ('HydBad','Bangalore','Chicago','New York')
dic = dict.fromkeys(keys)
for k,v in enumerate(dic,1):
    dic[v] = k   
print(dic)