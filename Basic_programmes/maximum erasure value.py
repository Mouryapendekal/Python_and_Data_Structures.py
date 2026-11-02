def maximum_erasure_value(n):
    erasure_values=set(n)
    total=0
    for i in erasure_values:
        total+=i
    return total
nums=input()
n=[int(nums) for nums in nums.split()]
print(maximum_erasure_value(n))