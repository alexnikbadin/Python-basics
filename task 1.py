
class Matrix:
    def __init__(self, my_list):
        self.my_list = my_list

    def __str__(self):
        return '\n'.join(map(str, self.my_list))

    def __add__(self, other):
        i = 0
        return Matrix([x+y for x, y in zip(self.my_list[i], other.my_list[i])])
#     не смог прикрутить в генератор счетчик i для сложения всех элементов..((


my_matrix = Matrix([[1, 5, 8],
                    [2, 6, 9],
                    [3, 99, 7]])

my_matrix_2 = Matrix([[34, 87, 90],
                      [45, 7, 12],
                      [34, 123, 345]])


print(my_matrix.my_list)
print(my_matrix)
print(my_matrix + my_matrix_2)
