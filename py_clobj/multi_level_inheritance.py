class grandfather:
    def farm_land(self):
        print("Land location :Kanyakumari")
class dad(grandfather):
    def house(self):
        print("House :Red")
class son(dad):
    def factory(self):
        print("Factory : yellow")
    def house(self):
        print("House :Blue")
s=son()
s.factory()
s.house()
s.farm_land()

'''grandfather is parent of dad,then dad is parent of son .
   so, son access both methods like farm_land and horse'''