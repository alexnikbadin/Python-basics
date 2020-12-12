with open('first_task.txt', 'r') as f:
    info = f.readlines()
print(info)
print(len(info)) #количество строк
for i, v in enumerate(info):
    words_count = len(v.split())
    print(words_count)
    