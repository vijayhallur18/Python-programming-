class vechicle:
    def __init__(self,mileage,cost):
        self.mileage=mileage
        self.cost=cost
    def show_details(self):
        print("i am a vechile")
        print("mileage of vechile is :",self.mileage)
        print("cost of vechile",self.cost)

v1=vechicle(500,500)
v1.show_details()

class car(vechicle):
    def __init__(self, mileage, cost,tyres,hp):
        super().__init__(mileage, cost)
        self.tyres=tyres
        self.hp=hp
    def show_car_details(self):
        print("i am a car")
        print("number of tyres are ",self.tyres)
        print("value of horse power is ",self.hp)

c1=car(20,12000,4,300)
c1.show_car_details()