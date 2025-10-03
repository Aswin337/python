'''Lambda Functions (or) anonymous function:
It is one line function and easy to implement'''
from functools import reduce
res=lambda a,b:a+b
print(res(1,2))

res=lambda z:z**3
print(res(3))

students=["Harish","Rishi","Wukong"]
res=list(map(lambda student : student.upper().strip(),students))
print(res)

dept={"Anachi":"CSE","Wukong":"ECE","Aswin":"AI"}
res=list(filter(lambda student :dept[student]=="ECE",dept))
print(res)

x=[1,2,3,4,5,6,7]
even=list(filter(lambda x:x%2==0,x))
print(even)

x=[1,2,3,4,5,6,7]
sum=reduce(lambda a,b:a+b,x)
print("sum of x:",sum)

game=["Black Myth Wukong","Bhaaji","zeus","Thor"]
large=reduce(lambda a,b : a if len(a)>len(b) else b,game)
print("largest word in list:",large)

num =[870,900,1000,700,1200]
greater=list(filter( lambda x : x >=1000,num))
sum=reduce(lambda a,b :a+b,greater)
print("sum of > than 1000 :",sum)