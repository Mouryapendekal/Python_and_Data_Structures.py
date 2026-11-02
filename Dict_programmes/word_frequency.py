#take a scentence create a dict containing each word its frequency.
s=input("enter a scentence:")
words=s.split()
f={}
high=0
high_word=""
for word in words:
    if word not in f:
        f[word]=1
    else:
        f[word]+=1
# for k,v in f.items():
#     print(k,":",v)
#     if v > high:
#         high=v
#         high_word=k
# print("The highest frequency :"high_word,":",high)
for k,v in f.items():
    print(k,":",v)
highest_word=max(f,key=f.get)
print(highest_word,":",f[highest_word])