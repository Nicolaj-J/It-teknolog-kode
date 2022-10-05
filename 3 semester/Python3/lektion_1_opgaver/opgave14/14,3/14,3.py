from __future__ import annotations

class Elapsed():
    def __init__(self,hours: int, minutes: int, seconds: int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.time = f"{self.hours}:{self.minutes:02d}:{self.seconds:02d}"
    def __str__(self) -> str:
        return self.time
    def __repr__(self) -> str:
        return repr(self.time)
    def getTotal(self) -> int:
        return self.seconds + (self.minutes * 60) + (self.hours * 3600)
    @staticmethod
    def getHMS(total: int):
        seconds = (total % 3600) % 60
        minutes = ((total - seconds) % 3600) / 60
        hours = ((total - seconds) -minutes * 60)/3600
        return int(hours),int(minutes),int(seconds)
    def __add__(self, other: 'Elapsed') -> 'Elapsed':
        duo = self.getTotal() + other.getTotal()
        tmp = Elapsed(*Elapsed.getHMS(duo))
        return tmp
e1 = Elapsed(1,45,10)
e2 = Elapsed(0,23,56)
print(e1.getTotal())
print(e2.getTotal())
print(Elapsed.getHMS(e1.getTotal()))
e3 = e1 + e2
print(e3)