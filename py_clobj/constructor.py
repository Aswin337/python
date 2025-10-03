'''Class with constructor :'''

class student:
    def __init__(self,name,rollno):       #__init__=constructor
        self.x=name                       #stored once
        self.y=rollno                     #stored once
    def attendance(self):                 #method(inside class function called as method)
        print(f"{self.x} enters attendance using {self.y}")
    def exam(self):
        print(f"{self.x} seat alloted using {self.y}")
s=student("Mudicheruky","23ucs001")
s.attendance()
s.exam()
        
'''stored once using constructor then call by any methods(def) inside class'''