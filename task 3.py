class Worker:
    name = input('Enter the name : ')
    surname = input('Enter the surname : ')
    position = input('Enter the position : ')
    salary = int(input('Enter the salary : '))
    bonus = int(input('Enter the bonus : '))
    _income = {'salary': salary, 'bonus': bonus}


class Position(Worker):


    def get_full_name(self):
        print(f'The full name of the worker is :  {Worker.name}  {Worker.surname}')


    def get_total_income(self):
        print(f' The total income of {Worker.name} {Worker.surname} is {sum(Worker._income.values())} ')


a = Position()
a.get_full_name()
a.get_total_income()