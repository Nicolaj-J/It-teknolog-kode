class Store:
    totalnumber = 0
    def __init__(self):
        self.number = 0
    def __call__(self, number):
        self.number = self.number + number
        return self.number

store = Store()
print(store(2))
print(store(40))