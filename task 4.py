# def my_func(x, y):
#     return x**abs(y)
#
#
# x = int(input('Enter positive number'))
# y = int(input('Enter negative number'))
#
#
# print(my_func(x, y))

#2



def my_func(x, y):
    count = 1
    while count < abs(y):
        (x * abs(y)) * abs(y)
        count = count + 1
    return None




x = int(input('Enter positive number'))
y = int(input('Enter negative number'))

result = my_func(x, y)
print(result)