from abc import ABC, abstractmethod
import math

pi = math.pi

class Figure(ABC):
    @abstractmethod
    def area(self) -> float:
        print(self)

class Square(Figure):
    def __init__(self, width, height) -> None:
        super().__init__()
        self._width = width
        self._height = height
    def area(self) -> float:
        return float(self._width * self._height)
class Circle(Figure):
    def __init__(self,radius) -> None:
        super().__init__()
        self._radius = radius
    def area(self) -> float:
        return float(self._radius ** 2 * pi)
class Triangle(Figure):
    def __init__(self,base, height) -> None:
        super().__init__()
        self._base = base
        self._height = height
    def area(self) -> float:
        return float(self._base * self._height / 2)

figures = [Square(10,20), Circle(10),Triangle(10,20),42]
for f in figures:
    if isinstance(f, Figure):
        print("Area =", f.area())
    else: 
        print("Invalid value")