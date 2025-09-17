st=input("Enter some words :")
print("Non-repeated letters in given word :")
for i in st:
    if st.count(i)==1:
        print(i)