import math

n = int(input())

def my_func(n):
    math.factorial(n)
    yield math.factorial(n)

# print(my_func(n))

fact = my_func(n)

for el in fact:
    print(el)



