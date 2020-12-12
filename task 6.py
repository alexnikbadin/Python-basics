subjects = []
hours = []
with open('subjects.txt', 'r') as f:
    for line in f:
        line = line.split()
        subjects.append(line[0])
        del line[0]
        line = [el for el in list(' '.join(line))]
        print(line)
print(subjects)
# Разбил посимвольно списки с числами и создал список дисциплин. Идея была в создании списка чисел, калькулировании их и на их основе создании словаря.
# Реализовать эту идею до конца не сумел.

