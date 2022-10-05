class Person():
    __slots__ = ("_name")
    def __init__(self,name) -> None:
        self._name = name
    @property
    def name(self) -> str:
        return self._name
    """
    @name.setter
    def name(self, name: str):
        self._name = name
    """
    
p = Person('Jensen')
print("Name is", p.name)
p.age = 42
