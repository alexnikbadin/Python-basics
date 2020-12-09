from itertools import count, cycle

for el in count(3):
    if el > 10:
        break
    else:
        print(el)


my_list = input('Please, enter a numbers : ').split()
number = 0
for el in cycle(my_list):
    if number < 10:
        print(el)
    else:
        break
    number += 1


