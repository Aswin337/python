st=input("Enter some words :")
vowels="aeiouAEIOU"
fi=""
for i in st:
    if i in vowels:
        fi+="*"
    else:
        fi+=i
print(fi)