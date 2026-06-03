class student():
    def __init__(self):
        self.name=""
        self.reg=""
    def display(self):
        print("name:",self.name)
        print("regno:",self.reg)

s1=student()
s2=student()

s1.name="ajo"
s1.reg="1987"

s2.name="vishwa"
s2.reg="1334"

s1.display()
s2.display()
