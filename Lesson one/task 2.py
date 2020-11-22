enter_seconds = int(input('Введите количество секунд : '))
hours = enter_seconds//3600
minutes = (enter_seconds - (hours * 3600))//60
seconds = enter_seconds - (hours * 3600 + minutes * 60)
print(f"{hours} : {minutes} : {seconds}")

