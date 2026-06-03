class bro1():
    def __init__(self):
        print("bike")

class bro2(bro1):
    def __init__(self):
        print("car1")
    def car(self):
        super().__init__()
        print("car")


s1=bro2()
s1.__init__()
s1.car()


