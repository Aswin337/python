'''Dictionary :'''
student_details={"Name":"Aswin","Age":"19","Degree":"AI","District":"Madurai","Name":"Krishna"}#dictionary update Name automatically
print(student_details)

# Below,it considerd only key not value 
print(student_details["Name"])
#print(student_details["Aswin"])
print(student_details.get("Name"))
print(student_details.get("Madurai"))#it doesn't show error ,(Safe way to use)
print(student_details.keys())
print(student_details.values())
print(student_details.items())
student_details.pop("District")
print("After pop:",student_details)

#iteration
for key,value in student_details.items():
    print(f"{key} : {value}")
#update Dictionary
print("Before update :",student_details)
student_details.update({"Area":"MandelaNagar"})
print("After update :",student_details)
student_details.update({"Name":"Anachi"})
print("After update :",student_details)

#store each key for multiple values(List)
food_list={"Name":["Mudicheruky","Mani","Harish","krishna"],
      "Age":[22,18,19,20],
      "Fav_Food":["parotta","puri","dosa","chappati"],
      "Fav_Hotel":["Maaran parotta kadai","asaivam","sala","veetu kadai"]}
print(food_list["Name"][0])
print(food_list.get("Name")[0])
#all keys and value
for k,v in food_list.items():
    print(f"{k} : {v}")
#Fav_Food only
for food in food_list["Fav_Food"]:
    print(f"Favourite Food :{food}")
#each key with multiple values of dictionary
food_dict={"Mudicheruky":{"Age":22,"Fav_Food":"parotta","Fav_Hotel":"Maaran parotta kadai"},
           "Mani":{"Age":18,"Fav_Food":"puri","Fav_Hotel":"asaivam"},
           "Krishna":{"Age":20,"Fav_Food":"chappati","Fav_Hotel":"veetuku kadai"}}
print("krishna Age:",food_dict["Krishna"]["Age"])
for k,v in food_dict.items():
    print(k)
    print(str(v["Age"])+"-"+v["Fav_Food"]+"-"+v["Fav_Hotel"])