'''Higher order Function :
1.First class Function
2.take another function as argument
3.returns a function as its output'''

#First class funtion:
def build_email(username,domain):
    if domain=="gmail":
        return f"{username}@{domain}.com"
    elif domain=="ymail":
        return f"{username}@{domain}.com"
    elif domain=="zmail":
        return f"{username}@{domain}.com"
    else:
        return f"{username}@example.com"

print("1.")
print(build_email("Hari","gmail"))
print(build_email("praveen","ymail"))
print(build_email("Anachi","unknown"))

#take another function as argument
def gmail_email(username,domain="@gmail.com"):
    return f"{username}{domain}"

def ymail_email(username,domain="@ymail.com"):
    return f"{username}{domain}"

def outlook_email(username,domain="@outlook.com"):
    return f"{username}{domain}"

def build_email(username,email_func):
    #print(type(email_func))
    return email_func(username) #gmail_email("Hari")

print("2.")
print(build_email("Hari",gmail_email))
print(build_email("praveen",ymail_email))
print(build_email("Anachi",outlook_email))

#Return a function as its output
def email_builder(domain):
    def build_email(username):
        return f"{username}{domain}"
    return build_email  #the function build_email is returned       


gmail=email_builder("@gmail.com")
#Now gmail refers to this returned function(build_email) and other also 
zmail=email_builder("@zmail.com")
outlook=email_builder("@outlook.com")

print("3.")
print(gmail("Suresh"))  #It runs the build_email function
print(zmail("Rajesh"))
print(outlook("Anachi"))

