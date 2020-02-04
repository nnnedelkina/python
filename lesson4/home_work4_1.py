from sys import argv


def payment(output, rate, bonus):
    return float(output) * float(rate) + float(bonus)

try:
    output, rate, bonus = argv[1:]
    print('зарплата Иванов И.И. - ', payment(output, rate, bonus))
except ValueError:
    print('введите 3 числа')