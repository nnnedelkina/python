from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, title):
        self.title = title

    @abstractmethod
    def l_cloth(self):
        pass

    @property
    def summery(self):
        return f"{self.title}, требует {self.l_cloth(): .2f} метров ткани"


class Coat(Clothes):

    def __init__(self, v):
        Clothes.__init__(self, 'Пальто')
        self.v = v

    def l_cloth(self):
        return self.v/6.5 + 0.5


class Suit(Clothes):

    def __init__(self, h):
        Clothes.__init__(self, 'Костюм')
        self.h = h

    def l_cloth(self):
        return 2 * self.h + 0.3


c = Coat(56)
s = Suit(120)
print(c.summery)
print(s.summery)

