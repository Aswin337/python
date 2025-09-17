import emoji
def emojize(text):
    return emoji.emojize(text,language="alias")
def movie(select,movies):
    lis=[]
    for i in movies:
        if i == select.strip():
            lis.append(i)
    return lis
def seat(seats):
    lis=[]
    print(emojize(":seat: Available Seats :"))
    print(seats)
    while True :
        i=input("Enter your seats (done to Finish) :")
        if i.lower() == "done":
            break
        if i.lower().strip() in seats:
            lis.append(i.lower().strip())
            seats.remove(i.lower().strip())
        else:
            print("Sorry ! This seat is not Available")
    return lis
def amount(s):
    l=len(s)*200
    pay=int(input(f"pay {l} :"))
    if pay == l:
        print("Hurray ! Your Seats Booked Successfully")
    elif pay >= l:
        a=pay - l
        print("Hurray ! Your Seats Booked Successfully")
        print("Balance :",a)
    else:
        print(" sorry Your Amount is not enough to book these Tickets")
movies=["F1","Demon Slayer","Super man","Tourist Family"]
seats=["a1","a2","a3","b1","b2","b3","c1","c2","c3"]
print(emojize("\n:clapper_board: Welcome App Movie Ticket Booking System :ticket:"))
print(emojize(":popcorn: Available Movies :"))
print(movies)
select=input("Enter movie :")
print("selected Movie:")
print(movie(select,movies))
s=seat(seats)
print(s)
print(f"Ticket Price {len(s)*200} is ready to pay !")
amount(s)