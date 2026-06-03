class teacher():
    def __init__(self,nam,reg):
        self.name=nam
        self.reg=reg
    def disp(self):
        print("name:",self.name)
        print("regno:",self.reg)


teach=teacher("ajo","9187")
teach.disp()
