user_number = int(input('Пожалуйста введите число : '))
m = user_number % 10
a = user_number // 10
while a > 0:
    if a % 10 > m:
        m = a % 10
    a = a // 10
print(m)



