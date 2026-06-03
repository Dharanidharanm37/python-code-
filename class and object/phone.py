class phone():
    chargertype="ctype"
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
    def disp(self):
        print("brand:",self.brand)
        print("price:",self.price)
        print("chargertype:",self.chargertype)
    
phone.chargertype="b_type"
p1=phone("samsung","100000")
p2=phone("vivo","50000")

p1.disp()
p2.disp()
