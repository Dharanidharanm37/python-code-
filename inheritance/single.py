class mom():
    def phone(self):
        print("mom phone")

class dad(mom):
    def money(self):
        print("dad money")

class son1(mom):
    def laptop(self):
        print("oc lap")

class son2(mom):
    def bike(self):
        print("oc bike")


s1=son1()
s1.laptop()
s1.phone()

d2=dad()
d2.money()
d2.phone()

s2=son2()
s2.phone()
s2.bike()

