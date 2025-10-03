#we have to discuss about variable scopes
student_name="Aswin" #Global variable
def college():
    student_department="CSE"  #Local Variable
    def semester():
        student_Grade=8.3 #Enclosed Variable
        print(f"{student_name} from {student_department} department get  CGPA of {student_Grade} in this current semester")
    semester()
college()
print(__file__) #Built-in variable