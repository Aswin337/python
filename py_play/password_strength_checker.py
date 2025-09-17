'''Normal method :'''
print("1st Method :")
def password_strength_chk(p):
  has_upper=False
  has_lower=False
  has_digit=False
  has_special=False
  special_characters="!@#$%^&*()/*-+"
  if len(p) < 8:
    print("Password Must be Atleast 8 characters")
  for char in p:
    if char.isupper():
      has_upper=True
    elif char.islower():
      has_lower=True
    elif char.isdigit():
      has_digit=True
    elif char in special_characters:
      has_special=True

  if has_upper==False:
    print("Password Must contain Atleast 1 upper character")
  if has_lower==False:
    print("Password Must contain Atleast 1 lower character")
  if has_digit==False:
    print("Password Must contain Atleast 1 digit")
  if has_special==False:
    print("Password Must contain Atleast 1 special character")

  if len(p)>8 and has_upper and has_lower and has_digit and has_special :
    print("Strong Password ! ,It should be good")

pWord=input("Enter your password :")
password_strength_chk(pWord)

'''Regular Expression(re) method'''
print("2nd method :")
import re
def password_stg_chk(ps):
  errors=[]
  if len(ps) < 8:
    errors.append("Password Must be Atleast 8 characters")
  if not re.search(r"[A-Z]",ps):
    errors.append("Password Must contain Atleast 1 upper character")
  if not re.search(r"[a-z]",ps):
    errors.append("Password Must contain Atleast 1 lower character")
  if not re.search(r"[0-9]",ps):
    errors.append("Password Must contain Atleast 1 digit")
  if not re.search(r"[!@#$%^&*()/*-+]",ps):
    errors.append("Password Must contain Atleast 1 special character")
  if errors:
    print("password is not Strong !:")
    for error in errors:
      print(error)
  else:
    print("Strong password !")
password_stg_chk(pWord)

  
