#set : unodered(no index) and mutable
#List to Set
fav_food=["idiyappam","chappati","dosa","idiyappam","chappati"]
unique_food=set(fav_food)
print(unique_food)

#some changes in set
fav_food={"idiyappam","chappati","dosa","idiyappam","chappati"}
print("Favourite unqiue foods :",fav_food)
fav_food.add("chilli")
print("Favourite food after added :",fav_food)
fav_food.remove("dosa")
print("Favourite food after removed :",fav_food)
'''use remove() if that word not in set it shows error alternative -discard() '''
fav_food.discard("kiruthika")#kiruthika is not in set so it print remaing element
print("Favourite food after removed :",fav_food)
