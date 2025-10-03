def plus_one(arr):
    s="".join([str(i) for i in arr])
    a=int(s)+1
    dig=[int(i) for i in str(a)]
    return dig
arr=[1,1,2]
print(plus_one(arr))
