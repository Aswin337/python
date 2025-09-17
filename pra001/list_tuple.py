#Last:

playlist=["believer","oo antava","jingnamani","thatha phonk","badass"]
toppers=["praveens","hari sanjay","hari","sharma","sivabalan"]
fav_food=["parrota","chappati","dosa","idiyappam","aappam"]
print("Playlist :",playlist)
print("Toppers :",toppers)
print("Favourite food :",fav_food)
#List Methods
playlist.append("jingucha")#add elements in last
print("Playlist :",playlist)
playlist.insert(2,"Arise")#add element based on index
print("Playlist :",playlist)
playlist.remove("believer")#remove element to give
print("Playlist :",playlist)
playlist.pop()#remove last element
print("Playlist :",playlist)
playlist.reverse()#reverse entire list
print("Playlist :",playlist)
print("count :",playlist.count("jingnamani"))#count selected word in list


#slicing :take particular part in list
print("First 2 toppers :",toppers[:2])
print("Last 2 toppers :",toppers[-2:])
print("Between 2 toppers :",toppers[2:4])


#iteration
print("Favourite food :",fav_food)
for food in fav_food:
    print(food,"-Maran Porrota kadai")


#change some values:
fav_food[0]="chilli parotta"
print("Favourite food :",fav_food)

#multiple type elements
lst=["Aswin",19,70.0]
for each in lst:
    print(f"type : {type(each)} and element : {each}")

#enumerate-give index for each element in list
fav_food=["parrota","chappati","dosa","idiyappam","aappam"]
for i,food in enumerate(fav_food):
    print(f"index {i} :{food}")


#tuple :
cab=("uber","Villapuram","Airport",100.0)
print(cab.count("uber"))
print(cab.index("uber"))