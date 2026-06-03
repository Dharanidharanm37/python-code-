class calculator():
    def __init__(self,num1,num2):
        self.a=num1
        self.b=num2
    def add(self):
        print("addition:",self.a+self.b)
    def sub(self):
        print("sub:",self.a-self.b)
    def mul(self):
        print("mul:",self.a*self.b)
    def div(self):
        print("div:",self.a/self.b)
    


cal=calculator(4,8)
cal.add()
cal.sub()
cal.sub()
cal.div()
