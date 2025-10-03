''''These type of input didnt Schedulers to give input at a particular time using database,website etc,....
Schedulers:
        Schedulers is used to run a program at particular time'''
#String Input:
'''a=input("Enter your name :")
print(a)
#Numerical input:
b=int(input("Enter your Favourite Number :"))
print(b)
'''
#so we use System directly to give input using (sys.argv) and these an be support schedulers
#single name:
import sys
'''
if len(sys.argv) == 2 :
    print("usage : EmailCreation so Enter First_name and Last_name")
    sys.exit()
first_name=sys.argv[1]
last_name=sys.argv[2]
#Format name
email=first_name.lower().replace(" ",".")+last_name.lower()+"@gmail.com"
#output :
print("Full_name :",first_name+last_name)
print("Email :",email)
'''
#take first,middle,last name in one line
#it takes multiple name but list
#full_name=sys.argv[1:]
#so we convert into string
full_name=" ".join(sys.argv[1:])
#Format name
email=full_name.lower().replace(" ",".")+"@gmail.com"
#output
print("Full name :",full_name)
print("Email :",email)