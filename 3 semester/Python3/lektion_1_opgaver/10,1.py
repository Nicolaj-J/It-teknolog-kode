class Pyramid:
    def __init__(self,side,height):
        self.side = side
        self.height = height
        
    def volume(self):
        V = self.side * self.side * self.height / 3.0
        return V
p1 = Pyramid(10,20)
print(p1.volume())
p2 = Pyramid(25,80)
print(p2.volume())


