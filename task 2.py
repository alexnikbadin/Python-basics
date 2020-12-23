from abc import ABC, abstractmethod


class Clothes(ABC):

    @abstractmethod
    def cloth_coat(self, size):
        pass

    @abstractmethod
    def cloth_suit(self, height):
        pass


class Coat(Clothes):

    def __init__(self):
        pass

    def cloth_coat(self, size):
        self.size = size
        result_coat = size / 6.5 + 0.5
        return result_coat

    def cloth_suit(self, height):
        pass

    @property
    def result_1(self):
        return self.result_coat

    @result_1.setter
    def result_1(self, result_1):
        self.result_coat = result_1

class Suit(Clothes):

    def __init__(self):
        pass

    def cloth_coat(self, size):
        pass

    def cloth_suit(self, height):
        self.height = height
        result_suit = 2 * self.height + 0.3
        return result_suit

    @property
    def result_2(self):
        return self.result_suit

    @result_2.setter
    def result_2(self, result_2):
        self.result_suit = result_2


my_coat = Coat()
my_suit = Suit()
print(my_coat.cloth_coat(int(input('Enter the size of the coat : '))))
print(my_suit.cloth_suit(int(input('Enter the height of the suit : '))))
my_coat.result_1 = int(input('Enter the volume of the coat cloth : '))
my_suit.result_2 = int(input('Enter the volume of the suit cloth : '))
print(f'Total cloths volume is {my_suit.result_2 + my_coat.result_1} metres')
