class ComplexNumber:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return ComplexNumber(self.x + other.x, self.y + other.y)


    def __mul__(self, other):
        return ComplexNumber(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f'{str(self.x)} + {str(self.y)}'


first_number = ComplexNumber(int(input('Enter a number : ')), int(input('Enter a number : ')))
second_number = ComplexNumber(int(input('Enter a number : ')), int(input('Enter a number : ')))
print(f'({str(first_number)}) * ({str(second_number)})')
print(f'({str(first_number)}) + ({str(second_number)})')






