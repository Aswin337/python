#Function is used to make the code reusable(with return only)
def add(a,b):
    print(a+b)
add(1,2)


#with return
def add(a,b):
    return a+b #it return addition value to res
res=add(3,2)
print(res)

#*args  to pass a variable number of arguments to a function
#numbers
def add(*args):
   total=0
   for num in args:
        total+=num
   return total
res=add(3,2,4)
print(res)
#names
def greet(*args):  #args is just name we call it like *num,*anachi
    lst=[]
    for name in args:
        print(f"Hello {name} ! ")
        lst.append(name)
    return lst
res=greet("sakthi","sharma","anachi")
print(res)


#**kwargs to pass (key-value pairs)
def info(**kwargs):
    for key,value in kwargs.items():
        print(f"{key} : {value}")
info(name="Anachi",age=20,job="App developer")

