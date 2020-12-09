# import sys
#
#
# def count_salary():
#     hours = int(sys.argv[1])
#     hour_cost = int(sys.argv[2])
#     bonus = int(sys.argv[3])
#     salary = (hours * hour_cost) + bonus
#     return int(salary)
#
#
# count_salary()

from sys import argv

# hours, hour_cost, bonus = argv


def count_salary(hours, hour_cost, bonus):
    hours, hour_cost, bonus = argv
    salary = (hours * hour_cost) + bonus
    return salary


# n = count_salary(1, 2, 3)
# print(n)
