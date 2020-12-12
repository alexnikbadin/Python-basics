rus_numbers = ["Один", "Два", "Три", "Четыре"]
i = 0
with open('numbers.txt', 'r') as f:
    for line in f:
        line = line.split()
        line.reverse()
        del line[2]
        line.append(rus_numbers[i])
        i += 1
        line.reverse()
        line = ' '.join(line)
        print(line)
        # map(str, line)


with open('new_numbers.txt', 'w') as f_new:
    f_new.writelines(line)



