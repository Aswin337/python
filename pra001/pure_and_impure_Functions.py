'''If a function doesnt affect the outer function or method is called pure function.Its wise versa is pure function'''
total=0
#impure
def impure(amount):
    global total
    total+=amount
    return total
impure(3)
impure(4)
impure(7)
print("impure :",total)

#pure
def pure(amount):
    total=0
    total+=amount
    return total
pure(7)
print("pure :",total)
