def simcal (a,b,cal):
    cal=cal.lower()
    if cal=="add":
         c=a+b
    elif cal=="sub":
         c=a-b
    elif cal=="mul":
         c=a*b
    elif cal=="quo":
         c=a/b
    elif cal=="rem":
         c=a%b
    else:
         c="Give valid input !"
    return c
a=int(input("Enter Number 1:"))
b=int(input("Enter Number 2:"))
str=input("Enter the Calculation Tyoe(ADD,SUB,MUL,quo,rem) :")
s=simcal(a,b,str)
print("Your Calculation :",s)