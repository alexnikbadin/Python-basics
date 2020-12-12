text = input('Please, write something : ')

with open('first_task.txt', 'w') as f:
    for el in text:
        f.write(text + '\n')
