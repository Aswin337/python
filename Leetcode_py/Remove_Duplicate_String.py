def duplicate(nums):
    nlis=[]
    for i in nums:
        if i in nlis:
            nlis.append("_")
        else :
            nlis.append(i)
    nlis.sort(key=lambda x:(str(x)=="_",x))
    return nlis
lis=[1,2,1,1,2,3]
d=duplicate(lis)
print(d)