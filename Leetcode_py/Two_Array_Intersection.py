def intersect(num1,num2):
    re=[]
    s=set()
    for i in num1:
        if i in num2:
            s.add(i)
            re.append(i)
    return re
num1=[4,9,5]
num2=[9,4,9,8,4]
print(intersect(num1,num2))

