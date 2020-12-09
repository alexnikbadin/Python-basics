my_list = list(map(int, input('Please, enter a numbers : ').split()))
my_list_1 = []
i = 0
for el in range(len(my_list) - 1):
    if my_list[i] < my_list[i+1]:
        my_list_1.append(my_list[i+1])
    i += 1

print(my_list_1)
