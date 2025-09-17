def index(nums,target):
    for i in range(0,len(nums)):
        if nums[i]>target:
            nums.insert(i,target)
            break
    else:
        nums.append(target)
    res=nums.index(target)
    return res

lis=[1,3,5,6]
tar=7
res=index(lis,tar)
print(res)