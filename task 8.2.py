class MyErrors(Exception):

    def __init__(self):
        pass

    def Zero_division_error(self, number_1, number_2):
        self.number_1 = number_1
        self.number_2 = number_2
        try:
            number_1 / number_2
        except ZeroDivisionError:
            print('You cannot do that!')
        return number_1 / number_2


example = MyErrors()
print(example.Zero_division_error(int(input('Enter a number : ')), int(input('Enter a number once again : '))))





