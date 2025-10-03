'''partial Function :
It is used to fixed some arguments for passing into function'''
from functools import partial

print("Partial Functions :")
def bill(amount,gst):
    return amount*(1+gst)
gst_apply=partial(bill,gst=0.18)
print("amount with GST :",gst_apply(1000))

def create_email(username,domain):
    return f"{username}{domain}"
gmail=partial(create_email,domain="@gmail.com")
outlook=partial(create_email,domain="@outlook.com")
zmail=partial(create_email,domain="@zmail.com")
print("Mails :")
print(gmail("Bhaaji"))
print(outlook("Parvesh"))

'''Composed Function :
      When the output of one function become the input of another function  f(g(x))'''

def add(x):
    return x+3
def mul(x):
    return x*2
def compo(x):
    return add(mul(x)) #f(g(x))
print("Composed Function With Multiplication and Addition :",compo(2))

'''Callback Function is a function that you pass as an argument to another function,
so that it can be called(executed) later,usually after some action is completed.'''


def on_button_click(callback): #showcase
    print("Button Clicked !")  #once this line got executed
    callback()
def showcase():
    print("Hi Thaneish")
on_button_click(showcase)

'''Recursive Function :
call by itself !'''

def factorial(n):
    if n==1:
        return 1
    return n * factorial(n-1)
print("Recurssive Factorial :",factorial(5))

print("CountDown :")
def countdown(n):
    if n==0:
        return "BooOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOMMMMMMMMMMMMMMMMMMMMMMMM  !"
    print(n)
    return countdown(n-1)
print(countdown(10))

'''Generative Function :
It uses 'yield' to return values 1 by 1,instead of returning everything at once'''

#normal function
def normal_function(num):
    return [i for i in range(num)]
num=10
print("Normal Function :",normal_function(num))

#generative function
def generative_function(num):
    for i in range(num):
        yield i
num=10
print("Generative Function :")
for i in generative_function(num):
    print(i) #while using Generative Function (use iteration to get output)