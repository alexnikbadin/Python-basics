my_list = input('Please, enter a numbers : ').split()
my_list_1 = [el for count, el in enumerate(my_list) if my_list[count - 1] < my_list[count]]
print(my_list_1)