class cricketr:
    def __init__(self,name,age,team):
        self.name=name
        self.age=age
        self.team=team
    def cricketr_details(self):
        print("Name of cricketr is :",self.name)
        print("age of the cricketr is :",self.age)
        print("team of the cricketr is :",self.team)
c1=cricketr("virat kholi",37,"RCB")
c1.cricketr_details()        