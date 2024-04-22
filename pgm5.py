class world:
    num =100
    def __init__(self,a,b):
        self.num1 = a
        self.num2 = b

    def getdata(self):
        print("I am very happy")

    def sum(self):
         return self.num1+ self.num2 + world.num
c = world(6,8)
print(c.sum())
c.getdata()



