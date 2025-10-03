'''encapsulation :
restricting direct access to some of the objects componenets'''

class order:
    def __init__(self,name,items,total_amount,discount): #constructor
        self.name=name
        self.it=items
        self.__totalamount=total_amount    #private variable
        self.__discount=discount           #private variable
    def __calculation(self):     #private method
        return self.__totalamount-self.__discount
    def _access_by_admin(self):   #protected method
        return {
            "Customer Name :":self.name,
            "Odered Items :":self.it,
            "Total Amount :":self.__totalamount,
            "Discount :":self.__discount,
            "Final Amount :" :self.__calculation()
        }
    def access_by_customer(self):     #public method
        return {
            "Customer Name :":self.name,
            "Odered Items :":self.it,
            "Final Amount :" :self.__calculation()
        }
class admin:   #stranger class
    def show_order(self,obj):
        print("Admin view :")
        return obj._access_by_admin()
class customer:   #stranger class
    def show_order(self,obj):
        print("Customer view :")
        return obj.access_by_customer()
ord=order("Aswin",["Dosa","Chappati"],500,100)
ad=admin()
print(ad.show_order(ord))
cust=customer()
print(cust.show_order(ord))


