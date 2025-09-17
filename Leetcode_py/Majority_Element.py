from collections import Counter
def majority_ele(nums):
    s=Counter(nums)
    m=max(s.values())
    for k,v in s.items():
        if m == v:
            return k
nums=[3,2,3]
print(majority_ele(nums))