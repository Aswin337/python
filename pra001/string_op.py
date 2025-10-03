'''Lets play with String'''
a="i am aswin"
fi=a.split()#split by empty space
print(a.title())#caps first letter in whole sentence
print(fi[2].capitalize())#caps first letter
print(fi[2].upper())#upper case
print(fi[2].lower())#lower case


b="My rollno is : 23ucs114 "
si=b.split(":")[1]#split by :(colon)
print(si)
print(si.strip())#removes spaces from front and back


#replace one word to another
Rollno="23ucs114"
rep=Rollno.replace("23ucs114","23ucs014")
print("New Rollno :",rep)


#Hide some content in mobile no
mobile="8475675321"
hide=mobile[:2]+"******"+mobile[-2:]
print(hide)


#used to particular word or character present in string or not
promo_code="use Anachi100 to get 30% off"
if "Anachi100" in promo_code :
    print("offer applied !")


#used to find postion of particular word or character in a string
pos=promo_code.find("Anachi100")
print("Postion of Anachi100 :",pos)


#take first letter from each word in str
str="hi harish nalla irukiya"
fisl=([word[0].upper() for word in str.split()])
fiss=" ".join([word[0].upper() for word in str.split()])#without list
print(fisl)
print(fiss)


#count each word in string
word1="Hari Sanjay was brilliant student in our class"
count=len(word1.split())
print("count of word1 :",count)