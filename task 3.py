def my_func(num_1, num_2, num_3):
    if num_1 >= num_2 and num_2 > num_3:
        return (num_1 + num_2)
    elif num_2 >= num_3 and num_3 > num_1:
        return (num_2 + num_3)
    elif num_3 >= num_1 and num_1 > num_2:
        return (num_1 + num_3)
    else:
        return (num_2 + num_3)

    
    # if num_1 == min(my_func(num_1, num_2, num_3)):
    #     return (num_2 + num_3)
    #  Пытался попробовать возможно ли решить так. Не получилось


num_1 = int(input('enter'))
num_2 = int(input('enter'))
num_3 = int(input('enter'))


result = my_func(num_1, num_2, num_3)
print(result)
