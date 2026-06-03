class mom():
    def phone(self):
        print("mom phone")

class dad():
    def money(self):
        print("dad money")

class son1(mom,dad):
    def laptop(self):
        print("oc lap")

class son2(mom):
    def bike(self):
        print("oc bike")


s1=son1()
s1.laptop()
s1.money()
s1.phone()

