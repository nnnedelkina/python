class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt

inp_divider = input('введите делитель: ')

try:
    divider = int(inp_divider)
    if divider == 0:
        raise OwnError('на ноль делить нельзя')
except ValueError:
    print('вы ввели не число')
except OwnError as err:
    print(err)
else:
    print('результат деления 100 на ваше число: ', 100 / divider)