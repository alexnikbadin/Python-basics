with open('incomes.txt', 'r') as f:
    income = f.read()
    income = income.split('\n')
less_20 = []
average_income = []
for string in income:
    string = string.split()
    if int(string[-1]) < 20:
        less_20.append(string[0])
    else:
        break
for string in income:
    string = string.split()
    average_income.append(int(string[-1]))
average_income = (map(int, average_income))
print(less_20)
print(sum(average_income) / len(income))


