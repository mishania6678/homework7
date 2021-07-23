from abc import ABC, abstractmethod


class Clothes:
    def __init__(self, v=0, h=0):
        self.v = v
        self.h = h

    @property
    @abstractmethod
    def get_square(self):
        return self.v * self.h


class Coat(Clothes):
    def __init__(self, v, h=0):
        super().__init__(v, h)
        self.v = v

    @property
    def get_square(self):
        return self.v / 6.5 + 0.5


class Costume(Clothes):
    def __init__(self, h, v=0):
        super().__init__(v, h)
        self.h = h

    @property
    def get_square(self):
        return 2 * self.h + 0.3


coat = Coat(13)
print(coat.get_square)
costume = Costume(6)
print(costume.get_square)


