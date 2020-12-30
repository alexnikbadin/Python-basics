import json

result = []
benefits = []
companies =[]
with open("companies.txt", 'r') as f:
    for line in f:
        line = line.split(' ')
        companies.append(line[0])
        benefits.append(int(line[2]) - int(line[3]))
        print(line)
    profit = dict([(companies[0], benefits[0]), (companies[1], benefits[1]), (companies[2], benefits[2])])
    average_profit = dict([('average profit', (benefits[0] + benefits[1] + benefits[2]) / 3)])
    result.append(profit)
    result.append(average_profit)
    print(profit)
    print(average_profit)
    print(result)

with open('result.json', 'w') as my_f:
    json.dump(result, my_f)

