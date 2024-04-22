from pgm5 import world


class country(world):
    c = 100
    def __init__(self):
        world.__init__(self,10,20)
    def getnewsum(self):
        return country.c + world.num + self.sum()
x = country()
print(x.getnewsum())