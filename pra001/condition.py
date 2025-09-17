#elif
#mark based conditions:
mark=80
if mark >=90:
    print("Grade O")
elif mark >=80:
    print("Grade A")
elif mark >=70:
    print("Grade B")
else :
    print("Grade C")


#nested if :
student="yes"
First_Graduate="yes"
if student == "yes":
    if First_Graduate== "yes":
        print("Eligible for scholarship")
    else :
        print("Not Eligible for scholarship")
else :
    print("Not a student")
    
#if with 2 conditions :
mark=70
attendance=80
if mark>=70 and attendance>=90:
    print("Allowed to exam")
else :
    print("Not Allowed to exam")

#Food ordering discount with (and,or)
order_amount=1000
days="wed"
membership="yes"
if(order_amount>=1000 and days in ["sat","sun"]) or( membership=="yes") :#use and,or simultaneously
    print("20% Discount")
else :
    print("no discount")
