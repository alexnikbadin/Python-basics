with open('numbers_sum.txt', "w+") as f:
    numbers = input("Enter numbers : ").split(' ')
    f.writelines(numbers)
    numbers_sum = sum(map(int, numbers))
    print(numbers_sum)
