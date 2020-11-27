my_list = [5, 8, 8, 6, 3, 3]
print(type(my_list[0]))
for number in my_list:
    number = int(input('Пожалуйста, введите число : '))
    if number == my_list[0]:
        my_list.insert(1, number)
    elif number == my_list[2]:
        my_list.insert(3, number)
    elif number == my_list[3]:
        my_list.insert(4, number)
    elif number < my_list[0]:
        my_list.insert(0, number)
    else:
        my_list.append(number)
    print(my_list)



