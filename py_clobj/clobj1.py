#class and object
class math:                        #class
    def square(self,num):          #method(inside class function called as method)
        return num*num
    def cube(self,num):            #method(inside class function called as method)
        return num*num*num
m=math()                           #object or instance
print("square :",m.square(7))
print("cube :",m.cube(3))
