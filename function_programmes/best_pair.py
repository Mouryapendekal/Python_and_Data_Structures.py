#take a list of elemets ,and the sum of pair is equal to 10 , take those pairs in another list,
# find which pair difference is minimum and make it as best pair print those  index values .

# count=8
# seats=[1,8,2,4,6,9,5,3]
# t=10
# m=[]
# for i in seats:
#     for j in seats:
#         if i+j==t:
#             m.append(i)
# best_pair=None
# min_diff=float('inf')
# s=set(m)
# for num in m:
#     target=t-num
#     if target in s and num<target:
#         diff=abs(num-target)
#         if diff<min_diff:
#             min_diff=diff
#             best_pair=(num,target)
# print(best_pair)
# v=seats.index(best_pair[0])
# u=seats.index(best_pair[1])
# print(v,u)

def find_pair(seats,t):
    m=[]
    for i in seats:
        for j in seats:
            if i+j==t:
                m.append(i)
    return m
def best_pair_diff(seats,t):
    m=find_pair(seats,t)
    best_pair = None
    min_diff = float('inf')
    s = set(m)
    for num in m:
        target = t - num
        if target in s and num < target:
            diff = abs(num - target)
            if diff < min_diff:
                min_diff = diff
                best_pair = (num, target)
    if best_pair:
        v = seats.index(best_pair[0])
        u = seats.index(best_pair[1])
        return best_pair, (v, u)
    return "There is no best pair"
seats = [1, 8, 2, 4, 6, 9, 5, 3]
t = 10
print(best_pair_diff(seats, t))