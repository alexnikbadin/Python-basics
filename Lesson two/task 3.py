#Решение со списком
seasons = ['Winter', 'Spring', 'Summer', 'Fall']
month = int(input("Please, enter the number of the month "))
if month == 1 or month == 2 or month == 12:
    print('There is a', seasons[0], 'outside')
elif month == 3 or month == 4 or month == 5:
    print('There is a', seasons[1], 'outside')
elif month == 6 or month == 7 or month == 8:
    print('There is a', seasons[2], 'outside')
else:
    print('There is a', seasons[3], 'outside')

#Решение со словарем

seasons_dict = {
    1: 'winter',
    2: 'spring',
    3: 'summer',
    4: 'fall'
}
month = int(input("Please, enter the number of the month "))
if month == 1 or month == 2 or month == 12:
     print('There is a', seasons_dict.get(1), 'outside')
elif month == 3 or month == 4 or month == 5:
     print('There is a', seasons_dict.get(2), 'outside')
elif month == 6 or month == 7 or month == 8:
     print('There is a', seasons_dict.get(3), 'outside')
else:
    print('There is a', seasons_dict.get(4), 'outside')