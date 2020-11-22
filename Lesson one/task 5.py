income = int(input('Введите размер выручки вашего предприятия в млн.руб за текущий период : '))
costs = int(input('Введите размер издержек вашего предприятия в млн.руб за текущий период : '))
if income > costs:
    profit = income - costs
    print('Поздравляем! За текущий период Вы получили прибыль в размере : ', profit, 'млн.руб')
    benefit = profit / income
    print('Рентабельность текущего периода составляет : ', benefit)
    employees = int(input('Введите количество сотрудников вашей компании : '))
    benefit_employees = profit / employees
    print('Прибыль из расчета на одного сотрудникак составляет : ', benefit_employees, 'млн.руб')

else:
    loss = costs - income
    print('К сожалению, за текущий период ваш убыток составил', loss, 'млн.руб')


