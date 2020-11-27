goods_quantity = int(input('Please enter goods quantity : '))
goods = []  # список кортежей
num = 1
names = []
prises = []
quantities = []
measures = []
while num <= goods_quantity:
    product = []  # список который станет кортежем. содержит 2 элемента - порядковый номер num и parametеrs (словарь)
    for parameters_i in range(1):
        name = input('Please enter product name : ')
        prise = input('Please enter product prise : ')
        quantity = input('Please enter product quantity : ')
        measure = input('Please enter product measure : ')
        parameters = dict(name=name, prise=prise, quantity=quantity, measure=measure)
        product.append(num)
        product.append(parameters)
        product = tuple(product)
        num += 1
        goods.append(product)
        names.append(name)
        prises.append(prise)
        quantities.append(quantity)
        measures.append(measure)
analytics = {'name': names,
             'price': prises,
             'quantity': quantities,
             'measure': measures
             }
print(analytics)
print(goods)


