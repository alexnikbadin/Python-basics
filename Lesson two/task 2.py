my_list = []
my_list.append(input('Введите данные : '))
my_list.append(input('Введите данные : '))
my_list.append(input('Введите данные : '))
my_list.append(input('Введите данные : '))
print(my_list)
my_list[0], my_list[1] = my_list[1], my_list[0]
my_list[2], my_list[3] = my_list[3], my_list[2]
print(my_list)