'''Accesss specifiers:
         *public
         *protected(_) 
         *private(__)'''

#Access specifiers in variables.
class parent:
    def __init__(self):
        self.a="I AM PUBLIC"        #public variable
        self._b="I AM PROTECTED"    #protected variable
        self.__c="I AM PRIVATE"     #private variable
    def access_same_class(self):
        print("INSIDE SAME CLASS :")
        print("public :",self.a)
        print("protected :",self._b)
        print("private :",self.__c)
class child(parent):
    def access_sub_class(self):
         print("INSIDE SUB(OR)CHILD CLASS :")
         print("public :",self.a)
         print("protected :",self._b)
         try:
            print("private :",self._parent__c)    #use name Mangalin for see that private content(Not recommended)
         except AttributeError:
            print("private variable cannot Access")
class strange:
    def access_strange_class(self,obj):
        print("INSIDE STRANGE CLASS :")
        print("public :",obj.a)
        print("protected :",obj._b)   #Not Recommended
        try:
            print("private :",obj.__c)
        except AttributeError:
            print("private variable cannot Access")

p=parent()
p.access_same_class()
c=child()
c.access_sub_class()
s=strange()
s.access_strange_class(p)