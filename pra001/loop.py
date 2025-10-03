#for loop
names=["sakthi","harish","praveen","anachi","hari"]
for i in names:
    print(i.capitalize())#captilazise first letter

#while loop:
#password validation :
saved_pin="1234"
entered_pin=""
attempt=0
max_attempt=3
while saved_pin!=entered_pin and attempt<max_attempt:
    entered_pin=input("Enter correct pin :")
    attempt+=1
if saved_pin==entered_pin :
    print("Access Granted \U0001F44D")
else :
    print("Access Denied ! \U0001F6AB")

#break-to catch that member
names1=["praveen","dhivan","anachi","naveen","aswin"]
for caught in names1:
    if caught=="anachi":
        break
    print("break :",caught)

#continue-to skip that member
n=[1,-9,-2,7,3]
for i in n:
    if i < 0:
        continue
    print("continue :",i)

#countdown
countdown=10
print("countdown :")
while countdown>0:
    print(countdown)
    countdown-=1
print("Times up !")

#Add to cart
items=[]
while True :
    i=input("Add items(\"done\" to finish) :")
    if i.lower()=="done":
        break
    items.append(i)

print("Items in Cart :",items)