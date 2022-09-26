class Pyramid:
    def __init__(self, side,height,density):
        self.side = side
        self.height = height
        
    def volume(self):
        V = self.side * self.side * self.height / 3.0
        return V
    
class DensPyramid(Pyramid):
    def __init__(self, side, height, density):
        super().__init__(side, height, density)
        self.density = density
    def mass(self):
        M = self.density * self.volume()
        return M
p1 = DensPyramid(10,20,1.5)
p2 = DensPyramid(20,80,3.5)

print(p1.mass())
print(p2.mass())